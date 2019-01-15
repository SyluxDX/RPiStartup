#!/usr/bin/env python
import sys
import time
import RPi.GPIO as GPIO

print 'Welcome to the Bulb Timer Tool.'

def progress_bar(value,bar_length=20):
    aux=value/100.0
    h='='*int(round(aux*bar_length))
    s=' '*(bar_length-len(h))
    line='\r['+h+s+']'
    sys.stdout.write(line)
    sys.stdout.flush()

def bulb_timer(timer):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16,GPIO.OUT)
	GPIO.output(16,GPIO.HIGH)
	interval=timer/100.0

	GPIO.output(16,GPIO.LOW)
	for k in range(100):
		progress_bar(k)
		time.sleep(interval)
	GPIO.output(16,GPIO.HIGH)
	GPIO.cleanup()
	print '\nShot taken sucessfully\n'
		

def get_time():
	while True:
		timer=raw_input('Duration of bulb shot (sec): ')
		if timer.isdigit():
			answer=raw_input('Ready to proceed?[y/n]')
			if answer.lower() in ['yes','y']:
				return int(timer)
			if answer.lower() in ['quit','q']:
				sys.exit()
		elif timer.lower() in ['quit','q','exit']:
			sys.exit()
		else:
			print 'Please enter only number (int)'
#Main
while True:
	timer=get_time()
	bulb_timer(timer)
	print 'Enter q/quit to exit'
