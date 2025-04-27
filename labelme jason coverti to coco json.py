from labelme2coco import convert

labelme_folder = r"D:\AAAUAVdata\SelfJson"  # ← 清理后的文件夹！
output_json = r"D:\AAAUAVdata\CocoJson\dataset.json"

convert(labelme_folder, output_json)
