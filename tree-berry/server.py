import SocketServer

class TcpHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data

if __name__ == "__main__":
    TCP_IP = '192.168.0.29'
    TCP_PORT = 5005

    server = SocketServer.TCPServer((TCP_IP, TCP_PORT), TcpHandler)

    server.serve_forever()
