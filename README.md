# Cockroach Project

## 프로젝트 개요
이 프로젝트는 특정 분야(예: 해충 탐지, AI 모델링 등)에 대한 데이터 분석 및 모델 개발을 목적으로 합니다.  
본 저장소는 모델 학습 결과, 평가 지표, 시각화 자료를 포함하고 있습니다.

## 주요 내용
- 모델 학습 결과 파일 (`models/best.pt` 등)
- 평가 지표 및 결과 시각화 (confusion matrix, precision-recall curve 등)
- 데이터셋 및 전처리 코드
- 주요 성능 평가 이미지와 그래프(`.jpg` 파일)

## 모델 요약

- Best 모델은 epoch 74에서 저장.
- 전체 94 epoch 학습, 시간은 약 33.8시간 소요
- best 모델의 크기: 약 136.7MB
- 총 모델 구조: 112 layer, 약 68M 파라미터, 연산량 257.4 GFLOPs(YOLOv8x 대형 모델)
- 검증 데이터셋(215 이미지, 339 인스턴스) 기준 성능
- Box(P): 0.733 (정확도, precision)
- R: 0.746 (재현율, recall)
- mAP50: 0.779 (IoU 0.5 기준 평균 정밀도)
- mAP50-95: 0.432 (다양한 IoU 기준 평균 정밀도)

## 설치 및 실행 방법

1. Python 가상환경 생성 및 활성화  
    ```
    python -m venv venv
    source venv/bin/activate  # Windows는 venv\Scripts\activate
    ```
2. 필수 패키지 설치  
    ```
    pip install -r requirements.txt
    ```
3. 학습 및 테스트 스크립트 실행 방법
    ```
    python train.py
    python test.py
    ```
4. main.py 사용법
- `main.py`는 모델 인퍼런스(추론) API 서버 역할을 합니다.
- 실행 방법
    ```
    uvicorn main:app --reload
    ```
- 웹 브라우저에서 `http://127.0.0.1:8000/docs` 접속 시 API 인터페이스 확인 가능
- API 엔드포인트 `/predict/`로 이미지 업로드 후 해충 탐지 결과(바운딩 박스 이미지)를 얻을 수 있습니다.
- 결과는 JSON 또는 base64 이미지 형태로 반환되어 UI와 쉽게 연동 가능합니다.

## Git LFS 관련 안내
- 큰 모델 파일(`best.pt`)은 Git LFS로 관리합니다.  
- Git LFS가 설치되어 있지 않다면 [설치 가이드](https://git-lfs.github.com/)를 참고하세요.

