import socket

def main():
	host = '127.0.0.1'
	port = 5001

	server = ('127.0.0.1', 5000)

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	while True:
		message=raw_input("type text to send")
		if message == 'q':
			s.close()
			break
		s.sendto(message, server)
		data, addr = s.recvfrom(1024)
		print 'recived from server: %s ; data %s .' % (addr,data)

if __name__ == "__main__":
	main()
