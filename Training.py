from ultralytics import YOLO
import torch

# 检测使用设备
device = 0 if torch.cuda.is_available() else "cpu"
print("🚀 使用设备:", device)

# 加载 YOLOv8 Nano 预训练模型
model = YOLO("yolov8n.pt")  # ✅ Nano版本

# 训练模型
model.train(
    data=r"D:\AAAUAVdata\AAAUAVdata\mygatedata.yaml",  # ✅ 这里改成你的最新yaml路径！
    epochs=100,
    imgsz=640,
    batch=8,
    device=device
)
