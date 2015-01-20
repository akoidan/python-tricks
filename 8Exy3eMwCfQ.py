from sys import version_info
from os import getpid
from time import sleep
from dis import dis
import builtins

def f(type1, val1, type2, val2):
	type1 = getattr(builtins, type1)
	type2 = getattr(builtins, type2)
	return type1(val1)*type2(val2)
dis(f)
#print(f('str','a','int', 3))
