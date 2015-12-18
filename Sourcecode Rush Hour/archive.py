# the StatesArchive class stores all the visited states. It contains functions
# to add states to the archive, check if certain states are in it, and to
# get the path from the beginstate to the solution as a list of states.
class StatesArchive(object):
    def __init__(self):
        self.states = {}

    def setInitialState(self, initialState):
        self.states[self.listToTuple(initialState)] = [initialState, initialState, 0]

    def listToTuple(self, inputList):
    	newTuple = ()
    	for item in inputList:
    		newTuple += (item,)
    	return newTuple

    def checkState(self, option):
    	optionTuple = self.listToTuple(option)
        return (optionTuple in self.states)

    def addState(self, newOption, parentOption):
    	newOptionTuple = self.listToTuple(newOption)
        parentDepth = self.states[self.listToTuple(parentOption)][2]
        self.states[newOptionTuple] = [newOption, parentOption, (parentDepth + 1)]

    def getStateDepth(self, state):
        return self.states[self.listToTuple(state)][2]

    def setStates(self, state, depth, parentState = []):
        stateTuple = self.listToTuple(state)
        self.states[stateTuple][2] = depth
        if parentState != []:
            self.states[stateTuple][1] = parentState

    def getSolutionPath(self, solution, parentSolution):
        solutionList = [solution]
        state = parentSolution
        parentState = self.states[self.listToTuple(state)][1]
        while state != parentState:
            solutionList.append(state)
            state = parentState
            parentState = self.states[self.listToTuple(state)][1]
        solutionList.append(state)
        return solutionList[::-1]
