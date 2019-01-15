import os
import sys
import shutil
import tkinter

def copyFile(src, dst, buffer_size=10485760):
	#default buffer size= 10 MB
	with open(src, 'rb') as fsrc:
		with open(dst, 'wb') as fdst:
			shutil.copyfileobj(fsrc, fdst, buffer_size)

def copyProcess(src, dst, clear=True):
	## Clear Destination
	if clear:
		for path,dirnames,files in os.walk(dst,topdown=False):
			for f in files:
				os.remove(os.path.join(path,f))
			st=os.path.split(path)
			if(st[-1]!=''):
				os.rmdir(path)
				
	## Copy files to Destination
	for path,dirnames,files in os.walk(src,topdown=True):
		st=os.path.split(path)
		subfolder=''
		if(st[1]!=''):
			os.mkdir(os.path.join(dst,st[1]))
			subfolder=st[1]
		files.sort()
		if(subfolder==''):
			print(dst)
			prefix=''
		else:
			print(' ',subfolder,'\\',sep='')
			prefix=' '
		for f in files:
			print(prefix,'  ',f,sep='')
			copyFile(os.path.join(src,subfolder,f),os.path.join(dst,subfolder,f))
			
def buttoncallback():
	print('Files copied:\n')
	copyProcess(src.get(), dst.get())
	root.quit()
	
#Main
if(len(sys.argv)==3):
	print('Files copied:\n')
	copyProcess(sys.argv[1], sys.argv[2])
	sys.exit()
	
#GUI
root=tkinter.Tk()
root.title('Copy Music to USB Strick')
mainframe=tkinter.Frame(root)
mainframe.grid(padx=20,pady=20)

src=tkinter.StringVar()
dst=tkinter.StringVar() 
#entry
src_entry=tkinter.Entry(mainframe, width=30, textvariable=src)
src_entry.grid(column=2, row=1, columnspan=2)

dst_entry=tkinter.Entry(mainframe, width=30, textvariable=dst)
dst_entry.grid(column=2, row=2, columnspan=2, pady=10)

#label
src_label=tkinter.Label(mainframe,text='Source folder: ')
src_label.grid(column=1, row=1, sticky='E')

dst_label=tkinter.Label(mainframe,text='Destination Forlder: ')
dst_label.grid(column=1, row=2)

#button
button=tkinter.Button(mainframe, text='Start Copy', command=buttoncallback)
button.grid(column=2,row=3, pady=(10,0), sticky='W')

root.mainloop()