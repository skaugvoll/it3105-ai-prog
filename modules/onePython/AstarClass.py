from abc import *
import time

class ASTAR(ABC):
    def __init__(self, initStateFile, algo):
        self.CLOSED = []  # visited and expanded
        self.OPEN = []  # found and to be expanded
        self.states = []  # the inital state filename.
        self.isGen = ()
        self.moves = 0
        self.startTime = None

    def getCurrentState(self):
        return self.states[-1]

    def _sortAgenda(self):
        self.OPEN = sorted(self.OPEN, key=lambda x: x.getFValue())

    def _popFromAgenda(self):
        return self.OPEN.pop(0)  # return the first element from the agenda / open list. (the node / state with lowest f-value)

    def _pushToAgenda(self, node):
        if self.algo == "DFS":
            self.OPEN.insert(0, node)
            return
        elif self.algo == "BFS":
            self.OPEN.append(node)
        else:
            self.OPEN.append(node)
            self._sortAgenda()

    def _pushToDone(self, node):
        self.CLOSED.append(node)
        self.states.append(node)

    @abstractmethod
    def _nodeIsSolution(self, node):
        pass

    def _traversePath(self, solution, node):
        if node.getParent() == None:
            return solution

        else:
            parent = node.getParent()
            solution.append(parent)
            return self._traversePath(solution, parent)

    def _getSolution(self, node):
        solution = self._traversePath([], node)
        solution.reverse()
        solution.append(node)
        # reconstruct path to goal (follow the parent of the goal state, backwords)

        print(len(self.states) - 1)  # -1 because 1 state is generated twice
        print("\n" * 5)
        print("::::: SOLUTION :::::")
        for step in solution:
            # print(step)
            self.bfs.drawBoard(step.state)
            print(step)
            print("\n" * 2)
        print("Num steps", len(solution) - 1)  # -1 because the first / inital state is not a move.
        # for step in self.CLOSED:
        #     print (step)
        return solution  # the nodes / states that generate the goal state

    '''should return the path, or failure.'''

    def solve(self):
        # do the inital work. (much is done in the initialization of Astar)
        # pop the inital state
        # initNode = self.getCurrentState()
        initNode = self.initState
        # set g value to 0,
        initNode.setGValue(0)
        # set h value to estimation.
        initNode.setHValue(self.bfs.calculateHValue(initNode, self.goalState))
        initNode.setFValue()
        # print(node)
        # push initial node to the agenda (open-list)
        self.OPEN.append(initNode)
        self.startTime = time.time()
        # Agenda loop starts here. While no solution found do:
        while len(self.OPEN):
            searchNode = self._popFromAgenda()
            self._pushToDone(searchNode)
            # print("\n"*2) #Space between boards
            # print(searchNode)
            # self.bfs.drawBoard(searchNode.getState())

            # check if the new node is the goal
            if self._nodeIsSolution(searchNode):
                return self._getSolution(searchNode)  # if solution return the path.

            # if not solution, generate all successors / children of seachNode (all possible moves) in this state. (move each piece onePython step, in both available orientation direction (left/right, or up/down))
            successors = self.bfs.generateSuccessors(searchNode)
            # for each successor do
            for kid in successors:
                # check if the successor has been created before --> check if the kid -list is in the self.states list

                self.attach_and_eval(kid, searchNode)

                if self.checkIfPrevGen(kid, self.OPEN) or self.checkIfPrevGen(kid, self.CLOSED):
                    if self.isGen[0] == self.CLOSED:
                        kid = self.CLOSED[self.isGen[1]]
                    else:
                        kid = self.OPEN[self.isGen[1]]

                # push the successor to the searchNode kids list.
                searchNode.addKid(kid)

                if not self.isGen:
                    self.attach_and_eval(kid, searchNode)
                    self._pushToAgenda(kid)
                elif (searchNode.getGValue() + self.bfs.arc_cost(searchNode, kid)) < kid.getGValue():
                    self.attach_and_eval(kid, searchNode)
                    if self.isGen == self.CLOSED:
                        self.propagate_path_improvement(kid)

                self.isGen = ()

        # if the while loop could not find a solution
        print("open is now: ", len(self.OPEN))
        print("close is now: ", len(self.CLOSED))
        print("states is now: ", len(self.states))
        return False

    def checkIfPrevGen(self, kid, l):
        if (len(l) == 0):
            return False
        for i in range(len(l)):
            node = l[i]
            if node.getId() == kid.getId():
                # kid = l[i]
                self.isGen = (l, i)
                return True
        return False

    def attach_and_eval(self, kid, node):
        kid.setParent(node)
        kid.setGValue(node.getGValue() + self.bfs.arc_cost(node, kid))
        kid.setHValue(self.bfs.calculateHValue(kid, self.goalState))
        kid.setFValue()

    def propagate_path_improvement(self, node):
        for kid in node.getKids():
            pathCost = node.getGValue() + self.bfs.arc_cost(node, kid)
            if (pathCost < kid.getGValue()):
                kid.setParent(node)
                kid.setGValue(pathCost)
                kid.setFValue()
                self.propagate_path_improvement(kid)
