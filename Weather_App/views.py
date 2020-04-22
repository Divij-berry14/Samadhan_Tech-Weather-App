from django.shortcuts import render
import json
import urllib.request
import requests
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        # source=urllib.request.urlopen('api.openweathermap.org/data/2.5/forecast/daily?q={} &appid=879e979b983fe4687d564521b399ad47'.format(city))
        url='http://api.openweathermap.org/data/2.5/weather?q=us &appid=879e979b983fe4687d564521b399ad47' #current weather API
        # url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=mexico&appid=879e979b983fe4687d564521b399ad47' #5 days API
        # url='https://api.openweathermap.org/data/2.5/onecall?lat=60.99&lon=30.9&appid=879e979b983fe4687d564521b399ad47' #Onecall Api
        source=requests.get(url)
        # print(source.text)
        # source = urllib.request.urlopen(
        #     'http://api.openweathermap.org/data/2.5/weather?q='
        #     + city + '&appid = 879e979b983fe4687d564521b399ad47').read()

        # converting JSON data to a dictionary
        list_of_data = source.json()
        print(list_of_data)

        #data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                          + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "Weather_App/index.html", data)

