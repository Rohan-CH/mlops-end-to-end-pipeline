import pandas as pd
from sklearn.datasets import fetch_california_housing
import os

def write_raw_csv(path):
    data = fetch_california_housing(as_frame=True)
    df = pd.concat([data.data, data.target.rename('target')], axis=1)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Wrote raw data to {path}")

if __name__ == '__main__':
    write_raw_csv('../data/raw/housing.csv')
