#!/usr/bin/python3

import board
import busio
import digitalio
import adafruit_bme280

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D8)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, cs)

print("Temperature: %0.1f C" % bme280.temperature)
print("Humidity: %0.1f %%" % bme280.humidity)
print("Pressure: %0.1f hPa" % bme280.pressure)

