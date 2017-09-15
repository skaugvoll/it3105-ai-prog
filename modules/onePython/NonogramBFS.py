from BFSclass import BFS

class NonogramBFS(BFS):
    def __init__(self):
        pass

    def getInitalState(self, fileWithInitState):
        try:
            initialState = open(fileWithInitState, 'r')
            for line in initialState: # for each playing piece
                line = line.replace('\n','') # remove unvalid character
                line = line.split(',') # create a list of coordinates / meta data
                line = map(lambda x: int(x), line) # change type from string to int
                state.append(tuple(line))
            # print(initialState)
            searchNode = SearchNode(state=state) # crate a state-node, with a state-tuple representing the entire state and append to state
            initialState.close()
            return searchNode
        except:
            raise Exception("Something went wrong when making inital state")
