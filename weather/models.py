from time import time
from django.db import models

# Create your models here.


class WeatherInfo(models.Model):
    temperature = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return str(self.time) + " " + str(self.temperature)
