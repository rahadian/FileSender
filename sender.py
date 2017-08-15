import socket
import sys,os
import os.path
from os import path
from pathlib import Path
#from socket import *

#s = socket(AF_INET,SOCK_STREAM)
s = socket.socket()
server_address=raw_input("Enter the Server Address: ")
server_port=raw_input("Enter the Server Port: ")
server_port=int(server_port)
print >> sys.stderr,'Connection to %s on port %s' %(server_address,server_port)
file_name1 = path.relpath('sensortest1.txt')
file1 = Path('sensortest1.txt')
file_name2 = path.relpath('sensortest2.txt')
file2 = Path('sensortest2.txt')
file_name3 = path.relpath('sensortest3.txt')
file3 = Path('sensortest3.txt')
server=(server_address,server_port)
s.connect(server)
#allThreeFail=True
if file1.exists():
	f=open(file_name1,'rb')
	print >> sys.stderr,'Sending file datasensor1 to %s ....'%server_address
	l = f.read(1024)
	while (l):
		print >> sys.stderr,'Sending...'
		s.sendall(l)
		l=f.read(1024)
	f.close()
	print >> sys.stderr,'Done sending to server %s' %server_address
	s.shutdown(socket.SHUT_WR)
	print s.recv(1024)
	s.close()
	os.remove("sensortest1.txt")
elif file2.exists():
	print "File datasensor1 not found"
	f=open(file_name2,'rb')
	print >> sys.stderr,'Sending file datasensor2 to %s ....'%server_address
	l = f.read(1024)
	while (l):
		print >> sys.stderr,'Sending...'
		s.sendall(l)
		l=f.read(1024)
	f.close()
	print >> sys.stderr,'Done sending to server %s' %server_address
	s.shutdown(socket.SHUT_WR)
	print s.recv(1024)
	s.close()
	os.remove("sensortest2.txt")
elif file3.exists():
	print "File datasensor2 not found"
	f=open(file_name3,'rb')
	print >> sys.stderr,'Sending file datasensor3 to %s ....'%server_address
	l = f.read(1024)
	while (l):
		print >> sys.stderr,'Sending...'
		s.sendall(l)
		l=f.read(1024)
	f.close()
	print >> sys.stderr,'Done sending to server %s' %server_address
	s.shutdown(socket.SHUT_WR)
	print s.recv(1024)
	s.close()
	os.remove("sensortest3.txt")
else:
	print "All Files not found"
	s.close()
	exit()
