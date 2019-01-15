#!/usr/bin/env python

import RPi.GPIO as GPIO

#Main
toggle=False
port=12

#setup GPIO port 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(port,GPIO.OUT)

while True:
	print ''
	if toggle:
		print  'Output port is HIGH'
	else:
		print 'Output port is LOW'
	aux=raw_input("Enter 't' to toggle ouput, 'q' to quit: ")
	if aux is 't':
		toggle=not toggle
		GPIO.output(port,toggle)

	elif aux is 'q':
		GPIO.cleanup()
		break
