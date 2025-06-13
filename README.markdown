# 🎉 MacJunkCleaner

## 🌟 概述 / Overview
**MacJunkCleaner** 是一个用于清理 macOS 系统垃圾文件的工具，适用于 Windows 系统。它可以删除 macOS 在外部存储设备（如 U 盘）上生成的常见垃圾文件和文件夹，例如 `.DS_Store` 和 `.Trashes`。

**MacJunkCleaner** is a tool for cleaning macOS junk files, designed for Windows systems. It removes common macOS-generated junk files and folders (e.g., `.DS_Store`, `.Trashes`) from external storage devices like USB drives.

## 🚀 功能 / Features
- **文件清理 / File Cleanup**: 🗑️ 删除 `.DS_Store`、`.` 开头文件等 macOS 垃圾文件。
- **文件夹清理 / Folder Cleanup**: 🗂️ 移除 `.Trashes`、`.Spotlight-V100` 等系统文件夹。
- **图形界面 / GUI**: 🎨 通过文件夹选择对话框选择清理路径。
- **日志记录 / Logging**: 📝 将清理记录保存为 `cleanup_log.txt`。
- **中英双语 / Bilingual**: 🌐 支持中英双语提示和日志。

- **File Cleanup**: 🗑️ Deletes macOS junk files like `.DS_Store` and `._` files.
- **Folder Cleanup**: 🗂️ Removes system folders like `.Trashes` and `.Spotlight-V100`.
- **GUI**: 🎨 Uses a folder selection dialog to choose the cleanup path.
- **Logging**: 📝 Saves cleanup records to `cleanup_log.txt`.
- **Bilingual**: 🌐 Supports mid-English prompts and logs.

## 📥 安装 / Installation
### Windows
1. 下载 **MacJunkCleaner.exe**（见 [Releases](https://github.com/ScorpioDai/MacJunkCleaner/releases)）。
2. 双击运行，无需安装 Python 或其他依赖。
3. 日志文件 `cleanup_log.txt` 将生成在程序运行目录。

1. Download **MacJunkCleaner.exe** (see [Releases](https://github.com/ScorpioDai/MacJunkCleaner/releases)).
2. Double-click to run; no Python or dependencies required.
3. A log file `cleanup_log.txt` will be created in the program’s directory.

### 开发者 / Developers
若需运行源代码：
1. 安装 Python 3.8+ 和 `tkinter`（通常包含在 Python 中）。
2. 下载 `MacJunkCleaner.py`。
3. 运行：
   ```bash
   python MacJunkCleaner.py
   ```

To run the source code:
1. Install Python 3.8+ with `tkinter` (usually included).
2. Download `MacJunkCleaner.py`.
3. Run:
   ```bash
   python MacJunkCleaner.py
   ```

## 🎮 使用方法 / Usage
1. 运行 **MacJunkCleaner.exe** 或 `MacJunkCleaner.py`。
2. 在弹出的对话框中选择要清理的目录（例如 U 盘根目录）。
3. 程序将显示清理进度并记录到 `cleanup_log.txt`。
4. 按回车键退出。

1. Run **MacJunkCleaner.exe** or `MacJunkCleaner.py`.
2. Select the directory to clean (e.g., USB drive root) in the dialog.
3. The program displays cleanup progress and logs to `cleanup_log.txt`.
4. Press Enter to exit.

## 📋 示例日志 / Sample Log
```
🍏 macOS垃圾文件清理工具 v1.0 (macOS Junk File Cleaner v1.0)
✅ 已删除文件: D:\.DS_Store (File deleted: D:\.DS_Store)
🧹 清理完成，共删除文件 1 个，文件夹 0 个。 (Cleanup complete, deleted 1 files and 0 folders.)
```

## 📜 许可证 / License
本项目采用 **[MIT License](LICENSE)**。欢迎使用、修改和分发！🎁

This project is licensed under the **[MIT License](LICENSE)**. Feel free to use, modify, and distribute! 🎁

## 🤝 贡献 / Contributing
欢迎提交问题或拉取请求！请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting issues or pull requests.

## 📧 联系 / Contact
- GitHub: [ScorpioDai](https://github.com/ScorpioDai)
