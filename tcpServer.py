#!/usr/bin/python
import socket
import time

def main():
	host = '127.0.0.1'
	port=37656
	s=socket.socket()
	print ('a socket has been created')
	s.bind((host, port))
	print ('just binded the socket')
	s.listen(1)
	print ('listening to socket')
	c, addr= s.accept()
	print ("connection from: ", str(addr))
	while True:
		data = c.recv(1024)
		if not data:
			break
		print ('from connected user: '+ str(data))
		data= str(data).upper()
		c.send('it works'.encode('utf-8'))
	c.close()

if __name__ == "__main__":
	main()
