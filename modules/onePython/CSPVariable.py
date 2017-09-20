from CSPDomain import CSPDomain

class CSPVariable():
    def __init__(self, name, domain=CSPDomain()):
        self.name = name
        self.domain = domain

    def __repr__(self):
        return self.name + "\nDomain: " + self.domain

    def getDomain(self):
        return self.domain

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def setDomain(self, domain):
        self.domain = domain