import sys
import socket
import urllib.parse
import select

def setupClient():
	s = socket.socket()
	host = socket.gethostname()
	port = 4000
	s.connect((host, port))
	while 1:
		try:
			ready = select.select([s], [], [], 5)
			if ready[0]:
				x = s.recv(1024)
				y = int.from_bytes(x, byteorder='big')
				print(y)
		except KeyboardInterrupt:
			print('user exit')
			sys.exit(1)
		except ConnectionResetError:
			print('server dced')
			sys.exit(1)
	s.close

	
setupClient()