def get_aqi_category(aqi):

    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"


def health_advice(aqi):

    if aqi <= 50:
        return "Air quality is good. Enjoy outdoor activities."
    elif aqi <= 100:
        return "Air quality acceptable."
    elif aqi <= 200:
        return "Sensitive people should reduce outdoor activity."
    elif aqi <= 300:
        return "Wear mask and limit outdoor exposure."
    elif aqi <= 400:
        return "Avoid outdoor activities."
    else:
        return "Health warning! Stay indoors."
