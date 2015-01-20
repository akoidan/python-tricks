class myClass():
	def __call__(self, function):
		self.function= function	
		print('it works')
		return None
	
	@classmethod
	def __instancecheck__(self, instance):
		print ('instacheck')

	def test(self):
		print('test has been called')

class BClass(myClass):
	def lol():
		pass


class Ololo():
	pass

d = BClass()
f = Ololo()

print(isinstance(f, BClass))
