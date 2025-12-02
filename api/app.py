from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
import numpy as np

app = FastAPI(title="House Price Prediction API")

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'src', 'model.pkl')
if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f'Model not found. Run training first and ensure {MODEL_PATH} exists.')

model = joblib.load(MODEL_PATH)

class Features(BaseModel):
    features: list

@app.get('/')
def root():
    return {"message": "House Price Prediction API - send POST to /predict with JSON [feature_list]"}

@app.post('/predict')
def predict(data: Features):
    features = data.features
    if not isinstance(features, list):
        raise HTTPException(status_code=400, detail="features must be a list")
    arr = np.array([features])
    pred = model.predict(arr)[0]
    return {"prediction": float(pred)}
