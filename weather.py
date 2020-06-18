import requests
import json

api_key = "Your api key"
city_name = "New Delhi"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
try:
    response = requests.get(url)
    value = response.json()
    lon = value['coord']['lon']
    latitude = value['coord']['lat']
    print(f'Langitude = {lon}     Latitude = {latitude}')
    temperature = value['main']['temp']
    print(f'Temperature = {temperature}')
    pressure = value['main']['pressure']
    print(f'Pressure = {pressure}')
    humidity = value['main']['humidity']
    print(f'Humidity = {humidity}')
    speed = value['wind']['speed']
    print(f'Wind Speed = {speed}')
    weather = value['weather'][0]['description']
    print(f'Weather = {weather}')
except Exception as e:
    print(e)