#!/usr/bin/env python
import time
import sys

def progress_bar(value,bar_length=20):
	aux=value/100.0
	h='='*int(round(aux*bar_length))
	s=' '*(bar_length-len(h))
	line='\r['+h+s+']'
	sys.stdout.write(line)
	sys.stdout.flush()

#Main
timer=raw_input('time: ')

aux=int(timer)/100.0

for k in range(100):
	progress_bar(k)
	time.sleep(aux)

print ''
