from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def weather_page(request):
    return render(request, 'weather.html')
