#!/usr/bin/python
import optparse
def fib(n, prin):
	a, b = 0, 1
	for i in range (n):
		a,b=b,a+b
		if prin:
			print (a) 
	return a

def main():
	parser = optparse.OptionParser()#'usage %pro -n <fib_number> -o <outputfile> -a (print all)', version='%prog 1.0')
	parser.add_option('-n',dest='num',type='int',\
		help='specify then n  fibbonacci number to output')
	parser.add_option('-o',dest='out',type='string',\
		help='specify the output file (optional)')
	parser.add_option('-a','--all', dest='prin', action='store_true', default=False, \
		help='print all numbers up to n')
	(option, args)= parser.parse_args()
	if (option.num == None):
		print (parser.usage)
		exit(0)
	else:
		number=option.num	
	result =fib(number, option.prin)
	print ( "The " +str(number)+ "th fib number is "+ str(result))
	
	if (option.out != None):
		f= open(option.out, 'a')
		f.write(str(result)+'\n')
if __name__ == "__main__":
	main()
