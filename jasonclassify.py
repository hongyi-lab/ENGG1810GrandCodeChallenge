import os
import shutil


def extract_json_files(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹
    json_count = 0
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('.json'):
                # 构造源文件和目标文件路径
                src_path = os.path.join(root, file)
                dst_path = os.path.join(output_folder, file)

                # 如果目标文件已存在，添加序号避免覆盖
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(dst_path):
                    new_file = f"{base}_{counter}{ext}"
                    dst_path = os.path.join(output_folder, new_file)
                    counter += 1

                # 复制文件
                shutil.copy2(src_path, dst_path)
                json_count += 1

    print(f"Extracted {json_count} JSON files to {output_folder}")


# 示例用法
if __name__ == "__main__":
    # 替换为你的输入和输出文件夹路径
    input_folder = r"D:\桌面\train"
    output_folder = r"D:\AAAUAVdata\SelfJson"
    extract_json_files(input_folder, output_folder)