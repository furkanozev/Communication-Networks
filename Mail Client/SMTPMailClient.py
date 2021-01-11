from socket import *
from base64 import *
import ssl

port = 587
username = "networkdeneme00@gmail.com"
password = "Deneme123."

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

#Choose a mail server (e.g. Googlemailserver) and call it mailserver
#Fill in start
mailserver = ("smtp.gmail.com", port)
#Fill in end
#Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
#Fill in end

recv = clientSocket.recv(1024)
print(recv)

if (recv[:3] != '220'):
	print('220 reply not received from server.')


#Send HELO command and print server response.
heloCommand = 'EHLO smtp.gmail.com\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print(recv1)
if (recv1[:3] != '250'):
	print('250 reply not received from server.')


TLSCommand = "STARTTLS\r\n"
clientSocket.send(TLSCommand.encode())
recv2 = clientSocket.recv(1024)
print(recv2)
if (recv2[:3] != '220'):
	print('220 reply not received from server.')


clientSocket = ssl.wrap_socket(clientSocket)


#Send AUTH command and print server response.
#AUTH with base64 encoded user name password
clientSocket.send("AUTH LOGIN " + b64encode(username.encode()) + "\r\n")
recv3 = clientSocket.recv(1024)
print(recv3)
if (recv3[:3] != "334"):
	print('334 reply not received from server.')


clientSocket.send(b64encode(password.encode()) + "\r\n")
recv4 = clientSocket.recv(1024)
print(recv4)
if (recv4[:3] != "235"):
	print('235 reply not received from server.')


#Send MAIL FROM command and print server response.
#Fill in start
mailFrom = "MAIL FROM: <networkdeneme00@gmail.com>\r\n"
clientSocket.send(mailFrom.encode())
recv5 = clientSocket.recv(1024)
print(recv5)
if (recv5[:3] != '250'):
	print('250 reply not received from server.')
#Fill in end


#Send RCPT TO command and print server response.
#Fill in start
rcptToCommand = "RCPT TO: <networkdeneme01@gmail.com>\r\n"
clientSocket.send(rcptToCommand.encode())
recv6 = clientSocket.recv(1024)
print(recv6)
if (recv6[:3] != '250'):
	print('250 reply not received from server.')
#Fill in end


#Send DATA command and print server response. 
#Fill in start
dataCommand = "Data\r\n"
clientSocket.send(dataCommand.encode())
recv7 = clientSocket.recv(1024)
print(recv7)
if (recv7[:3] != '354'):
	print('354 reply not received from server.')
#Fill in end


#Send message data.
#Fill in start
message = "SUBJECT: SMTP Mail Client Test\nSMTP Mail Client Test Content" + msg + endmsg
clientSocket.send(message.encode())
recv8 = clientSocket.recv(1024)
print(recv8)
if (recv8[:3] != '250'):
	print('250 reply not received from server.')
#Fill in end

# Send QUIT command and get server response.
Quit = "Quit\r\n"
print(Quit)
clientSocket.send(Quit.encode())
recv9 = clientSocket.recv(1024)
print(recv9)
if (recv9[:3] != '221'):
	print('221 reply not received from server.')

print("Mail Sent")

clientSocket.close()