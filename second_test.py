"""
Disciplina: Fundamentos de Sistemas Ciber Físicos
Professor: Afonso Miguel
Projeto: EcoBlue
Alunos: Fellipe de Oliveira, Hassan Fidelis, João Pedro Rodrigues de Lima
"""

#SECOND TEST - dht11 humidity and temperature levels

#!/usr/bin/python
import Adafruit_DHT
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    if humidity is not None and temperature is not None:
        print("Humidity (relative) {}" .format(humidity))
        print("Temperature (celsius) {}" .format(temperature))

        print("Collecting information [...]\n")

        sleep(2)

    else:
        print("ERROR %d" % result.error_code)
        print("Try Again!")