import mlflow
import mlflow.sklearn
import joblib
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import os
import numpy as np
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

def load_data():
    data = fetch_california_housing(as_frame=True)
    df = pd.concat([data.data, data.target.rename('target')], axis=1)
    # Simple preprocessing example: drop NA (none in this dataset)
    return df

def train_model(n_estimators=100, random_state=42):
    df = load_data()
    X = df.drop(columns=['target']).values
    y = df['target'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)

    with mlflow.start_run():
        model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        rmse = mean_squared_error(y_test, preds, squared=False)

        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("random_state", random_state)
        mlflow.log_metric("rmse", rmse)
        mlflow.sklearn.log_model(model, artifact_path="model")

        joblib.dump(model, MODEL_PATH)

        print(f"Run logged. RMSE: {rmse:.4f}")
        return rmse

if __name__ == '__main__':
    train_model()
