# Monitoring
Place production samples as CSV in data/processed/current.csv and a reference CSV in data/processed/reference.csv
Then run:
```
python monitoring/drift_check.py
```
The script will create monitoring/drift_report.html
