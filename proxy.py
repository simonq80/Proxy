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
	s.listen(1)
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
			
def passTo(conn, buffer):
	while 1:
		try:
			ready = select.select([conn], [], [])
			if ready[0]:
				d = conn.recv(4096)
				
				data = d.split()
				try:
					url = data[1]
					temp = url.decode().split(':', 1)
					sHost = temp[0]
					sPort = temp[1]
					print(sHost)
					print(sPort)
					serverData = serverConn(sHost, sPort, d)
					print(serverData)
					conn.send(serverData)
				except IndexError:
					a = 1
				conn.send(d)
		except KeyboardInterrupt:
			print('user exit')
			sys.exit(1)
		
		
def serverConn(host, port, data):
	s = socket.socket()
	#s.bind((socket.gethostname(), 4001))
	s.connect((host, int(port)))
	s.send(data)
	return s.recv(1000000)
	
	

buffer = bytearray()	
	
	
s = clientConn()

conn, address = s.accept()

#sendInts(conn)

passTo(conn, buffer)
conn.close()
	
	

	

		
		
		
		
		
		



	
