import SocketServer
import shlex, subprocess

cur_p = None

def hand1(name):
    global cur_p

    print "recv'd: ", name
    print "current process is: ", cur_p
    if cur_p != None:
        print "killing: ", cur_p
        cur_p.kill()
        print "killed process"

    print "starting: ", name
    cur_p = subprocess.Popen(["python", name])
    print "started: ", name

class TcpHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        hand1(self.data)

if __name__ == "__main__":

    hand1("up.py")

    TCP_IP = '192.168.0.29'
    TCP_PORT = 5005

    SocketServer.TCPServer.allow_reuse_address = True
    print "starting server..."
    server = SocketServer.TCPServer((TCP_IP, TCP_PORT), TcpHandler)

    try:
        server.serve_forever()
    finally:
        server.shutdown()
        server.server_close()
