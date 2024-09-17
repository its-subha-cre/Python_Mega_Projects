import requests
api_key="4e5f1dbfe280ccb6c3576630c8488dc4"
city=input("enter the name of city")
weather=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
p=weather.json()
# print(p['clouds']['all'])
print(p.keys())
print(p.values())
print(f"today's weather in {city} is {p["weather"][0]["main"]}")
print(f"today's temperature in {city} is {p['main']['temp']}")
