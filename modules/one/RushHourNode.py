class SearchNode:
    def __init__(self, state=None, g=None, h=None, f=None, status=None, parent=None, kids=[]):
        self.state = state
        self.gValue = g
        self.hValue = h
        self.fValue = f
        self.status = status
        self.parent = parent
        self.kids = kids

    def __repr__(self):
        return "state: " + str(self.state) +  " g: " +  str(self.gValue) + " h: " + str(self.hValue) + " f: " + str(self.fValue)

    def getPlayerPiece(self):
        return self.state[0]

    def setGValue(self, value):
        self.gValue = value

    def setHValue(self, value):
        self.hValue = value

    def getHValue(self):
        return self.hValue

    def getFValue(self):
        self.fValue = self.gValue + self.hValue
        return self.fValue

    def getKids(self):
        return self.kids

    def getCarByNumber(self, number):
        return self.state[number]

    def getState(self):
        return self.state
