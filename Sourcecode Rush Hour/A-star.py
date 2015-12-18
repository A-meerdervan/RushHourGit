from archive import StatesArchive
from CarsList import CarsList
from Car import Car
from allBords import *
import random
import copy
from rushhour_visualisation import *
import Queue

# Initialize global variables
STATES_ARCHIVE = []
SOLUTION_PATHS = []
CARS_LIST = CarsList()
INITIAL_STATE = []

# main is the main function, which sets the global variables, runs the algorithm,
# prints the outcome of the algorithm and runs the simulation
def main():

	# choose the bord to perform the algoritmh on (1-7)
	bordVariables = bord(1)

	# set global variables
	global WIDTH; WIDTH = bordVariables[1]
	global EXIT; EXIT = bordVariables[2]
	global CARS_LIST; CARS_LIST = bordVariables[0]
	global CARS_LIST_LENGHT; CARS_LIST_LENGHT = len(CARS_LIST.cars)
	global INITIAL_STATE; INITIAL_STATE = CARS_LIST.getFirstState()
	global STATES_ARCHIVE; STATES_ARCHIVE = StatesArchive()

	# run the A star algorithm
	algorithm(INITIAL_STATE)

	# print the results of the algorithm
	print "Algorithm is done"
	shortestPath = SOLUTION_PATHS[-1]

	# run the simulation of the shortest path
	runSimulation(CARS_LIST.getVisualisationList(), shortestPath, WIDTH, WIDTH, 0.5)


# the algorithm function runs the A star algorithm. It takes a input
# the initial state.
def algorithm(initialState):

	priorityQueue = Queue.PriorityQueue()
	priorityQueue.put((1, initialState))

	# set the initial state in the archive
	STATES_ARCHIVE.setInitialState(initialState)

	# set variables to count the generated states
	statesCount = 0
	statesGen = 0

	# run the algoritm until the queue is empty
	while not priorityQueue.empty():

		# get the first item of the queue
		option = priorityQueue.get();
		# get only the state and cut the priority
		option = option[1]

		# make a list of all possible states (from the dequeued state)
		allOptions = allMoves(option)
		# update the counter of the states generated
		statesGen += len(allOptions)

		# this loop selects a random state from the list
		# of all possible states.
		for optionIndex in random.sample(range(0, len(allOptions)), len(allOptions)):
			newOption = allOptions[optionIndex]

			# check if the state is already in the archive
			if optionIsNotNew(newOption):
				continue
			# check if the state is a solution, then add it to the solutions
			# and print the state values
			elif optionIsSolution(newOption):
				print statesCount
				print statesGen
				SOLUTION_PATHS.append(STATES_ARCHIVE.getSolutionPath(newOption, option))
				return
			# enqueue the state to the priorityQueue and add it to the archive
			else:
				priorityQueue.put((getPriority(newOption, option), newOption))
				STATES_ARCHIVE.addState(newOption, option)

				# print the state values once per 10000 states generated
				if statesCount%10000 == 0:
					print "st added: ", statesCount
					print "st gen:	", statesGen
				statesCount += 1


# this function takes the state and its previous state and returns a
# priorityvalue of the state, based on depth of the state and car movement
def getPriority(newOption, option):
	priority = 0
	priority += numberOfCarsBlocking(newOption)

	if newOption[-1] > option[-1]:
		return priority + STATES_ARCHIVE.states[listToTuple(option)][2] + 1
	elif newOption[-1] == option[-1]:
		# Check the parent state's depth
		return priority + STATES_ARCHIVE.states[listToTuple(option)][2] + 1 + 20
		# if the car moves to the left, the score is one extra
	else:
		return priority + STATES_ARCHIVE.states[listToTuple(option)][2] +  2 + 20 # + 2


# this function takes a state an counts the number of cars blocking the red car.
def numberOfCarsBlocking(state):
	# Create an empty field
	blockingCars = 0
	carIndex = 0
	tilesToExit = range(state[-1] + 2, EXIT + 2)
	# loop the cars in the state and check if they block the red car
	for mainTileNumber in state:
		for carTile in CARS_LIST.cars[carIndex].getTileNumbers(state[carIndex], WIDTH):
			if carTile in tilesToExit:
				blockingCars += 1
		carIndex += 1
	return blockingCars


# this function returns a deepcopy of the gives list
def deepCopyList(list):
	copiedList = []
	copiedList = list[::]
	return copiedList


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


# this function takes a list and converts it to a tuple. Later in the project,
# we found out that this is easily done in python by: tuple(list)...
def listToTuple(inputList):
	newTuple = ()
	for item in inputList:
		newTuple += (item,)
	return newTuple


# this make the program run when this file is opened from the command prompt
if __name__ == '__main__':
	main()
