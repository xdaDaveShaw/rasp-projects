import socket
from gpiozero import StatusBoard
from signal import pause

def send(name):
	TCP_IP = '192.168.0.29'
	TCP_PORT = 5005
	BUFFER_SIZE=1024

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(name)
	data = s.recv(BUFFER_SIZE)
	s.close()
def one_p():
	send("up.py")
def two_p():
	send("blink.py")
def three_p():
	send("flicker.py")
def four_p():
	send("seq.py")

sb = StatusBoard()

sb.one.button.when_pressed = one_p
sb.two.button.when_pressed = two_p
sb.three.button.when_pressed = three_p
sb.four.button.when_pressed = four_p

pause()

