import joblib
import numpy as np

model = joblib.load("../ml/model.pkl")

def predict_aqi(data):
    arr = np.array([[
        data.PM25,
        data.PM10,
        data.NO,
        data.NO2,
        data.NOx,
        data.NH3,
        data.CO,
        data.SO2,
        data.O3,
        data.Benzene,
        data.Toluene,
        data.Xylene
    ]])

    prediction = model.predict(arr)
    return float(prediction[0])
