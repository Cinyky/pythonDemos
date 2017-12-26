from SocketServer import TCPServer,StreamRequestHandler

class Hanler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from',addr
        self.wfile.write('Thank you for connection StreamRequestHandler')

server = TCPServer(('',1234),Hanler)
server.serve_forever()