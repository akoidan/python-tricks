import runpy
import sys
sys.argv[1]='it works'
try:
	lol='yayaya'
	w = runpy.run_module('mymodule', run_name='__main__') 
	print('before exit')
	exit(0)
finally:
	print (lol)
print('shouldnt print')
#print(w)
