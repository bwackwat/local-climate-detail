#!/usr/bin/python3

import os, sys, MySQLdb, django, board, busio, digitalio, adafruit_bme280
from time import sleep
from datetime import datetime

os.environ['DJANGO_SETTINGS_MODULE'] = 'lcd.settings'
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

sleep(60)
django.setup()
from lcd.models import *

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D8)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, cs)

while True:
    location = SensorLocation.objects.filter(current=True).first()
    if location is None:
        print(str(datetime.today()) + ": No current SensorLocation selected.")
    else:
        ClimateData(
            location=location,
            temperature=bme280.temperature,
            humidity=bme280.humidity,
            pressure=bme280.pressure
        ).save()

    sleep(60)

