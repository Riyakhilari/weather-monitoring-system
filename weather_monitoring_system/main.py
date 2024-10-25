import json
import time
from weather_api import get_weather_data
from data_processor import process_weather_data

class AlertManager:
    def __init__(self, threshold):
        self.threshold = threshold

    def check_alert(self, temp):
        if temp > self.threshold:
            print(f"Alert! Temperature exceeded threshold: {temp}°C")

def main():
    with open("config.json") as f:
        config = json.load(f)

    api_key = config["api_key"]
    locations = config["locations"]
    interval = config["interval"]
    threshold = config["temperature_threshold"]

    alert_manager = AlertManager(threshold)

    while True:
        for city in locations:
            data = get_weather_data(city, api_key)
            temp, feels_like, weather, timestamp = process_weather_data(data)

            if temp is None:
                print(f"Skipping {city} due to missing data.")
                continue

            print(f"{city}: {temp:.2f}°C, Feels like: {feels_like:.2f}°C, Condition: {weather}")
            alert_manager.check_alert(temp)

        time.sleep(interval)

if __name__ == "__main__":
    main()
