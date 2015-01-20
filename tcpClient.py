import socket
def main():
	host='127.0.0.1'
	port =37656
	s= socket.socket()
	s.connect((host,port))
	print('entering true loop')
	while True:	
		message = input ('type message to send: ')
		if message=='q':
			s.close()
			break
		s.send(message.encode('utf-8'))
		data=s.recv(1024)
		print ('received from server: '+data)

if __name__ == "__main__":
	main()
