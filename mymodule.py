import sys
print ('module andrew has been imported')
def main():
	print('module andrew has been called')
	print ('Number of arguments:', len(sys.argv), 'arguments.')
	print ('Argument List:', str(sys.argv))
print ('__name__ has been set to {%s} ;' %  __name__)
if __name__ == "__main__":
	main()
