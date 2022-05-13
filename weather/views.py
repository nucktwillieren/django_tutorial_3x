from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import WeatherInfo
from django.core import serializers
import json

# Create your views here.


def weather_page(request):
    data = WeatherInfo.objects.all().order_by("-id")[:1].values()
    # [
    #   {"temperature": 1}, .....
    # ]
    #

    return render(request, "weather.html", context={"data": data})
