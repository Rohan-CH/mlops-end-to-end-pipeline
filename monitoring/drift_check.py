# Simple example of generating a drift report using Evidently
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import os

def run_drift(reference_csv, current_csv, out_html='monitoring/drift_report.html'):
    ref = pd.read_csv(reference_csv)
    cur = pd.read_csv(current_csv)
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=ref, current_data=cur)
    report.save_html(out_html)
    print(f"Saved drift report to {out_html}")

if __name__ == '__main__':
    ref = '../data/processed/reference.csv'
    cur = '../data/processed/current.csv'
    if os.path.exists(ref) and os.path.exists(cur):
        run_drift(ref, cur)
    else:
        print('Place sample CSVs at', ref, 'and', cur)
