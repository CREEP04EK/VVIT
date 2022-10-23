import requests

city = "Moscow,RU"
appid = "e28b205c73363402331005f77b682ed1"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",

                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

data = res.json()

print("Прогноз погоды на неделю:")

for i in data['list']:
    print("Дата <", i['dt_txt'], " >\r\nТемпература <",
          '{0:+3.0f}'.format(i['main']['temp']), " >\r\nВетяр(м/с) <", i['wind']['speed'], " >\r\nВижен(м) <",
          i['visibility'], "> \r\nПогодные условия <",
          i['weather'][0]['description'], ">")

    print("____________________________")