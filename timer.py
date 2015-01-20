import threading 
import time

tLock= threading.Lock()

def timer(name, delay, repeat):
	print ("Timer: " + name + " Started")
	tLock.acquire()
	print (name+ " has aquired the lock")
	while repeat > 0:
		time.sleep(delay)
		print(name+": "+ str(time.ctime(time.time())))
		repeat -= 1
	tLock.release()
	print ("timer: " +name+ " is completed")

def main():
	t1=threading.Thread(target=timer, args=("A",1,5))
	t2=threading.Thread(target=timer, args=("B",2,4))
	t1.start()
	t2.start()

if __name__ == '__main__':
	main()
