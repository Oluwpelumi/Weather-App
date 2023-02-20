from django.shortcuts import redirect, render
import requests
from weather.forms import CityForm
from .models import City


# Create your views here.


def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=81524cc6dab2c5e2d66442d26a0e34ce'

    cities = City.objects.all()

    if request.method =='POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_list = []

    for city in cities:

        x = requests.get(url.format(city)).json()

        # print(x)

        weather = {
            'city': city,
            'description': x['weather'][0]['description'],
            'temp': (((x['main']['temp']) - 32)*5)/9,
            'icon': x['weather'][0]['icon'],
            'humidity': x['main']['humidity'],
            'country': x['sys']['country'],
        }

        weather_list.append(weather)

    context = {'weather_list': weather_list, 'form': form}

    return render(request, 'index.html', context)



def deletecity(request, name):
    city = City.objects.filter(name=name)
    city.delete();
    return redirect('/')