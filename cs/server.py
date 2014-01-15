import socket
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(('localhost', 8001))  
sock.listen(5)  

while True:  
	connection,address = sock.accept() 
 
        buf = connection.recv(1024)
	print "I receive:", buf 
 
        if buf == '1':  
        	connection.send('welcome to server!')  
        else: 
        	connection.send('bye')
		
	connection.close()

sock.close()  

