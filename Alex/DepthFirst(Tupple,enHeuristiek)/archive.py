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
        if parentDepth == 400:
            testPath = self.getSolutionPath(newOption, parentOption)
            visList = [[0, False, 2], [1, False, 2], [18, False, 2], [2, True, 2], [11, True, 2], [4, False, 2], [14, True, 3], [8, False, 2], [20, False, 2], [21, True, 2], [23, False, 3], [24, True, 2], [26, False, 3], [38, True, 3], [49, True, 2], [51, False, 2], [52, True, 2], [57, False, 3], [58, True, 2], [72, True, 3], [68, False, 2], [69, False, 2], [70, True, 2], [42, True, 2]]
            runSimulation(visList, testPath, 9, 9, 0.2) 

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
