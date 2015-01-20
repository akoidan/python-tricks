#!/usr/bin/python
import subprocess
dict1 = {}
print (stdout)
#process =   subprocess.Popen (['ls', '-a'],stdout=subprocess.PIPE)
#output = process.communicate()
#print(output[0])
dict1['a']= 'this is a'
dict1['c']= 3434343
dict1['b']= 'this is motherfuckign b'
val1=dict1.get('i')
val2='None'
if val1 == val2 :
	print ('lol')
for key in sorted(dict1):
	print(dict1[key])
#a= 'heres output with key %(c)d and value %(a)s' % dict1
del dict1['c']
print (dict1)

list = [12,23,234,54]
del list[-2:]
print (list)
