import requests

city = "Moscow,RU"
appid = "ab0d6a741273db47557acf9145d9d59b"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': 'Moscow,RU', 'units': 'metric', 'lang': 'ru',
                           'APPID': "ab0d6a741273db47557acf9145d9d59b"})
data = res.json()
print("Город:", 'Moscow,RU')
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра", data['wind']['speed'])
print("Видимость", data['visibility'])
print('\n')
#прогноз погоды на сегодня

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': 'Moscow,Ru', 'units': 'metric', 'lang': 'ru',
                           'APPID': "ab0d6a741273db47557acf9145d9d59b"})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
          '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
          i['weather'][0]['description'], ">")
    print("Скорость ветра <", i['wind']['speed'], "> \r\nВидимость <", i['visibility'], ">")
print("____________________________")
#прогноз погоды на неделю