from django.db import models
from django.utils.timezone import now


class SensorLocation(models.Model):
    created = models.DateTimeField(default=now)
    description = models.CharField(max_length=50)
    current = models.BooleanField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.description + (" (current)" if self.current else "")


class ClimateData(models.Model):
    date = models.DateTimeField(default=now)
    location = models.ForeignKey(SensorLocation, on_delete=models.CASCADE, related_name='data')
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()

    def __str__(self):
        return str(self.temperature) + "C, " + str(self.humidity) + "%, " + str(self.pressure) + "hPa (" + str(self.date) + ")"
