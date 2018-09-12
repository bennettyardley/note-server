from twisted.internet import task
from twisted.internet.defer import Deferred
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver


class Save(LineReceiver):
    test = b"Test Text"

    def connectionMade(self):
        self.sendLine(self.test)

    def lineReceived(self, line):
        print("receive:", line)
        if line == self.test:
            self.transport.loseConnection()

class NoteClientFactory(ClientFactory):
    protocol = Save

    def __init__(self):
        self.done = Deferred()

def main(reactor):
    factory = NoteClientFactory()
    reactor.connectTCP('localhost', 1234, factory)
    return factory.done


task.react(main)
