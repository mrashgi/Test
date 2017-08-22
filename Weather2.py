import requests

url = "http://api.openweathermap.org/data/2.5/forecast"

querystring = {"APPID":"ac41628472f62d0e771dd56447e26172","q":"tehran","mode":"XML"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "deedfc51-a3d8-41b1-d014-f8b9bace46c9"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

'''qprint(response.text)'''

tehranWeather= (response.json())


print(tehranWeather["list"][0]["main"]["temp"])
