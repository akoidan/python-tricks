#!/usr/bin/python
import os
print(os.listdir('.'))

##3
print('-'*20)
try:
	myfile ='./akoidan.txt'
	with open(myfile , 'a').close():
		os.utime(myfile,None)
	f=open(myfile ,'a')
	text=f.read()
	print(text)
	f.close
except IOError:
	print('something went wrong')
