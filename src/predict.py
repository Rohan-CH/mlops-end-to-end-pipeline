import joblib
import numpy as np
import os
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

def predict(features):
    model = joblib.load(MODEL_PATH)
    arr = np.array([features])
    return float(model.predict(arr)[0])

if __name__ == '__main__':
    # example feature vector (8 features for California housing)
    sample = [0.02, 6.0, 60.0, 3.0, 5.0, 200.0, 2.5, 34.0]
    print("Prediction:", predict(sample))
