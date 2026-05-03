# Task
本人的实践周作业

# 学生成绩管理系统

一个命令行交互的成绩管理工具，使用 Python 3 开发，支持添加学生、展示列表、计算平均分，并自动保存数据到 JSON 文件。

## 学习资料来源及相关链接

- Python 官方文档（中文）：https://docs.python.org/zh-cn/3/
- Python JSON 模块教程：https://docs.python.org/zh-cn/3/library/json.html
- Git 与 GitHub 入门：https://git-scm.com/book/zh/v2
- GitHub Desktop 使用文档：https://docs.github.com/zh/desktop
- 菜鸟教程 Python3：https://www.runoob.com/python3/

## 实践流程

### 环境准备
1. 安装 Python 3.8 及以上版本，确保已添加到系统 PATH。
2. 下载并安装 GitHub Desktop，登录 GitHub 账号。
3. 在 GitHub 网页上创建空仓库 `Task`。

### 项目开发
1. 用 GitHub Desktop 将空仓库克隆到本地。
2. 第一次提交：创建 `main.py`、`.gitignore`、`README.md`，实现主菜单循环框架。
3. 第二次提交：编写 `student_manager.py` 实现学生添加、展示、平均分计算，修改 `main.py` 调用业务逻辑，更新 README。
4. 第三次提交：增加 JSON 文件读写实现数据持久化，增强输入校验，完善 README。


### 遇到的问题及解决方法
问题1：JSON 文件首次运行时不存在导致读取失败
现象：运行程序时报错 FileNotFoundError: [Errno 2] No such file or directory: 'data.json'
解决方法：在 _load_data()函数中使用 os.path.exists(DATA_FILE) 检查文件是否存在，不存在则返回空列表 []。这样首次运行不会报错，且添加学生后会自动创建 JSON 文件。

问题2：成绩输入非数字字符时程序崩溃
现象：当用户输入 abc 作为成绩时，float() 转换抛出 ValueError，程序直接退出。
解决方法：在 main.py 中捕获 ValueError 异常，提示“成绩必须为数字！”并用 continue 回到菜单，保持程序稳定运行。同时增加姓名空字符串检查，提升用户体验。

### Git 学习心得
通过本次实践，我真正理解了 Git 不只是“备份代码”，它的核心价值在于版本追踪和变更管理。
以前我习惯写完所有代码再一次性上传，但这次刻意拆分成三个有逻辑的提交，体会到了“一个提交只做一件事”的意义，这让代码演进过程可追溯、易回滚。
GitHub Desktop 降低了操作门槛，可视化查看 diff 和历史记录，让我更专注于代码本身而非命令行指令。
写好 commit message 很重要，清晰的注释让自己几周后也能快速回忆改动原因，也方便团队协作。
遇到文件状态混乱时，学会了在 Desktop 中右键 Discard changes 或查看历史，避免盲目覆盖代码。
Git 将成为我后续学习和项目开发中不可或缺的工具，这次实践为养成良好的版本控制习惯打下了基础。
