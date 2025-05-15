"""
📄 Project 11: Weather App (GUI + API)
👨‍💻 Created by: Hashir Adnan
🌐 Website: www.techthf.xyz
🗓️ Date: [Insert today’s date]

🧠 Description:
This GUI-based weather app allows users to enter a city name and fetch real-time weather data.
It uses OpenWeatherMap API to display temperature, humidity, and weather conditions.

📦 Features:
- Tkinter-based GUI
- City input box
- Fetches weather data using an API
- Shows temperature, humidity, and condition
- Error handling for invalid cities

🧰 Tools & Modules Used:
- tkinter: for GUI interface
- requests: for API calls

💡 How to Use:
1. Get a free API key from https://openweathermap.org/api
2. Paste it into the `API_KEY` variable in the script
3. Run the script using: `python main.py`
4. Enter a city and click "Get Weather"

✅ Example:
Input: Lahore  
Output: 32°C, Clear Sky, 60% humidity
"""

import tkinter as tk
import requests

# 🔑 Replace this with your real API key from OpenWeatherMap
API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to get weather data
def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="❌ Please enter a city name.")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            result_label.config(text="❌ City not found!")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()

        result = f"🌆 {city.title()}\n🌡️ Temp: {temp}°C\n💧 Humidity: {humidity}%\n☁️ Condition: {condition}"
        result_label.config(text=result)
    except Exception as e:
        result_label.config(text="⚠️ Error fetching data.")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x300")
root.resizable(False, False)

# Widgets
title_label = tk.Label(root, text="🌤️ Weather App", font=("Arial", 16))
title_label.pack(pady=10)

city_entry = tk.Entry(root, width=25, font=("Arial", 12))
city_entry.pack(pady=5)
city_entry.focus()

get_btn = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12))
get_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
