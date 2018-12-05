"""
Disciplina: Fundamentos de Sistemas Ciber Físicos
Professor: Afonso Miguel
Projeto: EcoBlue
Alunos: Fellipe de Oliveira, Hassan Fidelis, João Pedro Rodrigues de Lima
"""

#FIRST TEST - testing dht11

#!/usr/bin/python
import Adafruit_DHT
from time import sleep
import sys

humidity, temperature = Adafruit_DHT.read_retry(11, 4)

if humidity is not None and temperature is not None:
    print("Collecting Information [...]\n")
    print("Humidity: {}" .format(humidity))
    print("Temperature: {}".format(temperature))
