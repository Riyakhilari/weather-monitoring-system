# weather-monitoring-system
Project Overview
The Weather Monitoring System is a Python application that fetches and monitors weather data for specified locations. It provides real-time temperature updates and alerts based on user-defined thresholds.

Installation
Clone the repository:

git clone <repository-url>
cd weather_monitoring_system

Install the required dependencies:

pip install -r requirements.txt

Set up the environment variables:

Create a .env file in the project root and add your OpenWeatherMap API key and other configurations.

API_KEY=your_api_key_here
Usage
Run the application:

python main.py

The application fetches weather data for the configured locations at the specified interval.

Configuration
The configuration file (e.g., config.json) includes settings like locations, intervals, and temperature thresholds.
Example:
json
{
  "locations": ["Delhi", "Mumbai", "Chennai"],
  "interval": 600,
  "temperature_threshold": 30
}

Design Choices
The application is built using Python, leveraging the Requests library to fetch data from the OpenWeatherMap API. The architecture follows a simple design pattern that allows easy extension and maintenance.

Dependencies
List of dependencies required to run the application:

requests==2.25.1
flask==2.0.1
python-dotenv==0.19.1

Non-Functional Requirements
Security: API keys are stored in a .env file to prevent exposure.
Performance: The application efficiently handles multiple requests using asynchronous calls.

Authored By
Riya
