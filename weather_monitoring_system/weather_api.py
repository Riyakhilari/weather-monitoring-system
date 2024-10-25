import requests

def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)

    # Check response status
    if response.status_code != 200:
        print(f"Error fetching data for {city}: {response.status_code} - {response.text}")
        return {}

    return response.json()
