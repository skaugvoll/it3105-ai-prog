
class CSPDomain():
    def __init__(self, values=[]):
        self.values = values

    def __repr__(self):
        return self.getValues()

    def setValues(self, values):
        self.values = values

    def getValues(self):
        return self.values