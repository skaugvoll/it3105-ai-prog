import sys
# from RushHourNode import SearchNode
from RushHourBFS import RushHourBFS

# commandline parameters: initalStateFile, goalState, boardSize,
class Astar:
    def __init__(self):
        self.bfs = RushHourBFS(6) # should be a sys arg.
        self.CLOSED = [] # visited and expanded
        self.OPEN = [] # found and to be expandedi
        self.states = [self.bfs.getInitalState(sys.argv[1])] # the inital state filename.
        self.goalState = (5,2) # sys.argv[2]
        self.bfs.drawBoard(self.states)
        self.isGen = False

    def getCurrentState(self):
        return self.states[-1]

    def _sortBasedOnFValue(self, nodeX, nodeY):
        return nodeX.getFValue() - nodeY.getFValue()

    def _sortAgenda(self):
        self.OPEN.sort(self._sortBasedOnFValue(x,y))

    def _popFromAgenda(self):
        return self.OPEN.pop(0) # return the first element from the agenda / open list. (the node / state with lowest f-value)

    def _pushToAgenda(self, node):
        self.OPEN.append(node)
        self._sortAgenda()
        # where we should use insertion sort, should speed up the process,
        # instead of sorting the whole list, every time. or possibly a binary seach, since its going to be "sorted"

    def _pushToDone(self, node):
        self.CLOSED.append(node)

    def _nodeIsSolution(self, node):
        car = node.getPlayerPiece()
        ## for our specific problem, check if right side of playing - car is on goal state
        # if the playing piece is on same row as goal and the right side of the car is on the same column as the goal
        if(self.goalState[1] == car[2] and (car[1] + (car[-1] - 1) == self.goalState[1])):
            return True # we found a solution!
        # if not solution
        return False

    def _getSolution(self, node):
        pass ## reconstruct path to goal (follow the parent of the goal state, backwords)


    '''should return the path, or failure.'''
    def solve(self):
        # do the inital work. (much is done in the initialization of Astar)
        # pop the inital state
        node = self.getCurrentState()
        # set g value to 0,
        node.setGValue(0)
        # set h value to estimation.
        node.setHValue(self.bfs.calculateHValue(node, self.goalState))
        print(node)
        #push initial node to the agenda (open-list)
        self.OPEN.append(node)
        #Agenda loop starts here. While no solution found do:
        while(len(self.OPEN)):
            searchNode = self._popFromAgenda()
            self._pushToDone(searchNode)
            # check if the new node is the goal
            if(self._nodeIsSolution(searchNode)):
                return self._getSolution(searchNode) # if solution return the path.

            # if not solution, generate all successors / children of seachNode (all possible moves) in this state. (move each piece one step, in both available orientation direction (left/right, or up/down))
            successors = self.bfs.generateSuccessors(searchNode)
                # for each successor do
            for kid in successors:
                pass
                # check if the successor has been created before --> check if the kid -list is in the self.states list

                kid = self.checkIfPreGen(kid, self.OPEN)
                kid = self.checkIfPreGen(kid, self.CLOSED)
                # push the successor to the searchNode kids list.
                self.bfs.addKid(node, kid)
                if not(self.isGen):
                    self.attach_and_eval(kid, node)
                    self._pushToAgenda(kid)
                elif((node.getGValue() + self.bfs.arc_cost(node, kid)) < (kid.getGValue)):
                    self.attach_and_eval(kid, node)
                    if(self.isGen == self.CLOSED):
                        self.propagate_path_improvement(kid)

                self.isGen = False

        # if the while loop could not find a solution
        return False

    def checkIfPrevGen(self, kid, l): 
        for i in range(len(l)):
            node = l[i]
            if (node.getId() == kid.getId()):
                kid = l.pop(i)
                self.isGen = l
        return kid

    def attach_and_eval(self, kid, node):
        kid.setParent(node)
        kid.setGValue(node.getGValue() + self.bfs.arc_cost(node, kid)) #Lag arc_cost i bfs
        kid.setHValue(self.bfs.calculateHValue(kid, self.goalState))
        kid.setFValue()

    def propagate_path_improvement(self, kid):
        pass


def main():
    algo = Astar()
    # algo.getCurrentState()
    algo.solve()

main()
