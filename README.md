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

1. 安装 pre-commit , ``` brew install pre-commit ```

2. 在工程根目录添加(即.git同级目录)添加 [.pre-commit-config.yaml](https://github.com/HaoXianSen/Objective-CLint/blob/main/.pre-commit-config.yaml)

   并配置为：

   ```
   fail_fast: false
   repos:
     - repo: https://github.com/HaoXianSen/Objective-CLint.git
       rev: v0.0.3
       hooks:
         - id: objc-lint
           name: objc-format
           entry: format-objc-hook
           language: script
           require_serial: true
           verbose: true
   ```

   **高阶使用**

   fork 工程，可修改、增加自定义规则，以及.clang 规则

### 相关截图

![image-20220914145906934](https://cdn.jsdelivr.net/gh/HaoXianSen/HaoXianSen.github.io@master/screenshots/20220914145908image-20220914145906934.png)

  

![image-20220914145930603](https://cdn.jsdelivr.net/gh/HaoXianSen/HaoXianSen.github.io@master/screenshots/20220914145930image-20220914145930603.png)

![image-20220914150033308](https://cdn.jsdelivr.net/gh/HaoXianSen/HaoXianSen.github.io@master/screenshots/20220914150033image-20220914150033308.png)



#### 联系方式

harry_c2016@163.com
