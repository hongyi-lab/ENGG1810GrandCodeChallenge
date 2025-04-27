from labelme2coco import convert
import os

labelme_folder = r"D:\trainingdata\4.17flydata1"
output_json = os.path.join(labelme_folder, "iron_coco.json")

convert(labelme_folder, output_json)
print("✅ COCO 格式数据生成完成：", output_json)
