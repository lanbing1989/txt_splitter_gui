# txt_splitter_gui

## 简介
`txt_splitter_gui` 是一个用于分割 TXT 文本文件的图形界面工具，旨在帮助用户将大型 TXT 文件按指定规则拆分为多个小文件，便于管理和后续处理。该项目主要使用 Python 开发，包含丰富的模块依赖，实现文本处理、压缩解压、文件操作等功能。

## 主要功能
- 支持将大文本文件分割成多个小文件
- 提供简单易用的图形界面
- 支持常见压缩格式（如 gzip、bz2、lzma 等）
- 支持自定义分割规则（如按行数、分隔符等）
- 分割后自动保存为新文件

## 安装方法
1. 克隆本仓库：
   ```bash
   git clone https://github.com/lanbing1989/txt_splitter_gui.git
   ```
2. 安装依赖（推荐使用 Python 3.8 及以上版本）：
   ```bash
   pip install -r requirements.txt
   ```
   *如未提供 requirements.txt，请根据实际环境安装 PyQt5 等 GUI 框架及所需依赖包。*

## 使用方法
1. 运行主程序：
   ```bash
   python txt_splitter_gui.py
   ```
2. 在界面中选择需要拆分的 TXT 文件
3. 设定分割参数（如每个文件的行数或分隔符等）
4. 点击“开始分割”按钮，等待分割完成
5. 分割结果会自动保存在指定目录

## 依赖
- Python 3.x
- PyQt5 或 Tkinter（依据实际 GUI 框架）
- 其他常用依赖（如 gzip、bz2、lzma、os、heapq、hashlib、logging、shutil 等）

## 许可证
本项目当前未指定开源许可证。如需商用或二次开发，请联系作者。

## 贡献
欢迎提交 issue 或 pull request 改进本项目。

## 联系方式
- 作者: [lanbing1989](https://github.com/lanbing1989)

> **备注**：本 README 依据代码结构自动生成，实际功能和用法请以源代码和界面为准。
