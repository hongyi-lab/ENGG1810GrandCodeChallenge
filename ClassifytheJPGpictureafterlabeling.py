import os
import shutil
from tkinter import Tk, filedialog


def select_folder(prompt):
    root = Tk()
    root.withdraw()  # 隐藏主窗口
    folder = filedialog.askdirectory(title=prompt)
    root.destroy()
    return folder


def copy_jpg_files():
    # 选择源文件夹
    source_folder = select_folder("请选择包含JPG文件的源文件夹")
    if not source_folder:
        print("未选择源文件夹")
        return

    # 选择目标文件夹
    dest_folder = select_folder("请选择目标文件夹")
    if not dest_folder:
        print("未选择目标文件夹")
        return

    # 确保目标文件夹存在
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 遍历源文件夹
    jpg_count = 0
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'):
                source_path = os.path.join(root, file)
                dest_path = os.path.join(dest_folder, file)

                # 如果目标文件已存在，添加数字后缀
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(dest_path):
                    new_filename = f"{base}_{counter}{ext}"
                    dest_path = os.path.join(dest_folder, new_filename)
                    counter += 1

                # 复制文件
                shutil.copy2(source_path, dest_path)
                jpg_count += 1
                print(f"已复制: {file}")

    print(f"\n操作完成，共复制 {jpg_count} 个JPG文件")


if __name__ == "__main__":
    copy_jpg_files()