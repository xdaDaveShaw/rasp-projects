import socket

TCP_IP = '192.168.0.29'
TCP_PORT = 5005
BUFFER_SIZE=1024
MESSAGE= "Start"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "rcv'd", data
