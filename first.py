#!/usr/bin/python
from random import randint
#months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
#for inner in  range(0,12):
#	if (daysInMonth[inner]>29):
#		print ('this is no feb')
#	else: 
#		print ('this is feb')
#	print ( '%s has %d days' % (months[inner], daysInMonth[inner]))
#loop = 1
#while loop==1:
#	login = input('enter month \n')
#	password = int(input('Enter day count\n'))
#	print ('you typed: %s , %d' % (login, password))
#	for i in range (0, len(months)):
#		if (login==months[i] and password==daysInMonth[i]):
#			print (months[i])
#			loop=0
#
#def myFunc(par1,par2):
#	print ('par1 is %s, par2 is %s' % (par1,par2))
#myFunc('a','b')
#myFunc('c','d')
#

#myList = [[1,'asdas',[1,2,3],4],['b','c'],['as','bd','ch']]
#print (myList[0][2][2])

class Dog:
	def __init__(this, *args, **kwargs):
		print (type(args))
		print (args)
	def set_name(this, n):
		this.name = n
	def set_age(self,a):
		self.age =a

	def description_of_person(self):
		print (self.name, self.age)

#andrew= Dog( 3)
#andrew.set_name('hoho')
#andrew.set_age(3)
#andrew.description_of_person()

#t= (234, 234 ,'sdfsd')
#s= [123,123,'sf']
#d= {'kuku ya 1':1, 'telephon':'t'}
#
#dict1 = {}                     # Create an empty dictionary
#dict2 = dict()                 # Create an empty dictionary 2
#dict2 = {"r": 34, "i": 56}     # Initialize to non-empty value
#dict3 = dict([("r", 34), ("i", 56)]) # Init from a list of tuples
#dict4 = dict(r=34, i=56)       # Initialize to non-empty value 3
#print (dict3)
#print ('-----------')
#dict1["temperature"] = 32      # Assign value to a key
#if "temperature" in dict1:     # Membership test of a key AKA key exists
#  del dict1["temperature"]     # Delete AKA remove
#equalbyvalue = dict2 == dict3
#print ('equal', equalbyvalue)
#itemcount2 = len(dict2)        # Length AKA size AKA item count
#print itemcount2
#isempty2 = len(dict2) == 0     # Emptiness test
#for key in dict2:              # Iterate via keys
#  print key, dict2[key]        # Print key and the associated value
#  dict2[key] += 10             # Modify-access to the key-value pair
#for value in dict2.values():   # Iterate via values
#  print value
#dict5 = {} # {x: dict2[x] + 1 for x in dict2 } # Dictionary comprehension in Python 2.7 or later
#dict6 = dict2.copy()             # A shallow copy
#dict6.update({"i": 60, "j": 30}) # Add or overwrite
#dict7 = dict2.copy()
#dict7.clear()                  # Clear AKA empty AKA erase
#print dict1, dict2, dict3, dict4, dict5, dict6, dict7, equalbyvalue, itemcount2

def a(**kwargs):
	print (type(kwargs))
	print (kwargs)

d={'asd':5,'asd':3}
a(*d)
exit()

