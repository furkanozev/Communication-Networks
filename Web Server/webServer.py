#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

port = 6789

#Prepare a server socket

#Fill in start
serverSocket.bind(('', port))
print ("Server socket binded to %s" %(port))  
  
# put the socket into listening mode  
serverSocket.listen(1)   #5
print ("Server socket is listening") 
#Fill in end

while True:
	#Establish the connection
	print("Ready to serve...")
	#Fill in start
	connectionSocket, addr = serverSocket.accept()
	print("Connection address:", addr)
	#Fill in end
	
	try:
		#Fill in start
		message = connectionSocket.recv(1024)
		#Fill in end

		if not message:
			connectionSocket.close()
			continue;

		filename = message.split()[1]
		print("File name:", filename[1:])

		f = open(filename[1:])

		#Fill in start
		outputdata = f.read()
		#Fill in end

		
		#Fill in start
		#Send one HTTP header line into socket
		mes = "HTTP/1.1 200 OK\r\n\r\n " 
		connectionSocket.send(mes.encode())
		#Fill in end

		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.close()

	except IOError:
		#Send response message for file not found
		#Fill in start
		mes = "HTTP/1.1 404 Not Found\r\n\r\n"
		connectionSocket.send(mes.encode())

		mes = "<html><head><title> 404 </title></head><body><h1>404 Not Found!</h1></body></html>\r\n"
		connectionSocket.send(mes.encode())
		#Fill in end

		#Close client socket
		#Fill in start
		connectionSocket.close()
		#Fill in end

serverSocket.close()