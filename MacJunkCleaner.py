import os
import shutil
import platform
import tkinter as tk
from tkinter import filedialog
import sys
import logging

# 配置日志 (Configure logging)
log_file = os.path.join(os.getcwd(), "cleanup_log.txt")
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    encoding="utf-8",
    handlers=[
        logging.FileHandler(log_file, mode="a", encoding="utf-8"),  # 追加到文件 (Append to file)
        logging.StreamHandler()  # 输出到控制台 (Output to console)
    ]
)

# 要清除的文件和文件夹特征 (Files and folders to be deleted)
DELETE_FILE_PATTERNS = [
    ".DS_Store",             # 文件夹图标配置 (Folder icon configuration)
    "Icon\r",                # 老系统的图标配置 (Old system icon configuration)
]

DELETE_FOLDER_NAMES = [
    ".Spotlight-V100",
    ".TemporaryItems",
    ".Trashes",
    ".fseventsd",
]

def is_mac_junk_file(filename):
    return (
        filename in DELETE_FILE_PATTERNS or
        filename.startswith("._") or
        filename.endswith("Icon\r") or
        filename in DELETE_FOLDER_NAMES
    )

def clean_mac_junk(base_path):
    deleted_files = 0
    deleted_folders = 0

    for dirpath, dirnames, filenames in os.walk(base_path, topdown=False):
        # 删除文件 (Delete files)
        for file in filenames:
            if is_mac_junk_file(file):
                full_path = os.path.join(dirpath, file)
                try:
                    os.remove(full_path)
                    logging.info(f"✅ 已删除文件: {full_path} (File deleted: {full_path})")
                    deleted_files += 1
                except Exception as e:
                    logging.info(f"❌ 删除文件失败: {full_path}，错误: {e} (Failed to delete file: {full_path}, Error: {e})")

        # 删除目录 (Delete directories)
        for folder in dirnames:
            if folder in DELETE_FOLDER_NAMES:
                folder_path = os.path.join(dirpath, folder)
                try:
                    shutil.rmtree(folder_path)
                    logging.info(f"📁 已删除文件夹: {folder_path} (Folder deleted: {folder_path})")
                    deleted_folders += 1
                except Exception as e:
                    logging.info(f"❌ 删除文件夹失败: {folder_path}，错误: {e} (Failed to delete folder: {folder_path}, Error: {e})")

    logging.info(f"\n🧹 清理完成，共删除文件 {deleted_files} 个，文件夹 {deleted_folders} 个。 (Cleanup complete, deleted {deleted_files} files and {deleted_folders} folders.)")

if __name__ == "__main__":
    # 在打包环境下确保正确处理路径 (Ensure proper path handling in packaged environment)
    if getattr(sys, 'frozen', False):
        # 运行在 PyInstaller 打包后的环境 (Running in PyInstaller bundled environment)
        os.chdir(os.path.dirname(sys.executable))
    logging.info("🍏 macOS垃圾文件清理工具 v1.0 (macOS Junk File Cleaner v1.0)")
    # 初始化 tkinter (Initialize tkinter)
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口 (Hide main window)
    logging.info("请在弹出的窗口中选择要清理的目录... (Please select the directory to clean in the pop-up window...)")
    # 弹出文件夹选择对话框 (Pop up folder selection dialog)
    target_path = filedialog.askdirectory(title="选择要清理的目录 (Select Directory to Clean)")
    root.destroy()  # 销毁 tkinter 实例 (Destroy tkinter instance)
    if not target_path:
        logging.info("❌ 未选择目录，程序退出。 (No directory selected, program exiting.)")
    elif not os.path.exists(target_path):
        logging.info("❌ 路径不存在，请重新运行脚本。 (Path does not exist, please rerun the script.)")
    else:
        clean_mac_junk(target_path)
    # 保持控制台窗口打开 (Keep console window open)
    logging.info("\n按回车键退出... (Press Enter to exit...)")
    input()