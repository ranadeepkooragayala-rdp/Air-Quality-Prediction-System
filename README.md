# 🌍 AI-Based Real-Time Air Quality Prediction & Health Advisory System

🚀 Live ML project that predicts Air Quality Index (AQI) using real-time data and provides health recommendations.
---

## 📸 Demo

<img width="1611" height="709" alt="image" src="https://github.com/user-attachments/assets/379926a8-2cb4-4fb6-b462-54ec990ac5f2" />


---

## 📌 Overview
This project is an end-to-end AI-powered system that predicts Air Quality Index (AQI) using real-time environmental data and provides health recommendations.

It integrates Machine Learning, FastAPI, and Streamlit to deliver an interactive and user-friendly experience.

---

## 🚀 Features

- 🌆 City-based AQI prediction
- 🌫️ Real-time pollution data using API
- 🧠 Machine Learning model
- 🎯 AQI gauge visualization
- 📊 Historical AQI trend graph
- 💡 Health advisory system
- 🌐 FastAPI backend
- 🎨 Streamlit frontend

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- Scikit-learn
- Pandas & NumPy
- Plotly
- OpenWeather API

---
## 📂 Project Structure
app/ → Backend
frontend/ → UI
ml/ → Model
data/ → Dataset

---

## ⚙️ How to Run

pip install -r requirements.txt
uvicorn app.main:app --reload
streamlit run frontend/app.py

---

## 📊 Workflow

1. Enter city name  
2. Fetch real-time pollution data  
3. Send to ML model via FastAPI  
4. Predict AQI  
5. Display results with visualization  

---

## ⚙️ How It Works

1. User enters city name  
2. System fetches real-time pollution data  
3. Data is sent to FastAPI backend  
4. ML model predicts AQI  
5. Results displayed with:
   - AQI value
   - Category
   - Health advice
   


## ⚠️ Model File Note

The trained model file (model.pkl) is not included due to GitHub size limitations.

To generate the model:

python ml/train_model.py

## 🧠 Key Learnings

- Built end-to-end ML system
- Integrated real-time APIs
- Developed backend using FastAPI
- Designed interactive UI using Streamlit


## 👨‍💻 Author

Ranadeep Kooragayala

---

## ⭐ Star this repo if you like it!



