import requests
city = "Moscow,RU"
appid = "e28b205c73363402331005f77b682ed1"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)

print("Погодные условия:", data['weather'][0]['description'])
print("ветяр м/с:",data['wind']['speed'])
print("вижен (м):", data['visibility'])

print("Температура:", data['main']['temp'])

print("Минимальная температура:", data['main']['temp_min'])

print("Максимальная температура", data['main']['temp_max'])