import sys
import socket
import time
import urllib.parse
import select

def clientConn():
	s = socket.socket()
	host = socket.gethostname()
	port = 4000
	s.bind((host, port))
	s.listen(5)
	return s
	
def sendInts(conn):
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
			
def getClientPackets(conn, buffer):
	while 1:
		ready = select.select([conn], [], [], 5)
		if ready[0]:
			d = conn.recv(4096)
			print(d)
		
		

	

buffer = bytearray()	
	
	
s = clientConn()

conn, address = s.accept()

#sendInts(conn)

getClientPackets(conn, buffer)

	
	

	

		
		
		
		
		
		



	
