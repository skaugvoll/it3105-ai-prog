from BFSclass import BFS
from NonogramVariable import NonogramVariable
import pip
from copy import deepcopy
from NonogramNode import NonogramNode

class NonogramBFS(BFS):
    def __init__(self):
        self.numColumns = 0
        self.numRows = 0
        self.rows = []
        self.columns = []
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
                    self.rows.append(NonogramVariable("row", self.numColumns, line))
                else:
                    columns.append(line)
                    self.columns.append(NonogramVariable("column", self.numRows, line))

                lineNumber += 1
            return NonogramNode([self.rows, self.columns])
        except:
            raise Exception("Something went wrong when making inital state")



    def createBoard(self):
        board = None
        return board

    def drawBoard(self, state):
        color = True

        try:
            print("trying...")
            import termcolor
            print("imported: termcolor")
        except ImportError as e:
            print("NO IMPORT...")
            # pip.main(['install', termcolor])
            color = False




        nono = state
        print("NONO:")
        print(nono)
        for row in nono[0]:
            for d in row.domain:
                s = ""
                for ch in d:
                    if (color):
                        if (ch == 0):
                            s += termcolor.colored(ch, "blue")
                        else:
                            s += termcolor.colored(ch, "white")
                    else:
                        s += str(ch)
            print(s)
        pass

    def calculateHValue(self, node, goal):
        return node.sumDomains() - 1

    def generateSuccessors(self, node):
        ''' Rember to check if moveing will be outside "board" (use self.boardSize) '''
        pass

        

    def addKid(self, node, kid):
        node.addKid(kid)

    def arc_cost(self, kid, node):
        pass

    def foundSolution(self, node, goalState):
        return node.hasFoundSolution




    # def reduceRowsAndCols(self):
    #     for row in self.rows:
    #         self.reduceDomain(row, self.columns)
    #
    #     for col in self.columns:
    #         self.reduceDomain(col, self.rows)
    #
    #
    # def reduceDomain(self, a, b):
    #     change = False
    #     for key in a.common.keys():
    #         if (b == self.columns):
    #             x = b[key]
    #         else:
    #             x = b[(len(self.rows)-1) - key]
    #         index = 0
    #         while index < len(x.domain):
    #             d = x.domain[index]
    #             # print("Dkey: " + str(d[key]))
    #             # print("aCommonKey: " + str(a.common[key]))
    #             if(b == self.rows):
    #                 l = self.columns.index(a)
    #             else:
    #                 l = (len(self.rows)-1)-self.rows.index(a)
    #             if d[l] != a.common[key]:
    #                 x.domain.remove(d)
    #                 change = True
    #             else:
    #                 index += 1
    #     return change
    #
    #
    # def findNewCommons(self):
    #     for row in self.rows:
    #         row.findCommon()
    #
    #     for col in self.columns:
    #         col.findCommon()


    # def isSolution(self):
    #     solution = True
    #     for row in self.rows:
    #         if len(row.domain) > 1:
    #             solution =  False
    #
    #     for col in self.columns:
    #         if len(col.domain) > 1:
    #             solution =  False
    #
    #     return solution
    #
    # def sumDomains(self):
    #     domainSum = 0
    #
    #     for row in self.rows:
    #         domainSum += len(row.domain)
    #     for col in self.columns:
    #         domainSum += len(col.domain)
    #     return domainSum
    #
    # def solve(self):
    #     iterate = True
    #     lastDomainSum = self.sumDomains()
    #     solution = False
    #     while iterate:
    #         self.reduceRowsAndCols()
    #
    #         self.findNewCommons()
    #         if self.isSolution():
    #             iterate = False
    #             solution = True
    #         elif lastDomainSum == self.sumDomains():
    #             iterate = False
    #
    #         lastDomainSum = self.sumDomains()
    #
    #     if(solution):
    #         self.rows.reverse()
    #         return self.rows
    #     else:
    #         print("SNAIL FUCKUP!! WOHO")



































def main():
    color = True

    try:
        print("trying...")
        import termcolor
        print("imported: termcolor")
    except ImportError as e:
        print("NO IMPORT...")
        # pip.main(['install', termcolor])
        color = False

    nono = NonogramBFS()
    nono.getInitalState("tasks/nono-telephone.txt")
    nono.solve()

    nono.rows.reverse()
    for row in nono.rows:
        for d in row.domain:
            s = ""
            for ch in d:
                if(color):
                    if (ch == 0):
                        s += termcolor.colored(ch, "blue")
                    else:
                        s += termcolor.colored(ch, "white")
                else:
                    s += str(ch)
        print(s)



    # nono.getInitalState("tasks/nono-chick.txt")
    # nono.getAllRowPermutations([5, 1, 3, 2])

    # nono.getInitalState("tasks/nono-cat.txt")
    # nono.getAllRowPermutations([3, 1])

    # nono.getInitalState("tasks/nono-fox.txt")
    # nono.getAllRowPermutations([1, 2, 1, 1, 1, 1, 1, 1, 2, 3])




    # nono.moveCurrentString()
    # print(nono.orderConstraint('0-11-2-3-4-5-6-7-999--88', [1, 2, 1, 1, 1, 1, 1, 1, 2, 3]))
    # print(nono.orderConstraint('0-111', [1, 3]))
    # print(nono.drawString([3,1], 4))

# main()