from archive import StatesArchive
from CarsList import CarsList
from Stack import Stack
from Car import Car
from allBords import *
import copy
from rushhour_visualisation import *

# Initialize global variables
STATES_ARCHIVE = []
SOLUTION_PATHS = []
WIDTH = 0
CARS_LIST = CarsList()
INITIAL_STATE = []
EXIT = 0

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
	global STATES_ARCHIVE; STATES_ARCHIVE = StatesArchive()

	# run the Depth First Search algorithm
	algorithm(INITIAL_STATE)

	# print the results of the algorithm
	print "Algorithm is done"
	shortestPath = SOLUTION_PATHS[-1]
	print "amount of solutions: ", len(SOLUTION_PATHS)
	listOfLengths = []
	for path in SOLUTION_PATHS:
		listOfLengths.append(len(path))
	print "shortest found length: ", min(listOfLengths)
	print "length of dicionary: ", len(STATES_ARCHIVE.states)

	# run the simulation of the shortest path
	runSimulation(CARS_LIST.getVisualisationList(), shortestPath, WIDTH, WIDTH, 0.5)


# the algorithm function runs the Depth First Search algorithm. It takes a input
# the initial state.
def algorithm(initialState):

	stack = Stack()
	stack.push(initialState)

	# set the initial state in the archive
	STATES_ARCHIVE.setInitialState(initialState)

	# run the algoritm until the stack is empty
	while stack.isNotEmpty():

		# take the next state from the stack
		option = stack.pop();
		# make a list of all possible states (from the popped state)
		allOptions = allMoves(option)

		# this loop selects a random state from the list
		# of all possible states.
		for optionIndex in random.sample(range(0, len(allOptions)), len(allOptions)):
			newOption = allOptions[optionIndex]

			# check if the state is already in the archive
			if optionIsNotNew(newOption):
				continue
			# check if the state is a solution, then add it to the solutions
			elif optionIsSolution(newOption):
				SOLUTION_PATHS.append(STATES_ARCHIVE.getSolutionPath(newOption, option))
				return
			# push the state to the stack and add it to the archive
			else:
				stack.push(newOption)
				STATES_ARCHIVE.addState(newOption, option)


# this function returns a deepcopy of the gives list
def deepCopyList(List):
	return list(List)


# this function checks if the given state is present in the archive
def optionIsNotNew(option):
	return STATES_ARCHIVE.checkState(option)


# this function returns a boolean based on the given state. It returns
# true if the state is a solution of the problem, i.e. if the path
# of the red car to the exit is empty.
def optionIsSolution(state):
	occupied = getOccupiedTiles(state)
	arraycounter =[]
	counter = 1
	while state[-1] < EXIT:
		counter += 1
		arraycounter.append(counter)
		state[-1] += 1
	state[-1] = state[-1] - counter + 1

	for number in arraycounter:
		tileCheck = state[-1] + number
		if tileCheck in occupied:
			return False
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
			if state[i] -1 not in occupied and state[i] not in range(0,WIDTH*WIDTH,WIDTH): #een bezette tegel of buiten het bord belanden
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
