### 使用 pyinstaller 打包可执行文件


* 单文件 
```bash
  pyinstaller app.py

```

* 静态文件
在使用PyInstaller进行打包时，如果你不希望编译静态文件，可以使用--add-data参数来指定需要包含的文件或目录，而不进行编译。

以下是一个示例命令：

bash
```py
    pyinstaller --add-data "path/to/static/files:static" your_script.py
```
在这个例子中：

```py
    pyinstaller --add-data "web:web" your_script.py
```
path/to/static/files 是包含你的静态文件的目录。
static 是你希望在打包后的可执行文件中的目标目录。
通过这样的方式，PyInstaller将直接复制静态文件到打包后的目录，而不会进行编译。

请确保你的脚本中引用静态文件的路径是相对路径，并且与--add-data中指定的目录结构一致。


* pyinstaller 生成spec配置文件


PyInstaller可以通过生成一个spec文件来配置打包过程。spec文件是一个文本文件，包含了用于构建可执行文件的配置信息。

以下是一个简单的示例，演示如何使用PyInstaller生成一个spec文件：

打开命令行终端。
进入包含你的Python脚本的目录。
然后执行以下命令：

```bash
pyinstaller --name your_executable_name your_script.py --specpath build_folder
```
在这个命令中：

your_executable_name 是你希望生成的可执行文件的名称。
your_script.py 是你的Python脚本的文件名。
build_folder 是一个目录，用于存放生成的spec文件以及其他构建过程中产生的临时文件。
执行完这个命令后，你会在指定的build_folder中找到生成的spec文件，其文件名通常为your_script.spec。

你可以编辑这个spec文件，以满足你特定的需求。spec文件使用Python语法，你可以在其中指定诸如数据文件、依赖项等的详细配置。编辑完成后，你可以使用以下命令来构建可执行文件：

```bash
pyinstaller your_script.spec
```
这将根据你的spec文件进行构建，并生成最终的可执行文件