
from Stack import Stack
from CarsList import CarsList
from Car import Car
import copy
from allBords import *
from rushhour_visualisation import *
# this contains the state and it's parent state like:
# [state, parentState]
# this contains the solution state and it's parent state like:
# [state, parentState]
SOLUTIONS = []
# This contains the path to the solution backwards.
SOLUTION_PATHS = []
WIDTH = 6
CARS_LIST = CarsList()
INITIAL_STATE = []



def main():
	bordVariables = bord(5) # return [carsList,width,exit]
	global WIDTH; WIDTH = bordVariables[1]
	global EXIT; EXIT = bordVariables[2]
	global CARS_LIST; CARS_LIST = bordVariables[0]

	# TEST dept first algorithme:
	global INITIAL_STATE; INITIAL_STATE = CARS_LIST.getFirstState()
	global STATES_ARCHIVE; STATES_ARCHIVE = dict()

	algorithm(INITIAL_STATE)

	path1 = SOLUTION_PATHS[0]
	# print results
	# print "length solutions ", len(SOLUTIONS)
	#rint SOLUTIONS
	# print SOLUTION_PATHS


	runSimulation(CARS_LIST.getVisualisationList(), path1[::-1], WIDTH, WIDTH, 0.2)

def algorithm(initialState):
	stack = Stack()
	# add first state
	initialStateTupple = ()
	for number in initialState:
		initialStateTupple += (number,)

	STATES_ARCHIVE[initialStateTupple] = [initialState, initialState]
	stack.push(initialState)
	# loop all possible moves
	count = 0
	solutionNotFound = True
	while stack.isNotEmpty() and solutionNotFound:
		option = stack.pop();
		# Loop all options and (conditionaly) store them on the stack to revisit later
		for newOption in allMoves(option):
			# Stop the loop if option is a repeat or the solution
			if optionIsNotNew(newOption):
				continue
			elif optionIsSolution(newOption):
				SOLUTIONS.append([newOption, option])
				solutionNotFound = False
				continue

			else:
				count += 1
				# add the option to the stack for later evaluation
				stack.push(newOption)
				# add the option to the states archive
				newOptionTupple = ()
				for number in newOption:
					newOptionTupple += (number,)

				STATES_ARCHIVE[newOptionTupple] = [newOption, option]
	getSolutionPaths()

def deepCopyList(List):
	return list(List)

def getSolutionPaths():
	path = [SOLUTIONS[0]]
	parent = SOLUTIONS[0][1]
	notAtRoot = True
	# find the parent of the parent until the root is reached
	while notAtRoot:
		#find parent state
		parentTupple = ()
		for number in parent:
			parentTupple += (number,)
		parentOfParrent = STATES_ARCHIVE[parentTupple][1] # dit is [ding zelf, zijn pap]
		path.append(parent)
		
		if parentOfParrent == INITIAL_STATE:
			notAtRoot = False
		parent = parentOfParrent

	SOLUTION_PATHS.append(path)

def optionIsNotNew(option):
	# turn option into tupple
	tuppleOption = ()
	for number in option:
		tuppleOption = tuppleOption + (number,)
	# check tree for state
	return (tuppleOption in STATES_ARCHIVE)


def optionIsSolution(state):
	#checkt nog te veel maar Alex zeurt
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

		if car.isHorizontal and car.length == 2 : # moet niet car[1] maar een link naar de class zijn
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
