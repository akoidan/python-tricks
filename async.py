import threading
import time

class AsyncWrite(threading.Thread):
	def __init__(self, text, out):
		threading.Thread.__init__(self)
		self.text = text
		self.out= out
	def run (self):
		f = open (self.out, "a")
		f.write(self.text +'\n')
		f.close()
		time.sleep(1)
		print("finished "+ self.out)
def Main():
	message = input("enter a string to store: ")
	background = AsyncWrite(message, 'out.txt')
	background.start()
	print("the program can continue to run while it writes to another thread")
	background.join()
	print ("waited until thread was complete")
Main()
