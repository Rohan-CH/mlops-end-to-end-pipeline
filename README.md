House Price Prediction (End-to-End)

This repository is an end-to-end **MLOps** example that demonstrates:
- Model training and experiment tracking with **MLflow**
- Data and model versioning using **DVC**
- Model serving with **FastAPI**
- Containerization with **Docker**
- Deployment manifests for **Kubernetes (minikube)**
- A simple training DAG using **Airflow**
- Basic data drift monitoring using **Evidently**

## Quick start (local)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run training (creates `src/model.pkl` and logs to MLflow):
   ```bash
   python src/train.py
   ```
3. Start the API:
   ```bash
   cd api
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```
4. Predict:
   ```bash
   curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '[0.1, 8.3252, 41, 6.9841, 1, 322, 2.5556, 37.88]'
   ```

## Project layout
```
data/                 # raw and processed data (DVC-managed)
src/                  # training, preprocessing, utils
api/                  # FastAPI model server + Dockerfile
k8s/                  # Kubernetes manifests
pipelines/            # Airflow DAG or Prefect flow
monitoring/           # Evidently drift report example
```

## Author
Rohan Chakkadath
