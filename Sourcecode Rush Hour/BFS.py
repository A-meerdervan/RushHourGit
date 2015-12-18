from CarsList import CarsList
from Car import Car
from allBords import *
import copy
import Queue
from rushhour_visualisation import *

# Initialize global variables
STATES_ARCHIVE = []
SOLUTION = []
SOLUTION_PATH = []
INITIAL_STATE = []
WIDTH = 0
EXIT = 0
CARS_LIST = CarsList()

# main is the main function, which sets the global variables, runs the algorithm,
# prints the outcome of the algorithm and runs the simulation
def main():

	# choose the bord to perform the algoritmh on (1-7)
	bordVariables = bord(1)

	# set global variables
	global WIDTH; WIDTH = bordVariables[1]
	global EXIT; EXIT = bordVariables[2]
	global CARS_LIST; CARS_LIST = bordVariables[0]
	global INITIAL_STATE; INITIAL_STATE = CARS_LIST.getFirstState()
	global STATES_ARCHIVE; STATES_ARCHIVE = dict()

	# run the Breadth First Search algorithm
	algorithm(INITIAL_STATE)

	# print the results of the algorithm
	print "Algorithm is done"
	print len(SOLUTION_PATH)

	# run the simulation of the shortest path
	runSimulation(CARS_LIST.getVisualisationList(), SOLUTION_PATH, WIDTH, WIDTH, 0.5)


# the algorithm function runs the Breadth First Search algorithm. It takes a input
# the initial state.
def algorithm(initialState):

	queue = []
	queue.append(initialState)
	statesCount = 0
	# add first state
	STATES_ARCHIVE[tuple(initialState)] = [initialState, initialState]

	# loop all possible moves
	solutionNotFound = True
	while (not (queue == []) and solutionNotFound) :

		# take the next state from the queue
		option = queue.pop(0)

		# make a list of all possible states (from the dequeued state) and
		# loop through them
		for newOption in allMoves(option):

			# check if the state is already in the archive
			if optionIsNotNew(newOption):
				continue
			# check if the state is a solution, then add it to the solutions
			elif optionIsSolution(newOption):
				print statesCount
				SOLUTION.append(newOption)
				SOLUTION.append(option)
				solutionNotFound = False

				break
			# push the state to the stack and add it to the archive
			else:
				# add the option to the queue for later evaluation
				queue.append(newOption)
				statesCount += 1
				# add the option to the states archive
				STATES_ARCHIVE[tuple(newOption)] = [newOption, option]

	# get the path from start to solution
	getSolutionPath()


# this function returns a deepcopy of the gives list
def deepCopyList(List):
	return list(List)


# this function returns the path from start to solution as a list of states
def getSolutionPath():
	path = [SOLUTION[0]]
	parent = SOLUTION[1]
	notAtRoot = True
	# find the parent of the parent until the root is reached
	while notAtRoot:
		# print "Not at root"
		#find parent state
		parentOfParrent = STATES_ARCHIVE[tuple(parent)][1] # dit is [ding zelf, zijn pap]
		# parentOfParrent = STATES_ARCHIVE.getParent(parent) # dit is [ding zelf, zijn pap]
		path.append(parent)

		if parentOfParrent == INITIAL_STATE:
			notAtRoot = False
			# print "bij de root"
		parent = parentOfParrent
	path.append(INITIAL_STATE)
	# store the path (but the path needs to be flipped)
	global SOLUTION_PATH; SOLUTION_PATH = path[::-1]


# this function checks if the given state is present in the archive
def optionIsNotNew(option):
	return tuple(option) in STATES_ARCHIVE


# this function returns a boolean based on the given state. It returns
# true if the state is a solution of the problem, i.e. if the path
# of the red car to the exit is empty.
def optionIsSolution(state):
	carIndex = 0
	tilesToExit = range(state[-1] + 2, EXIT + 2)
	# loop the cars in the state and check if they block the red car
	for mainTileNumber in state:
		for carTile in CARS_LIST.cars[carIndex].getTileNumbers(state[carIndex], WIDTH):
			# if a car is in the way, the option is not a solution
			if carTile in tilesToExit:
				return False
		carIndex += 1
	return True


# this function takes a state and returns a list with tiles, which are
# occupied by cars.
def getOccupiedTiles(state):
	occupied = []
	k = 0
	for car in CARS_LIST.cars:

		if car.isHorizontal and car.length == 2 :
			occupied.append(state[k])
			occupied.append(state[k]+1)
		elif not car.isHorizontal and car.length == 2:
			occupied.append(state[k])
			occupied.append(state[k]+WIDTH)
		# The car is 3 long and horizontal:
		elif car.isHorizontal and car.length == 3:
			occupied.append(state[k])
			occupied.append(state[k]+1)
			occupied.append(state[k]+2)
		# The car is 3 long and veritcal:
		else:
			occupied.append(state[k])
			occupied.append(state[k]+WIDTH)
			occupied.append(state[k]+WIDTH*2)
		k += 1
	return occupied


# this functions returns a list of states which are possible to make by
# moving a car one space on the gives state.
def allMoves(state):
	moveOptions = []
	i = 0
	occupied = getOccupiedTiles(state)

	for car in CARS_LIST.cars:
		bord = deepCopyList(state)
		bord2 = deepCopyList(state)

		if car.isHorizontal and car.length == 2 :
			if state[i] -1 not in occupied and state[i] not in range(0,WIDTH*WIDTH,WIDTH): # moet niet op een bezette tegel of buiten het bord belanden
				bord[i] -= 1
				moveOptions.append(bord)
			if state[i] + 2 not in occupied and state[i] not in  range(WIDTH-2,(WIDTH*WIDTH+WIDTH-2),WIDTH): # range om te kijken of de positie binnen het bereik van het bord is.
				bord2[i] += 1
				moveOptions.append(bord2)

		elif not car.isHorizontal and car.length == 2:
			if state[i] - WIDTH not in occupied  and state[i] not in  range(WIDTH):
				bord[i] -= WIDTH
				moveOptions.append(bord)
			if state[i] + 2*WIDTH not in occupied and state[i] not in range(WIDTH*(WIDTH-2),WIDTH*(WIDTH-1)):
				bord2[i] += WIDTH
				moveOptions.append(bord2)

		elif car.isHorizontal and car.length == 3:
			if state[i] - 1 not in occupied and state[i] not in  range(0,WIDTH*WIDTH,WIDTH):
				bord[i] -= 1
				moveOptions.append(bord)
			if state[i] + 3 not in occupied and state[i] not in  range(WIDTH-3,WIDTH*WIDTH+WIDTH-3,WIDTH):
				bord2[i] += 1
				moveOptions.append(bord2)

		elif not car.isHorizontal and car.length == 3:
			if state[i] - WIDTH not in occupied and state[i] not in  range(WIDTH):
				bord[i] -= WIDTH
				moveOptions.append(bord)
			if state[i] + 3*WIDTH not in occupied and state[i] not in range(WIDTH*(WIDTH-3),WIDTH*(WIDTH-2)):
				bord2[i] += WIDTH
				moveOptions.append(bord2)
		i += 1

	return moveOptions


# this make the program run when this file is opened from the command prompt
if __name__ == '__main__':
	main()
