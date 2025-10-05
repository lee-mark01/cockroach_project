from ultralytics import YOLO

# 1. 모델 불러오기 (사전학습 모델)
model = YOLO('yolov8x.pt')

# 2. 파인튜닝 (YOLO 기본 증강 사용)

if __name__ == "__main__":
    model = YOLO('yolov8x.pt')
    results = model.train(
        data='dataset/data.yaml',
        epochs=100,
        imgsz=640,
        batch=16,
        patience=20,
        project='cockroach_detection',
        name='yolov8x_cockroach',
        augment=True
    )
