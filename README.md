

# Objective-CLint

创建一个轻量级的、支持pre-commit的Objective-C 的静态检查

### 感谢

感谢 [spacecommander](https://github.com/square/spacecommander)作者提供的Objective-C lint的思路以及open source
本文大部分是基于 [spacecommander](https://github.com/square/spacecommander)累加的一些新功能。再次感谢开源作者，非常棒👍🏻

### 架构/构思

#### 1.前因

因为OC-Lint的重量型检查，导致如果使用OCLint 那么首先我们需要安装OCLint 以及 还需要编译工程，如果我们使用[pre-commit](https://pre-commit.com/)那么
就会导致我们每次 git commit 时间会增加很多，每次 commit可能对于我们来说都是一种煎熬。ok那么就需要我们使用另外的方式解决。

OK，解决方法之一就是我们之间使用Clang-format，我们知道其实OCLint也是基于Clang-format做的，那么在寻找的过程中发现了有伟大的 spacecommander 作者已经帮助我们集成了Clang-format
作者除此之外还解决了可能会引起Clang-format有歧义的代码修改、以及Clang-format 扫不到的一些规则修改。

那么有了伟大的 spacecommander 作为基础，我们就可以利用他做一个pre-commit hook，用来OClint

#### 2.相关实现、改动

1. 在spacecommander 的基础上，实现了支持pre-commit，更方便集成
2. spacecommander 只是对比了format之后行数，以用来比较是否有不否和规则的代码出现，不够明显，我们采用diff的方式对比了
   format之前和之后的代码，使得开发者能更清楚，自己哪些地方代码不规范
3. spacecommander 提供了api 一键format代码，我们不提供此功能，因为我总觉得只有多次的认识到不规范的代码，才能保证下次写出规范的代码
4. 提供了diff之后可视化输出，打开html，一眼即可看到不规范的代码
5. 修改了部分自定义规则代码，以适应灵活的代码不规范
6. [.clang-format](https://github.com/HaoXianSen/Objective-CLint/blob/main/.clang-format) 配置了更多的clang 规则

### 使用

#### 基于Pre-commit 工具

  1. 安装 pre-commit , ``` brew install pre-commit ```

  2. 在工程根目录添加(即.git同级目录)添加 [.pre-commit-config.yaml](https://github.com/HaoXianSen/Objective-CLint/blob/main/.pre-commit-config.yaml)

     ```yaml
     fail_fast: false
                repos:
                    - repo: https://github.com/HaoXianSen/Objective-CLint.git
                        rev: v1.0.2
                      hooks:
                         - id: objc-lint
                         name: objc-format
                        entry: format-objc-hook
                      language: script
            require_serial: true
            verbose: true
      # entry: format-objc-hook 后可添加下面更新的便捷性命令, 如 format-objc-hook --reporter open_html --auto--fix
     ```

  3. 根目录下放置.clang-format 文件，修改规则（可将此工程下的.clang-format copy 到自己工程根目录下）

  4. 执行```pre-commit install```

  4. 如果需要更新版本则 修改rev版本号，并且执行```pre-commit autoupdate```

#### homebrew 安装，手动执行

  1. ```brew tap haoxiansen/private```

  2. ```brew update && brew install objc-lint && brew upgrade objc-lint```

  3. ``` shell
     format-objc-hook -h
     ```

4. 在根目录下，使用相关命令手动执行。
   ```shell
      format-objc-hook --reporter [<terminal>, <html>, <open_html>] --output [<path>] --quiet --auto-fix
   ```

### 相关截图

![image-20220914145906934](https://cdn.jsdelivr.net/gh/HaoXianSen/HaoXianSen.github.io@master/screenshots/20220914145908image-20220914145906934.png)

  

![image-20220914145930603](https://cdn.jsdelivr.net/gh/HaoXianSen/HaoXianSen.github.io@master/screenshots/20220914145930image-20220914145930603.png

![image-20220914150033308](https://cdn.jsdelivr.net/gh/HaoXianSen/HaoXianSen.github.io@master/screenshots/20220914150033image-20220914150033308.png)

### 命令列表
```
   -h, --help # 帮助命令
   -v, --version # 当前版本
   --reporter [<terminal>, <html>, <open_html>] # 输出类型
   --output [<path>] # 输出html地址
   --quiet           # 静默执行
   --auto-fix        # 自动修复格式问题
```

----


### 2023年更新

* 增加一些便捷性命令

  * --reporter [<terminal>, <html>, <open_html>]

    增加报告类型，1、terminal 终端直接输出 2、html 终端输出html 3、 直接web打开html

  * --output [<path>]

    增加可配置输出目的地址，如果带有--output 输出会直接输出到指定文件

  * --quiet

    增加静默执行，即增加--quiet之后，全程不输出提示性、错误性的信息

* 美观report html

  * 嵌入开源三方库[diff2html](https://github.com/rtfpessoa/diff2html) 美观report html

  ![image-20230616114432297](https://cdn.jsdelivr.net/gh/HaoXianSen/HaoXianSen.github.io@master/screenshots/20230616114433image-20230616114432297.png)

### 2023.10

  * 修复pre-commit 工具不能运行问题
  * 增加--auto-fix 自动修复功能

### 2023 年后续迭代

  * 目录|多文件 非pre-commit支持


#### 联系方式
若有疑问或建议，可直接issues留言或邮件联系！看到后会第一时间回复~
邮箱：harry_c2016@163.com
