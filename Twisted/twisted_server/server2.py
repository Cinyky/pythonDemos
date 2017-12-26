from twisted.internet import reactor
from twisted.internet.protocol import Protocol,Factory
from twisted.protocols.basic import LineReceiver

class SimleLogger(LineReceiver):

    def connectionMade(self):
        print 'Got connection from',self.transport.client

    def connectionLost(self, reason):
        print self.transport.client,'disconnected'

    def lineReceived(self, line):
        print line


factory = Factory()
factory.protocol = SimleLogger

reactor.listenTCP(1234,factory)
reactor.run()