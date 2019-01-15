import os
import sys
import random
import subprocess

fm='sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi' 
supportedTypes=['.mp3','.wav']
tracks=list()
devnull=open(os.devnull,'w')

#mount usb
subprocess.run(fm.split(),stderr=devnull)
#get ls from usb-> all music files in list
for path,dirnames,files in os.walk('/media/usb'):
	for f in files:
		filename,extension=os.path.splitext(f)
		if extension in supportedTypes:
			tracks.append(os.path.join(path,f))

cmd=['omxplayer','-o','local','']
while(len(tracks)!=0):
	# use random for pick random music
	cmd[3]=random.choice(tracks)
	print(cmd[3])

	#call omxplayer with subprocess
	subprocess.run(cmd)

	#remove played music from list
	tracks.remove(cmd[3])
