from django.shortcuts import render
import json
import urllib.request
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q ='+city+'&appid=967da5744640200a741d7be2aff31193').read()
        list_of_data = json.loads(source)

        # data for variable list_of_data
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

