from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

class Save(Protocol):
    def receivedSaveText(self, saveText):
        self.transport.write(saveText)


def ():
    f = Factory()
    f.protocol = Save
    reactor.listenTCP(1234, f)
    reactor.run()


main()
