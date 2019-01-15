#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

print 'Welcome to the Complete Manual Time-Lapse Tool.'

def get_param():
	while True:
		shots=raw_input('Number of Shots: ')
		interval=raw_input('Interval between shots (in seconds): ')
		if shots.isdigit() and interval.isdigit():
			aux=[int(shots),int(interval)]
			return aux
		else:
			print 'Please enter only number (int)'

def time_lapse(shots,interval):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16,GPIO.OUT)
	GPIO.output(16,GPIO.HIGH)
	taken=1

	for i in range(0,shots):
		print 'Shot %d of %d'%(taken,shots)
		GPIO.output(16,GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(16,GPIO.HIGH)
		time.sleep(interval)
		taken+=1
	GPIO.cleanup()
	print 'All shots taken sucessfully\n'
		

#Main
shots,interval=get_param()
duration=shots*interval
min=duration/60
sec=duration-min*60
print 'Shoting for %d minutes and %d seconds'%(min,sec)
while True:
	answer=raw_input('Ready to proceed?[yes/no]')
	if answer.lower() in ['yes','y']:
		time_lapse(shots,interval)
		break
	elif answer.lower() in ['no','n']:
		break
	else:
		print 'Please input your answer as yes/no'
