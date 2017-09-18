from itertools import permutations
from BFSclass import BFS

class NonogramBFS(BFS):
    def __init__(self):
        self.numColumns = 0
        self.numRows = 0
        pass

    def getInitalState(self, fileWithInitState):
        try:
            initialState = open(fileWithInitState, 'r')
            lineNumber = 0
            rows = []
            columns = []
            for line in initialState:
                line = list(map(int, line.split(" "))) #map returns an iterable whitch is converted to a list
                if(lineNumber == 0):
                    self.numColumns = line[0]
                    self.numRows = line[1]
                elif(lineNumber <= self.numRows):
                    rows.append(line)
                    # self.generateNode(line, "row")
                else:
                    columns.append(line)
                    # self.generateNode(line, "column")

                lineNumber += 1
            print("Rows: " + str(rows))
            print("Columns:" + str(columns))
        except:
            raise Exception("Something went wrong when making inital state")

    def createBoard(self):
        board = None
        return board

    def drawBoard(self, state):
        self.board = self.createBoard()
        # place the pieces on a fresh board
        # print board.
        pass

    def calculateHValue(self, node, goal):
        pass

    def generateSuccessors(self, node):
        ''' Rember to check if moveing will be outside "board" (use self.boardSize) '''
        pass

    def addKid(self, node, kid):
        node.addKid(kid)

    def arc_cost(self, kid, node):
        pass

    def foundSolution(self, node, goalState):
        pass

    def generateNode(self, variable, dir):
        domain = []
        if(dir == "row"):
            domain = self.getAllRowPermutations(variable)
        else:
            domain = self.getAllColumnPermutations(variable)
        print("var = " + str(variable))
        print("dom = " + str(domain))
        print("\n")


    def getAllRowPermutations(self, elementArray):
        elementString = ""
        for i in range(len(elementArray)):
            if(elementArray[i] == self.numColumns):
                elementString = str(i) * self.numColumns
            else:
                elementString += str(i) * elementArray[i]
            if i == len(elementArray)-1:
                elementString += "-" * (self.numColumns - len(elementString))
        # all permutations # contains duplicates... (1,2) and (2,1) == duplicates.
        perms = list(set([''.join(p) for p in permutations(elementString)]))

        print("ELEMENT STRING: " + elementString)
        print("ELEMENT ARRAY: " + str(elementArray))

        # ******** VI ønsker å gjøre denne og ikke linje 81 ******** #

                                # perms = self.getAllLegalPermutations(elementString, elementArray)

        # ******** VI ønsker å gjøre denne og ikke linje 81 ********

        legalRowPerms = []
        for l in range(len(perms)):
            for k in range(len(elementArray)):
                legal = True
                if str(perms[l]).find(str(k) * int(elementArray[k])) == -1:
                    legal = False
                    break
            if(legal):
                legalRowPerms.append(perms[l])
        return legalRowPerms

    def getAllColumnPermutations(self, elementArray):
        elementString = ""
        for i in range(len(elementArray)):
            if (elementArray[i] == self.numRows):
                elementString = str(i) * self.numRows
            else:
                elementString += str(i) * elementArray[i]
            if (i == len(elementArray)-1):
                elementString += "-" * (self.numRows - len(elementString))
        # all permutations # contains duplicates... (1,2) and (2,1) == duplicates.
        perms = list(set([''.join(p) for p in permutations(elementString)]))
        legalColumnPerms = []
        for l in range(len(perms)):
            for k in range(len(elementArray)):
                legal = True
                if (str(perms[l]).find(str(k) * int(elementArray[k])) == -1):
                    legal = False
                    break
            if (legal):
                legalColumnPerms.append(perms[l])
        return legalColumnPerms


    def makefunc(self, var_names, expression, envir=globals()):
        args = ",".join(var_names)
        print("args:" + str(args))
        return eval("(lambda " + args + ":" + expression + ")", envir)


    def orderConstraint(self, domain, segments): # domain = on of the row/columns permutations || segements are the variables involved [3,1] or [3,1,1]
        numberOfSegments = len(segments)

        constraint = ""

        if numberOfSegments <= 1:
            return domain

        for i in range(numberOfSegments):
            # stuff.append(chr(97 + i))
            if i != numberOfSegments - 1 :
                constraint += "domain.rfind(" + "str(" +str(i) + "))" + " < domain.find(" + "str(" + str(i+1) + ")) - 1 and "
            else: # if last variable, you are covered by the other variables. you just need to be after them
                constraint = constraint[:len(constraint)-4]

        print("con:  " + constraint)
        print("domain:  " + domain)

        if eval(constraint):
            print("EUREKA")


    def getAllLegalPermutations(self, elementString, elementArray):
        numberOfShifts = len(elementString) - sum(elementArray)
        numberOfSegments = len(elementArray)

        temp = elementString
        permutations = []
        # for shift in range(numberOfShifts):
        # for segment in range(numberOfSegments, -1, -1): # move the rightmost first, then work your way leftover.
        # finn første hendelse i strengen av segment vi er på
        # finn størrelsen på den (er lagret i elementArray)
        # flytt segmentet en til venstre
            # bytt første hendelse ut med - og ta siste hendelse index + 1 og sett segment symbol
            # sjekk om lovelig permutasjon --> self.orderConstraint(....)
        # legg denne nye permutasjonen inn i permutations listen
        # sett denne permutasjone som temp.
        # gjør denne opperasjonen på nytt til vi har flyttet dette segmentet helt til høyre

        # når vi har flyttet ett segment helt til høyre, ta neste segment og flytt etter
        # når vi har flyttet alle segmentene helt til høyre,
        # ta utgangspunt / orginal raden, og skift alle en til høyre
        # sett den nye skiftete raden som utgangspunkt / orginal raden, utfør alle skifting for hvert segment på nytt

        # nar vi har gjort dette før alle skiftene nødvendig, har vi alle mulige og lovelige permutasjoner for raden.
        # siden vi har hatt alle segmenten på alle posisjonene de kan være uten at det bryter med rekkefølgen.
        return -1



def main():
    nono = NonogramBFS()
    nono.getInitalState("tasks/nono-cat.txt")
    # nono.getAllRowPermutations([3, 1])
    # print(nono.getAllRowPermutations([2, 2]))
    # print(nono.getAllColumnPermutations([2, 2]))
    print(nono.orderConstraint('0-11-2-3-4-5-6-7-999--88', [1, 2, 1, 1, 1, 1, 1, 1, 2, 3]))
    print(nono.orderConstraint('0-111', [1, 3]))

main()
