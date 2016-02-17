import sys
import socket
import time
import urllib.parse

def setupConn():
	s = socket.socket()
	host = socket.gethostname()
	port = 4000
	s.bind((host, port))
	s.listen(5)
	conn, address = s.accept()
	a = 0
	while 1:
		try:
			a=a+1
			b = bytes([a])
			print(a)
			conn.send(b)
			time.sleep(1)
		except KeyboardInterrupt:
			print('user exit')
			sys.exit(1)
		except ConnectionResetError:
			print('client dced')
			sys.exit(1)
	
setupConn()


	

	
	

	

		
		
		
		
		
		



	
