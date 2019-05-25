#!/usr/bin/python3

import board, busio, digitalio, adafruit_bme280

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D8)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, cs)

print("Temperature: " + format(bme280.temperature, '.2f') + " C")
print("Humidity: " + format(bme280.humidity, '.2f') + " %")
print("Pressure: " + format(bme280.pressure, '.2f') + " hPa")
