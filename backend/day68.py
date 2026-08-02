import requests

def get_weather(city_name):
    # Endpoint with JSON format parameter
    url = f"https://wttr.in/{city_name}?format=j1"
    
    print(f"\n🔍 Fetching weather for '{city_name}'...")
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Accessing nested JSON values
            current = data["current_condition"][0]
            temp_c = current["temp_C"]
            feels_like_c = current["FeelsLikeC"]
            humidity = current["humidity"]
            weather_desc = current["weatherDesc"][0]["value"]
            
            print("=" * 35)
            print(f"📍 City: {city_name.capitalize()}")
            print(f"🌡️ Temperature: {temp_c}°C (Feels like {feels_like_c}°C)")
            print(f"💧 Humidity: {humidity}%")
            print(f"☁️ Condition: {weather_desc}")
            print("=" * 35)
        else:
            print(f"❌ Failed to get data. Status Code: {response.status_code}")
            
    except Exception as error:
        print(f"⚠️ An error occurred: {error}")

# Interactive CLI Loop
if __name__ == "__main__":
    print("--- 🌤️ PYTHON WEATHER APP 🌤️ ---")
    user_city = input("Enter a city name (e.g., Peshawar, London, Tokyo): ").strip()
    
    if user_city:
        get_weather(user_city)
    else:
        print("No city entered. Defaulting to Peshawar...")
        get_weather("Peshawar")