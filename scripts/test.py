from ultralytics import YOLO

# 1. 파인튜닝된 모델 불러오기 (경로는 실제 저장된 best.pt로)
best_model = YOLO('cockroach_detection/yolov8x_cockroach/weights/best.pt')

# 2. 폴더 전체 테스트 및 결과 저장
results = best_model.predict(
    source='dataset/test/images',
    conf=0.4,
    save=True,
    project='results',   # yolov8/results 폴더에 저장
    name='test_output'   # results/test_output 폴더 생성
)

# 3. 결과 시각화 (원하면)
results.show()
