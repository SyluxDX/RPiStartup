#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

#Main
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
GPIO.output(16,GPIO.HIGH)

while True:
	aux=raw_input('\nPress s to take a shot, q to quit: ')
	if aux is 's':
		GPIO.output(16,GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(16,GPIO.HIGH)
	elif aux is 'q':
		GPIO.cleanup()
		break
