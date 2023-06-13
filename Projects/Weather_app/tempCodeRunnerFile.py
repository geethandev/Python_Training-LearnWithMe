import requests
import pprint as pp

API_KEY = "8e42fd443bf15bad56f763d3087b4bb1"  # Replace with your actual API key
# location = input("Enter the location: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=YOUR_API_KEY&q=New%20York"

response = requests.get(base_url)
raw_data = response.json()

pp.pprint(raw_data)
