from socket import *
from time import *

clientSocket = socket(AF_INET, SOCK_DGRAM)
serverAddr = ('localhost', 12000)
clientSocket.settimeout(1)


i = 1
while (i < 11):

	try:
		sendTime = time()
		message = "PING " + str(i) + " " + str(strftime("%H:%M:%S"))
		clientSocket.sendto(message.encode(), serverAddr)
		print("Sent Message: " + message)

		data, server = clientSocket.recvfrom(1024)
		print("Response Message: " + data.decode())
		responseTime = time();

		elapsed = responseTime - sendTime;
		print("RTT: ", str(elapsed) + " seconds\n")

	except timeout:
		print("Request #" + str(i) + " Time Out\n")

	i += 1

print("Closing Socket")
clientSocket.close()