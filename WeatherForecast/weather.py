import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # To get temperature in Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            condition = data['weather'][0]['description'].title()

            print(f"\nWeather Report for {city_name.title()}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {condition}")

        else:
            print(f"Error: {data.get('message', 'Unable to fetch weather data')}")
    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    print("=== Simple Weather App ===")
    city = input("Enter city name: ").strip()
    api_key = "863649b222c87361bbdd0d520918add1"
    
    if city:
        get_weather(city, api_key)
    else:
        print("City name cannot be empty.")
