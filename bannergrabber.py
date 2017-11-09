#!/usr/bin/env python

#this program makes a simple socket request to a target IP and port and prints out
#it's response

import socket
import sys

ip_address = raw_input("Target IP\n> ")
port = raw_input("Target port\n> ")
port = int(port)
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(2)
	s.connect((ip_address,port))
except:
	print("Service unavailable")
	exit
byte = str.encode("Server:\r\n")
s.send(byte)
banner = s.recv(1024)
print(banner)
