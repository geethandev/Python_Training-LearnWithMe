import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = ' '  # Replace with your actual API key

def Get_Weather():
    location = location_entry.get()

    base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+location

    response = requests.get(base_url)
    raw_data = response.json()

    if response.status_code == 200:
        main_data = raw_data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        weather = raw_data['weather']
        first_weather = weather[0]
        desc = first_weather['description'] 
        wind = raw_data['wind']
        speed = wind['speed']
        
        messagebox.showinfo("Weather Info", f"Location: {location}\nTemperature: {temperature}\nHumidity: {humidity}\nDescription: {desc}\nWind Speed: {speed}")
    else:
        messagebox.showerror("Error", "Failed to fetch weather data.")

window = tk.Tk()
window.title("Weather App")

location_label = tk.Label(window, text="Location:")
location_label.pack()

location_entry = tk.Entry(window)
location_entry.pack()

get_weather_button = tk.Button(window, text="Get Weather", command=Get_Weather)
get_weather_button.pack()

window.mainloop()
