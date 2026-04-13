import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    weather = {
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "status": data["weather"][0]["description"]
    }
    return weather
