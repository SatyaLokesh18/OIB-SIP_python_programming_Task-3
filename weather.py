import requests

def get_weather_info(location, api_key):
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # You can adjust units as needed, e.g., metric, imperial
    }
    response = requests.get(weather_url, params=parameters)
    weather_data = response.json()
    return weather_data

def display_weather_info(weather_data):
    if "main" in weather_data and "weather" in weather_data:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        conditions = weather_data["weather"][0]["description"]
        print(f"Weather in {weather_data['name']} - Temperature: {temperature}°C, Humidity: {humidity}%, Conditions: {conditions}")
    else:
        print("Location not found or data unavailable.")

def run_weather_app():
    """
    Main function to run the weather app.
    """
    print("Weather Information")

    # Obtain user input for location
    user_location = input("Enter a city or ZIP code: ")

    # You need to replace your API key
    api_key = "4tgw478gb4g87qe"

    # Fetch weather data
    weather_info = get_weather_info(user_location, api_key)

    # Display weather information
    display_weather_info(weather_info)

if __name__ == "__main__":
    run_weather_app()
