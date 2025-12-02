FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy API and model (assuming model already exists in src/model.pkl)
COPY . /app
COPY ../src/model.pkl /app/model.pkl

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
