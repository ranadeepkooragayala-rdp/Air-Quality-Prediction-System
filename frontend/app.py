import requests
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Air Quality System", layout="centered")

st.title("🌍 Real-Time Air Quality Prediction System")
st.markdown("### AI-Based AQI Monitoring & Health Advisory")

API_KEY = "Your_API_Key"

# 🌆 City Input (NEW)
city = st.text_input("Enter City Name", "Hyderabad")

if st.button("🔄 Get AQI"):
    
    # 🌍 Convert City → Lat/Lon
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    geo_response = requests.get(geo_url)

    if geo_response.status_code == 200 and geo_response.json():
        geo_data = geo_response.json()[0]
        lat = geo_data["lat"]
        lon = geo_data["lon"]

        st.success(f"📍 Location: {city}")

        # 🌫️ Pollution API
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            components = data["list"][0]["components"]

            st.markdown("### 📊 Pollutant Levels")
            st.dataframe({
                "Pollutant": ["PM2.5", "PM10", "NO", "NO2", "NH3", "CO", "SO2", "O3"],
                "Value": [
                    components["pm2_5"], components["pm10"], components["no"],
                    components["no2"], components["nh3"], components["co"],
                    components["so2"], components["o3"]
                ]
            })

            # 🧠 Prepare input
            input_data = {
                "PM25": components["pm2_5"],
                "PM10": components["pm10"],
                "NO": components["no"],
                "NO2": components["no2"],
                "NOx": components["no"] + components["no2"],
                "NH3": components["nh3"],
                "CO": components["co"],
                "SO2": components["so2"],
                "O3": components["o3"],
                "Benzene": 0,
                "Toluene": 0,
                "Xylene": 0
            }

            try:
                prediction_response = requests.post(
                    "http://127.0.0.1:8000/predict",
                    json=input_data
                )

                if prediction_response.status_code == 200:
                    result = prediction_response.json()

                    aqi = result["predicted_aqi"]
                    category = result["category"]
                    advice = result["health_advice"]

                    st.markdown("### 📈 AQI Prediction")

                    # 🎯 Gauge
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=aqi,
                        title={'text': "AQI Level"},
                        gauge={
                            'axis': {'range': [0, 500]},
                            'steps': [
                                {'range': [0, 50], 'color': "#2ecc71"},
                                {'range': [50, 100], 'color': "#f1c40f"},
                                {'range': [100, 200], 'color': "#e67e22"},
                                {'range': [200, 300], 'color': "#e74c3c"},
                                {'range': [300, 400], 'color': "#8e44ad"},
                                {'range': [400, 500], 'color': "#7f0000"},
                            ],
                        }
                    ))

                    st.plotly_chart(fig)

                    # 🎨 Category color
                    if aqi <= 50:
                        color = "#2ecc71"
                    elif aqi <= 100:
                        color = "#f1c40f"
                    elif aqi <= 200:
                        color = "#e67e22"
                    elif aqi <= 300:
                        color = "#e74c3c"
                    elif aqi <= 400:
                        color = "#8e44ad"
                    else:
                        color = "#7f0000"

                    st.markdown(
                        f"""
                        <div style="
                            padding:15px;
                            border-radius:12px;
                            background-color:{color};
                            color:white;
                            font-size:20px;
                            text-align:center;
                            font-weight:bold;">
                            {category}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.progress(min(aqi / 500, 1.0))
                    st.info(f"💡 {advice}")

                else:
                    st.error("Prediction failed")

            except Exception as e:
                st.error(f"FastAPI error: {e}")

        else:
            st.error("Pollution API failed")

    else:
        st.error("City not found ❌")
