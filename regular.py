#!/usr/bin/python
import re
#string = 'my email is nightmare.quake@mail.ru . And its cool but toms email is toom@jerks.ru'
#match = re.sub(r'([\w.-]+)@([\w.-]+)',r'\1SOBAKA\2', string )
#if match:
#	print (match)
#else : print ('nothing')
email='nightmare.quake@@smail.ru'
pat=r'^[\w.]+\@[\w.]+$' 
res= re.search(pat,email) 
if res:
	print('this is email')

