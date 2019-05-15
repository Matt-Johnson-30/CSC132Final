import RPi.GPIO as GPIO
from os import system

GPIO.setmode(GPIO.BCM)
keys = [12, 20, 26]
functions = ["skip", "pause", "play"]

GPIO.setup(keys, GPIO.IN, GPIO.PUD_DOWN)
while True:
	if GPIO.input(keys[0]) == 1:
		system("curl -G -d 'song={}' -d 'function={}' 192.168.0.130:5000".format("", functions[0]))
		print functions[0]
	elif GPIO.input(keys[1]) == 1:
		system("curl -G -d 'song={}' -d 'function={}' 192.168.0.130:5000".format("", functions[1]))
		print functions[1]
	elif GPIO.input(keys[2]) == 1:
		system("curl -G -d 'song={}' -d 'function={}' 192.168.0.130:5000".format("", functions[2]))
		print functions[2]
