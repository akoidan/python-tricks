#!/usr/bin/python

global isCamel
isCamel = False
def camelCase(char):
	global isCamel
	print(isCamel)
	isCamel= not isCamel
	if isCamel:
		return char.upper()
	return char

lol= [ camelCase(n) for n in "hello andrew you're doing fine"]

print(''.join(lol))
