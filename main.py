import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
print(weather_data.json())
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    maxm =(weather_data.json()['main']['temp_max'])
    minm=(weather_data.json()['main']['temp_min'])
    humidity= (weather_data.json()['main']['humidity'])
    speed=(weather_data.json()['wind']['speed'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")
    print(f"The maximum temperature in {user_input} is: {maxm}ºF")
    print(f"The  minimum temperature in {user_input} is: {minm}ºF")
    print(f"The humidity in {user_input} is: {humidity}")
    print(f"The wind speed in {user_input} is: {speed} mph")
