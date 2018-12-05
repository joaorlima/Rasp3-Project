"""
Disciplina: Fundamentos de Sistemas Ciber Físicos
Professor: Afonso Miguel
Projeto: EcoBlue
Alunos: Fellipe de Oliveira, Hassan Fidelis, João Pedro Rodrigues de Lima
"""

#THIRD TEST - dht11 + relay trigger + lamp

#!/usr/bin/python
import Adafruit_DHT
from time import sleep
import RPi.GPIO as GPIO

sensor = 4
port = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(sensor, GPIO.IN)

GPIO.setup(port, GPIO.OUT)

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, sensor)

    if humidity is not None:
        print("Humidity: {}" .format(humidity))
        print("Temperature: {}".format(temperature))

        if humidity >= 95:
            GPIO.output(port, False)

        else:
            GPIO.output(port, True)

        sleep(1)
