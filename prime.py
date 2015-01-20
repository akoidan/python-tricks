#!/usr/bin/python
import sys

def main():
	#print (sorted(range(2,100),key=isNotPrime))
	tuple = range(3,    100)
	print(tuple)
	#prints sorted modulo of given numbers in range 2-100
	#first - devided by 2, then by 3, etc
def isNotPrime(num):
	for i in range (2,num-1):
		if num%i == 0:
			return i
	return 0

if __name__ == '__main__':
	main()
