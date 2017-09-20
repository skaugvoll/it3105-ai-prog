

class NonogramNode:
    def __init__(self, state=None):
        self.state = state # state is a list with list of rows and columns state = [ [ rows[nonogramVar,...]] , [cols [nonogramVar,..]] ]
        self.gValue = None
        self.hValue = None
        self.fValue = None
        self.parent = None
        self.kids = []
        self.rank = self._createId()
        self.rows = self.state[0]
        self.columns = self.state[1]
        self.solve()
        self.hasFoundSolution = False


    def _createId(self):
        if self.state == None:
            self.rank = "woopsies"
        return str(self.state)

    def getId(self):
        return self.rank

    def __repr__(self):
        return "state: " + str(self.state) + " g: " + str(self.gValue) + " h: " + str(self.hValue) + " f: " + str(
            self.fValue)

    def getPlayerPiece(self):
        return self.state[0] # returns list with rows.

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

    def getParent(self):
        return self.parent


    def reduceRowsAndCols(self):
        for row in self.rows:
            self.reduceDomain(row, self.columns)

        for col in self.columns:
            self.reduceDomain(col, self.rows)


    def reduceDomain(self, a, b):
        change = False
        for key in a.common.keys():
            if (b == self.columns):
                x = b[key]
            else:
                x = b[(len(self.rows) - 1) - key]
            index = 0
            while index < len(x.domain):
                d = x.domain[index]
                # print("Dkey: " + str(d[key]))
                # print("aCommonKey: " + str(a.common[key]))
                if (b == self.rows):
                    l = self.columns.index(a)
                else:
                    l = (len(self.rows) - 1) - self.rows.index(a)
                if d[l] != a.common[key]:
                    x.domain.remove(d)
                    change = True
                else:
                    index += 1
        return change


    def findNewCommons(self):
        for row in self.rows:
            row.findCommon()

        for col in self.columns:
            col.findCommon()


    def isSolution(self):
        solution = True
        for row in self.rows:
            if len(row.domain) > 1:
                solution =  False

        for col in self.columns:
            if len(col.domain) > 1:
                solution =  False

        return solution

    def sumDomains(self):
        domainSum = 0

        for row in self.rows:
            domainSum += len(row.domain)
        for col in self.columns:
            domainSum += len(col.domain)
        return domainSum

    def solve(self):
        iterate = True
        lastDomainSum = self.sumDomains()
        self.hasFoundSolution = False
        while iterate:
            self.reduceRowsAndCols()

            self.findNewCommons()
            if self.isSolution():
                iterate = False
                self.hasFoundSolution = True
            elif lastDomainSum == self.sumDomains():
                iterate = False

            lastDomainSum = self.sumDomains()

        if(self.hasFoundSolution):
            return True
        else:
            return False


    def getSolution(self):
        return self.rows.reverse()

    def hasFoundSolution(self):
        return self.hasFoundSolution