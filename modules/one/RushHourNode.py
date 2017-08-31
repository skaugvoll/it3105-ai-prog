class SearchNode:
    def __init__(self, state=None, g=None, h=None, f=None, status=None, parent=None, kids=[]):
        self.state = state
        self.gValue = g
        self.hValue = h
        self.fValue = f
        self.status = status
        self.parent = parent
        self.kids = kids
        self.rank = self._createId()

    def _createId(self):
        if(self.state == None):
            self.rank = "woopsies"
        self.rank = str(self.state)
    
    def getId(self):
        return self.rank


    def __repr__(self):
        return "state: " + str(self.state) +  " g: " +  str(self.gValue) + " h: " + str(self.hValue) + " f: " + str(self.fValue)

    def getPlayerPiece(self):
        return self.state[0]

    def getstate(self):
        return self.state

    def setGValue(self, value):
        self.gValue = value

    def setHValue(self, value):
        self.hValue = value

    def getGValue(self):
        return self.gValue

    def getHValue(self):
        return self.hValue

    def getFValue(self):
        #self.fValue = self.gValue + self.hValue
        return self.fValue

    def setFValue(self):
        self.fValue = self.gValue + self.hValue

    def getKids(self):
        return self.kids

    def addKid(self, kid):
        self.kids.append(kid)

    def getCarByNumber(self, number):
        return self.state[number]

    def getState(self):
        return self.state

    def setParent(self, parent):
        self.parent = parent

