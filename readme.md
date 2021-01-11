# Mobile Communication Network Projects

## Web Server
This project is simple mail server that can accept HTTP request packages and send response them.
It does not use httplib or another library. It uses only TCP sockets.
The server accepts only GET requests and return only index.html page.
Additionally, the project includes a client code that can send HTTP requests.
Real web servers are multithreaded programs. Each thread handle another client.
This project is upgraded to multithreaded web server too. But it is so simple.

## UDP Pinger
This project is simple pinger that can send and some packets and measuere time between sending and recieveing.
It uses UDP instead of ICMP. It has 1 second timeout value for each packet. To simulate packet loss, the server randomly drop some packets.

Another application for UDP ping is UDP heartbeat. You can monitor a remote app by using this mechanism. Client send signals peridically and
server collect this signal. If there is no signal for a while, it means client is has been stopped.

## Mail Client
This project is simple mail client that can send emails to any reciepent.
It does not use smtplib or another library. It establish a TCP connection with your mail server.
Then communicate with SMTP commands. Before you run enter your authentication information and set mail server information.
Also if any encryption method available, it starts SSL session. Most modern and popular mail servers (Gmail or Office 365) force you to use TLS.
Additionally, you can send images as attachment.