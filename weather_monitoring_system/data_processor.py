def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_weather_data(data):
    if 'main' not in data or 'weather' not in data:
        print(f"Error: Missing data in API response - {data}")
        return None, None, None, None

    temp = kelvin_to_celsius(data['main']['temp'])
    feels_like = kelvin_to_celsius(data['main']['feels_like'])
    weather_condition = data['weather'][0]['main']
    timestamp = data['dt']
    
    return temp, feels_like, weather_condition, timestamp
