class Storage():

	def __init__(self):
		self.__observers = []

	def add_observers(self, observer):
		self.__observers.append(observer)

	def notify_all(self, *agr, **agrs):
		for observer in self.__observers:
			observer.notify(*agr, **agrs)


class ObserverA():

	def __init__(self, storage):
		storage.add_observers(self)
		self.send_all = storage.notify_all

	def notify(self, message):
		print('A << %s' % message)


class ObserverB():

	def __init__(self, storage):
		storage.add_observers(self)

	def notify(self, message):
		print('B << %s' % message)


if __name__ == '__main__':
	storage = Storage()
	obsa = ObserverA(storage)
	obsb = ObserverB(storage)
	obsa.send_all('asd')
