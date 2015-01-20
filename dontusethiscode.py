class Monster():

	def getnext(self):
		return 5

	def getlen(self):
		return 24

	def __iter__(self):
		for i in range(4):
			yield i


	@property
	def x(self):
		print ('defx')
		return self.koko

	@x.setter
	def x(self, value):
		if value < 0:
			raise ValueError('cannot leave the arena')
		self.koko= value

	class __metaclass__(type):
		def __instancecheck__(self, other):
			print ('helloo ololo')
			print(self, other)
	__len__ = getlen
	__next__ = getnext


#										 #
## END OF THE CLASS ##
#										 #
a = Monster()
print('lol1')
print('lol2')
print('lol3')
print('lol4')

#print(next(a))
#print (len(a))
print(isinstance('a', Monster))

#def f123():
#	yield 1
#	yield 2
#	yield 3
#	print ('lol')
#	return 4
#print(f123())
#for item in f123():
#	print( item)
