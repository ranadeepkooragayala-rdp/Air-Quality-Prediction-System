from fastapi import FastAPI
from schemas import AQIInput
from model_loader import predict_aqi
from utils import get_aqi_category, health_advice

app = FastAPI(title="Air Quality Prediction API")

@app.get("/")
def home():
    return {"message": "Air Quality Prediction System Running"}

@app.post("/predict")
def predict(data: AQIInput):

    aqi = predict_aqi(data)
    category = get_aqi_category(aqi)
    advice = health_advice(aqi)

    return {
        "predicted_aqi": round(aqi, 2),
        "category": category,
        "health_advice": advice
    }
