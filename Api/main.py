import requests

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 9.07,
        "longitude": 7.48,
        "current": "temperature_2m",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")
        return None

weather = get_weather()
print(weather)