
from Stack import Stack
from CarsList import CarsList
from tree import Tree
from Car import Car
import copy
from rushhour_visualisation import *
import sys

# this contains the state and it's parent state like:
# [state, parentState]
STATES_ARCHIVE = []
# this contains the solution state and it's parent state like:
# [state, parentState]
SOLUTIONS = []
# This contains the path to the solution backwards.
SOLUTION_PATHS = []
WIDTH = 6
HEIGHT = 6
CARS_LIST = CarsList()
INITIAL_STATE = []
DEPTH_LIMIT = 1000


def main():

	# Car1 = Car(22, False, 3)
	# Car2 = Car(9, False, 2)
	# Car3 = Car(10, True, 2)
	# RedCar = Car(20, True, 2)

	# CARS_LIST.cars.append(Car1)
	# CARS_LIST.cars.append(Car2)
	# CARS_LIST.cars.append(Car3)
	# CARS_LIST.cars.append(RedCar)

	RedCar = Car(20, True, 2)
	Car1 = Car(0, False, 2)
	Car2 = Car(12, True, 2)
	Car3 = Car(3, False, 2)
	Car4 = Car(4, True, 2)
	Car5 = Car(10, True, 2)
	Car6 = Car(14, True, 2)
	Car7 = Car(16, False, 2)
	Car8 = Car(17, False, 3)
	Car9 = Car(25, True, 2)
	Car10 = Car(27, True, 2)
	Car11 = Car(32, True, 2)
	Car12 = Car(34, True, 2)

	CARS_LIST.cars.append(Car1)
	CARS_LIST.cars.append(Car2)
	CARS_LIST.cars.append(Car3)
	CARS_LIST.cars.append(Car4)
	CARS_LIST.cars.append(Car5)
	CARS_LIST.cars.append(Car6)
	CARS_LIST.cars.append(Car7)
	CARS_LIST.cars.append(Car8)
	CARS_LIST.cars.append(Car9)
	CARS_LIST.cars.append(Car10)
	CARS_LIST.cars.append(Car11)
	CARS_LIST.cars.append(Car12)
	CARS_LIST.cars.append(RedCar)

	# TEST dept first algorithme:
	global INITIAL_STATE; INITIAL_STATE = CARS_LIST.getFirstState()
	global STATES_ARCHIVE; STATES_ARCHIVE = Tree(WIDTH, CARS_LIST.getDirectionsList())
	algorithm(INITIAL_STATE)
	path1 = SOLUTION_PATHS[0]

	# print results
	# print "length solutions ", len(SOLUTIONS)
	#rint SOLUTIONS
	print len(SOLUTION_PATHS)
	listSolutionsPaths = []
	for sols in SOLUTION_PATHS:
		listSolutionsPaths.append(len(sols))
	print listSolutionsPaths

	pathDepth = []
	for state in path1[:-1]:
		print len(state), state
		pathDepth.append(STATES_ARCHIVE.goToEndNode(state).depth)
	print pathDepth
	#runSimulation(CARS_LIST.getVisualisationList(), path1[::-1], WIDTH, HEIGHT, 0.2)

def findDuplicates(list):
	checkList = []
	for item in list:
		if item in checkList:
			return True
		checkList.append(item)
	return False

def algorithm(initialState):
	stack = Stack()
	DEPTH_LIMIT = 1000
	# add first state
	stack.push(initialState)
	STATES_ARCHIVE.addState(initialState, initialState, 1)
	# loop all possible moves
	count = 0
	while stack.isNotEmpty():
		option = stack.pop();
		if STATES_ARCHIVE.goToEndNode(option).depth > DEPTH_LIMIT:
			continue
		# Loop all options and (conditionaly) store them on the stack to revisit later
		for newOption in allMoves(option):
			# Stop the loop if option is a repeat or the solution
			if optionIsNotNew(newOption, option):
				continue
			elif optionIsSolution(newOption):
				SOLUTIONS.append([newOption, option])
				DEPTH_LIMIT = STATES_ARCHIVE.goToEndNode(option).depth
				print(DEPTH_LIMIT)
				#getSolutionPaths()
				continue

			else:
				count += 1
				# add the option to the stack for later evaluation
				stack.push(newOption)
				# add the option to the states archive
				STATES_ARCHIVE.addState(newOption, option)
			#if count == 150:
				#rint "Stack : ", stack.items
	# print "Stack : ", stack.items
	getSolutionPaths()

def getSolutionPaths():
	count = 0
	for solution in SOLUTIONS:
		#if count == 10:
		#	break
		path = [solution[0]]
		parent = solution[1]
		notAtRoot = True
		# find the parent of the parent until the root is reached
		while notAtRoot:
			# print "Not at root"
			#find parent state
			parentOfParrent = STATES_ARCHIVE.getParent(parent) # dit is [ding zelf, zijn pap]
			path.append(parent)
			# print "Parent of parent: ", parentOfParrent
			# print "Intital state: ", INITIAL_STATE
			if parentOfParrent == INITIAL_STATE:
				notAtRoot = False
				# print "bij de root"
			parent = parentOfParrent
		# print path
		SOLUTION_PATHS.append(path)
		count += 1

def optionIsNotNew(newOption, option):
	# check tree for state
	return STATES_ARCHIVE.checkState(newOption, option)

# def optionIsSolution(option):
# 	# Verzin hier iets voor, gewoon als alle dingen van rode auto tot uitgang
# 	# vrij zijn.
# 	if option in [8,13]:
# 		return True
# 	return False

def optionIsSolution(state):
	#checkt nog te veel maar Alex zeurt
	occupied = getOccupiedTiles(state)
	arraycounter =[]
	EXIT = 22
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
			occupied.append(state[k]+HEIGHT)
			occupied.append(state[k]+HEIGHT*2)
		k += 1
	return occupied

def deepCopyList(list):
	copiedList = []
	# for item in list:
	# 	copiedList.append(item)
	copiedList = list[::]
	return copiedList

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
			if state[i] - HEIGHT not in occupied and state[i] not in  range(WIDTH):
				bord[i] -= HEIGHT
				moveOptions.append(bord)
			if state[i] + 3*HEIGHT not in occupied and state[i] not in range(WIDTH*(WIDTH-3),WIDTH*(WIDTH-2)):
				bord2[i] += HEIGHT
				moveOptions.append(bord2)
		i += 1

	return moveOptions


if __name__ == '__main__':
	main()
