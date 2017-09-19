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
        elementString = self.drawString(elementArray, 0, self.numColumns)
        # all permutations # contains duplicates... (1,2) and (2,1) == duplicates.
        # print("ELEMENT STRING: " + elementString)
        # print("ELEMENT ARRAY: " + str(elementArray))
        print(elementString)

        perms = self.getAllLegalPermutations(elementString, elementArray, self.numColumns)




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

        # print("con:  " + constraint)
        # print("domain:  " + domain)

        if not eval(constraint):
            return False

        return True

    def getAllLegalPermutations(self, elementString, elementArray, rowColSize):
        numberOfShifts = len(elementString) - sum(elementArray)
        numberOfSegments = len(elementArray)

        temp = elementString

        permutations = []
        shift = 0
        if sum(elementArray) + len(elementArray) -1 == len(elementString):
            permutations.append(elementString)
        else:
            permutations.append(elementString)
            while temp.rfind(str(len(elementArray) -1)) != len(temp) -1:
                permutations = list(set(permutations + self.moveSegments(numberOfSegments, numberOfShifts, elementArray, temp))) # concatenate two lists
                shift += 1
                temp = self.drawString(elementArray, shift, rowColSize)

        # for shift in range(numberOfShifts):



            # localNumberOfShifts = numberOfShifts -1
            # localTemp = temp
            # while localTemp.rfind(str(len(elementArray)-1)) != len(temp)-1:
            #     for numSeg in range(2, len(elementArray)):
            #         move = self.moveCurrentString(numSeg, elementArray, localTemp)
            #         print("move" + move)
            #         permutations = list(set(permutations + self.moveSegments(numberOfSegments, localNumberOfShifts, elementArray, move)))  # concatenate two lists
            #         localNumberOfShifts -= 1
            #     localTemp = move
            # print("GALP temp"  + temp)
            # print("GALP len temp: " + str(len(temp)))
            # print("******* SHIFT MY BABY UP *******")
            # numberOfShifts -= 1


        print(permutations)
        print(len(permutations))

        return -1

    def moveCurrentString(self, numSeg, elementArray, elementString):
        newElementString = list(elementString)
        index = elementString.find(str(len(elementArray) - numSeg))
        newElementString.insert(int(index), "-")
        newElementString.pop(-1)
        temp = "".join(newElementString)
        return temp


    def drawString(self, elementArray, startpos, rowColSize):
        elementString = ""
        if startpos != 0:
            elementString += "-" * startpos
        for i in range(len(elementArray)):
            if (elementArray[i] == rowColSize):
                elementString = str(i) * rowColSize
            else:
                elementString += str(i) * elementArray[i]
                if len(elementString) < rowColSize:
                    elementString += "-"
            if i == len(elementArray) - 1:
                elementString += "-" * (rowColSize - len(elementString))
        print("DS elementString: " + elementString)
        print("DS len es : " + str(len(elementString)))
        return elementString


    def moveSegments(self, numberOfSegments, numberOfShifts, elementArray, elementString):
        newElementString = list(elementString)
        temp = elementString
        permutations = []

        for segment in range(numberOfSegments-1, -1, -1): # move the rightmost first, then work your way leftover.
            if(segment == len(elementArray) -1):
                shifts = len(temp) - temp.rfind(str(segment)) -1
                for s in range(shifts):
                    # finn første hendelse i strengen av segment vi er på
                    index = temp.find(str(segment))  # first occurence in the string of this segment
                    # finn størrelsen på den (er lagret i elementArray)
                    size = elementArray[segment]
                    # flytt segmentet en til høyre
                    # bytt første hendelse ut med - og ta siste hendelse index + 1 og sett segment symbol

                    newElementString[index] = "-"
                    newElementString[index + size] = str(segment)
                    temp = "".join(newElementString)
                    print("TEMP: " + str(temp))
                    # sjekk om lovelig permutasjon --> self.orderConstraint(....)
                    if self.orderConstraint(temp, elementArray):
                        # legg denne nye permutasjonen inn i permutations listen
                        permutations.append(temp)
            else:
                shifts = temp.find(str(segment+1)) - temp.rfind(str(segment)) -2
                #
                # print("Segment:  " + str(segment))
                # print("Shifts:  " + str(shifts))
                for s in range(shifts):
                    # finn første hendelse i strengen av segment vi er på
                    index = temp.find(str(segment))  # first occurence in the string of this segment
                    # finn størrelsen på den (er lagret i elementArray)
                    size = elementArray[segment]
                    # flytt segmentet en til høyre
                    # bytt første hendelse ut med - og ta siste hendelse index + 1 og sett segment symbol

                    newElementString[index] = "-"
                    newElementString[index + size] = str(segment)
                    temp = "".join(newElementString)
                    print("TEMP: " + str(temp))
                    # sjekk om lovelig permutasjon --> self.orderConstraint(....)
                    if self.orderConstraint(temp, elementArray):
                        # legg denne nye permutasjonen inn i permutations listen
                        permutations.append(temp)
            # for s in range(numberOfShifts):
            #     # finn første hendelse i strengen av segment vi er på
            #     index = temp.find(str(segment)) # first occurence in the string of this segment
            #     # finn størrelsen på den (er lagret i elementArray)
            #     size = elementArray[segment]
            #     # flytt segmentet en til høyre
            #     # bytt første hendelse ut med - og ta siste hendelse index + 1 og sett segment symbol
            #
            #     newElementString[index] = "-"
            #     newElementString[index+size] = str(segment)
            #     temp = "".join(newElementString)
            #     print("TEMP: " + str(temp))
            #     # sjekk om lovelig permutasjon --> self.orderConstraint(....)
            #     if self.orderConstraint(temp, elementArray):
            #         # legg denne nye permutasjonen inn i permutations listen
            #         permutations.append(temp)

        return permutations


def main():
    nono = NonogramBFS()
    nono.getInitalState("tasks/nono-chick.txt")
    nono.getAllRowPermutations([5, 1, 3, 2])

    # nono.getInitalState("tasks/nono-cat.txt")
    # nono.getAllRowPermutations([2, 2, 1])

    # nono.getInitalState("tasks/nono-fox.txt")
    # nono.getAllRowPermutations([1, 2, 1, 1, 1, 1, 1, 1, 2, 3])




    # nono.moveCurrentString()
    # print(nono.getAllRowPermutations([2, 2]))
    # print(nono.getAllColumnPermutations([2, 2]))
    # print(nono.orderConstraint('0-11-2-3-4-5-6-7-999--88', [1, 2, 1, 1, 1, 1, 1, 1, 2, 3]))
    # print(nono.orderConstraint('0-111', [1, 3]))
    # print(nono.drawString([3,1], 4))

main()
