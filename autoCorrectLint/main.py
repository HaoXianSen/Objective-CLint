# This is a sample Python script.
import subprocess

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import yamlParse
import os
import sqlite3

cache_home = "~/.cache/pre-commit"

def getLintRepos():
    last_dir = os.path.abspath(os.path.pardir)
    print(f"parentPath: {last_dir}")
    path = f"{last_dir}/.pre-commit-config.yaml"
    print(f"yaml: {path}")

    if not os.path.exists(path):
        raise Exception(".pre-commit-config.yaml 文件不存在，请添加此文件、并配置相关lint")

    parse_data = yamlParse.parse_yaml(path)

    repos = ["https://github.com/HaoXianSen/Objective-CLint.git", "https://github.com/realm/SwiftLint"]
    all_repos = parse_data["repos"]
    repos_dict = []
    for repo in all_repos:
        if repo["repo"] in repos:
            repo_dict = {"repo": repo['repo'], "rev" : repo['rev']}
            repos_dict.append(repo_dict)
    return repos_dict


def check_pepo_local_path(repos):
    path = os.path.join(os.path.expanduser(cache_home), "db.db")
    if not os.path.exists(path):
        raise Exception("当前没有安装pre-commit hooks, 请安装pre-commit并安装hooks，才能进行代码自动格式化")

    sqlite = sqlite3.connect(path).cursor()
    repo_local_paths = []
    for repo in repos:
        cursor = sqlite.execute("SELECT * FROM repos WHERE repo=? and ref=?", (repo["repo"], repo["rev"]))
        path = cursor.fetchone()[2]
        repo_single = {"repo": repo["repo"], "path": path}
        repo_local_paths.append(repo_single)
    sqlite.close()
    return repo_local_paths


def autoLintObjctiveC(path):

    os.chdir(os.path.abspath(os.path.pardir))
    if not os.path.exists(path):
        raise Exception(f"{path} 不存在")

    parentPath = os.path.abspath(os.path.curdir)
    data = subprocess.getoutput("git diff --cached --name-only | grep -e '\.m$' -e '\.mm$' -e '\.h$' -e '\.hh$'")
    if len(data) <= 0:
        return

    def appending_path(path):
        return f"{parentPath}/{path}"
    data = data.split("\n")
    all_modified_paths = map(appending_path, data)
    data_list = list(all_modified_paths)
    cmd_path = f"{path}/format-objc-file.sh"
    for git_paths in data_list:
        result = os.system(f"sh {cmd_path} {git_paths}")
        if result == 0:
            print(f"{git_paths} 成功")
        else:
            print(f"{git_paths} 失败")


def autoLintSwift(path):
    if not os.path.exists(path):
        raise Exception(f"{path} 不存在")


def open_cache_file_and_excute(repos):
    object_c_lint_path = ""
    swift_lint_path = ""
    for repo in repos:
        repo_name = repo["repo"]
        repo_local_path = repo["path"]
        if repo_name == "https://github.com/HaoXianSen/Objective-CLint.git":
            object_c_lint_path = repo_local_path
        elif repo_name == "https://github.com/realm/SwiftLint":
            swift_lint_path = repo_local_path

    if len(object_c_lint_path) > 0:
        autoLintObjctiveC(object_c_lint_path)
    if len(swift_lint_path) > 0:
        autoLintSwift(swift_lint_path)
    print("已经自动修改了缓存git里的代码规范")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     data = check_pepo_local_path(getLintRepos())
     open_cache_file_and_excute(data)

