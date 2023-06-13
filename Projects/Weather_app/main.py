import requests
import tkinter as tk
from tkinter import messagebox, ttk
import pprint as pp

class WeatherApp:
    def __init__(self):
        self.API_KEY = ' '  # Replace with your actual API key
        self.weather_data = []

        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.title("Weather App")

        self.title_label = tk.Label(self.window, text="Weather App", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.location_frame = tk.Frame(self.window)
        self.location_frame.pack()

        self.location_label = tk.Label(self.location_frame, text="Location:")
        self.location_label.pack(side="left")

        self.location_entry = tk.Entry(self.location_frame, width=30)
        self.location_entry.pack(side="left")

        self.get_weather_button = tk.Button(self.window, text="Get Weather", command=self.get_weather, bg="blue", fg="white", font=("Arial", 12))
        self.get_weather_button.pack(pady=10)

        self.treeview = ttk.Treeview(self.window, columns=("Temperature", "Humidity", "Description", "Wind Speed"), height=4)
        self.treeview.heading("#0", text="Location")
        self.treeview.heading("Temperature", text="Temperature")
        self.treeview.heading("Humidity", text="Humidity")
        self.treeview.heading("Description", text="Description")
        self.treeview.heading("Wind Speed", text="Wind Speed")
        self.treeview.pack()

    def run(self):
        self.window.mainloop()

    def get_weather(self):
        location = self.location_entry.get()

        base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+self.API_KEY+"&q="+location

        response = requests.get(base_url)
        raw_data = response.json()
        
        # Printing the json responce 
        pp.pprint(raw_data)
        
        if response.status_code == 200:
            main_data = raw_data["main"]
            temperature = main_data["temp"]
            humidity = main_data["humidity"]
            weather = raw_data['weather']
            first_weather = weather[0]
            desc = first_weather['description'] 
            wind = raw_data['wind']
            speed = wind['speed']

            # Append new data to the weather data list
            self.weather_data.append((location, temperature, humidity, desc, speed))

            # Clear the table
            self.treeview.delete(*self.treeview.get_children())

            # Insert all data into the table
            for data in self.weather_data:
                self.treeview.insert("", "end", values=data)
        else:
            messagebox.showerror("Error", "Failed to fetch weather data.")

# Create an instance of the WeatherApp class
app = WeatherApp()
# Run the weather app
app.run()
