from ast import IsNot
from curses import noecho
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 21

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        with open('env.txt', 'w') as f:
            f.write(str(temperature)+"C")
            f.write("\n")
            f.write(str(humidity)+"%")
    else:
        print("error")