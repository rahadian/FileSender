import sys,os,mmap
from socket import *
s = socket(AF_INET,SOCK_STREAM)
server_address=raw_input("Enter the Server Address: ")
server_port=raw_input("Enter the Server Port: ")
server_port=int(server_port)
print >> sys.stderr,'Building up server %s on port %s' %(server_address,server_port)
server=(server_address,server_port)
f = open('datasensor.txt','wb')
s.bind(server)
s.listen(5)
while True:
	conn,client_address = s.accept()
	print >> sys.stderr,'waiting connection from  client ... '
	print >> sys.stderr,'connection from client ', client_address
	print >> sys.stderr,'Receiving data ...'
	data=conn.recv(1024)
	while (data):
		print >> sys.stderr,'Receiving data from ',client_address
		f.write(data)
		data=conn.recv(1024)
	f.close()
	print >> sys.stderr,'Data Received Successfully'
	conn.close()
	print "Renamed ..."
	z = open('datasensor.txt','r')
	x = mmap.mmap(z.fileno(), 0, access=mmap.ACCESS_READ)
	#for line in z:
     	if x.find("sensor kelembapan")!=-1:
        	print "Sensor kelembapan"
		os.rename("datasensor.txt","sensortest1.txt")
      		print "File renamed"
	elif x.find("sensor cahaya")!=-1:
		print "Sensor cahaya"
		os.rename("datasensor.txt","sensortest2.txt")
		print "File renamed"
	elif x.find("sensor WLC")!=-1:
  		print "Sensor WLC"
		os.rename("datasensor.txt","sensortest3.txt")
 		print "File renamed"
	else:
		print "Not Found"
	break



