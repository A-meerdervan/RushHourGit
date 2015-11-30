
from CarsList import CarsList
from tree import Tree
from Car import Car
from allBords import *
import copy
import Queue
from rushhour_visualisation import *
# this contains the state and it's parent state like:
# [state, parentState]
STATES_ARCHIVE = []
# this contains the solution state and it's parent state like:
# [state, parentState]
SOLUTION = []
# This contains the path to the solution backwards.
SOLUTION_PATH = []
INITIAL_STATE = []
WIDTH = 0
EXIT = 0
CARS_LIST = CarsList()


def main():
	bordVariables = bord(3) # return [carsList,width,exit]
	global WIDTH; WIDTH = bordVariables[1]
	global EXIT; EXIT = bordVariables[2]
	global CARS_LIST; CARS_LIST = bordVariables[0]
	global INITIAL_STATE; INITIAL_STATE = CARS_LIST.getFirstState()
	global STATES_ARCHIVE; STATES_ARCHIVE = Tree(WIDTH, CARS_LIST.getDirectionsList())
	algorithm(INITIAL_STATE)
<<<<<<< HEAD
	
=======

>>>>>>> 5156c69216521bba734f79f9c01ab8b244d847ff
	# Print some results

	#Print some results
	#print "Algorithm is done"
	#print len(SOLUTION_PATH)

	runSimulation(CARS_LIST.getVisualisationList(), SOLUTION_PATH, WIDTH, WIDTH, 0.8)

def algorithm(initialState):
	queue = []
	queue.append(initialState)
	# add first state
	STATES_ARCHIVE.addState(initialState, initialState)
	# loop all possible moves
	solutionNotFound = True
	while (not (queue == []) and solutionNotFound) :
		option = queue.pop(0)

		# Loop all options and (conditionaly) store them on the stack to revisit later
		for newOption in allMoves(option):
			# Stop the loop if option is a repeat or the solution
			if optionIsNotNew(newOption):
				continue
			elif optionIsSolution(newOption):
				SOLUTION.append(newOption)
				SOLUTION.append(option)
				solutionNotFound = False

				break
			else:
				# add the option to the queue for later evaluation
				#print "lq:" , len(queue)
				queue.append(newOption)

				# add the option to the states archive
				STATES_ARCHIVE.addState(newOption, option)

	getSolutionPath()

def deepCopyList(list):
	copiedList = []
	# for item in list:
	# 	copiedList.append(item)
	copiedList = list[::]
	return copiedList

def getSolutionPath():
	path = [SOLUTION[0]]
	parent = SOLUTION[1]
	notAtRoot = True
	# find the parent of the parent until the root is reached
	while notAtRoot:
		# print "Not at root"
		#find parent state
		parentOfParrent = STATES_ARCHIVE.getParent(parent) # dit is [ding zelf, zijn pap]
		path.append(parent)

		if parentOfParrent == INITIAL_STATE:
			notAtRoot = False
			# print "bij de root"
		parent = parentOfParrent
	# store the path (but the path needs to be flipped)
	global SOLUTION_PATH; SOLUTION_PATH = path[::-1]

def optionIsNotNew(option):
	# check tree for state
	return STATES_ARCHIVE.checkState(option)

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
			occupied.append(state[k]+WIDTH)
			occupied.append(state[k]+WIDTH*2)
		# The car is 3 long and veritcal:
		else:
			occupied.append(state[k])
			occupied.append(state[k]+WIDTH)
			occupied.append(state[k]+WIDTH*2)
		k += 1
	return occupied

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
			if state[i] + 12 not in occupied and state[i] not in range(WIDTH*(WIDTH-2),WIDTH*(WIDTH-1)):
				bord2[i] += WIDTH
				moveOptions.append(bord2)

		elif car.isHorizontal and car.length == 3:
			if state[i] - 1 not in occupied and state[i] not in  range(0,WIDTH*WIDTH,WIDTH) :
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

if __name__ == '__main__':
	main()
