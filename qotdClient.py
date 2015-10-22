#!/usr/bin/python
#Author : Brendan Lilly
#Date: 9/21/2015
#Filename: qotdClient.py
#Purpose : Connect to the QOTD Server and print a quote
#Active QOTD servers: mir.intstl.com , cygnus-x.net , djxmmx.net , alpha.mike-r.com , home.kyleterry.com


import sys
import socket  
import errno
#Default port if none are passed in via cmd line arguments 
port = 17

#Checks if the command line arguments are in the correct range
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print "Usage: " , sys.argv[0] , " <hostname> [port]"
    exit(0)
elif len(sys.argv) == 2:
	#If there are 2 cmd line arguments just get the hostname
    hostname = sys.argv[1]
    try:
		#Converts the passed hostname to an ip address and assignes it
        ipAddr=socket.gethostbyname(hostname)
    except:
        print "Invalid hostname"
        exit(0)
else:
	#If there are 3 command line arguments get the hostname and port number 
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    try:
        ipAddr=socket.gethostbyname(hostname)
    except:
        print "Invalid hostname"
        exit(0)

#Create a socket for the upcoming connection
sockfd = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
if sockfd == -1:
       print("Socket call failed.")
       exit(-1)

#Try to connect to the ip address and port specified on the newly created socket
try:   
    sockfd.connect((ipAddr,port))
except socket.error as error:
    print error
    exit(-1)

#Receive the message output by the QOTD server , max is 512 bytes
message = sockfd.recv(512)

#Output the received message
print message 

#Close the Socket connection 
sockfd.close()