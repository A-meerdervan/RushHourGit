from rushhour_visualisation import *


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
        # if parentDepth == 400:
        #     testPath = self.getSolutionPath(newOption, parentOption)
        #     visList = [[0, False, 2], [1, True, 3], [4, False, 2], [5, True, 2], [7, True, 2], [11, False, 3], [12, False, 2], [17, False, 3], [18, True, 2], [22, True, 2], [27, False, 2], [45, True, 2], [48, False, 3], [44, False, 3], [30, False, 2], [59, False, 3], [32, True, 3], [63, False, 2], [73, True, 3], [50, True, 3], [69, True, 3], [37, True, 2]]
        #     runSimulation(visList, testPath, 9, 9, 0.2) 

    def getStateDepth(self, state):
        return self.states[self.listToTuple(state)][2]

    def setState(self, state, depth, parentState = []):
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
