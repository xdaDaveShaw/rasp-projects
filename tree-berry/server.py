import SocketServer
import shlex, subprocess

cur_p = None

class TcpHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        self.hand1()

    def hand1(self):
        global cur_p
        
        print "recv'd: ", self.data
        print "current process is: ", cur_p
        if cur_p != None:
            print "killing: ", cur_p
            cur_p.kill()
            print "killed current process"

        print "starting: ", self.data
        cur_p = subprocess.Popen(["python", self.data])

        print "started: ", self.data

if __name__ == "__main__":
    TCP_IP = '192.168.0.29'
    TCP_PORT = 5005

    SocketServer.TCPServer.allow_reuse_address = True
    print "starting server..."
    server = SocketServer.TCPServer((TCP_IP, TCP_PORT), TcpHandler)

    try:
        server.serve_forever()
        print "started server."
    finally:
        server.shutdown()
        server.server_close()
