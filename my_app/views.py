from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a334fa138d5a48f041584f3b0cc1f7dd'    
    city = "HOSHIARPUR"

    r = requests.get(url.format(city))
    print(r.text)
    return render(request, 'base.html')
