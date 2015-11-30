
from Stack import Stack
from CarsList import CarsList
from tree import Tree
from Car import Car
from PathTracker import PathTracker
from allBords import *
import copy
from rushhour_visualisation import *
# this contains the state and it's parent state like:
# [state, parentState]
STATES_ARCHIVE = []
# this contains the solution state and it's parent state like:
# [state, parentState]
SOLUTIONS = []
# This contains the path to the solution backwards.
SOLUTION_PATHS = []
# This list shrinks and grows, it keeps
# track where the algorithm is in the possibilities tree
# it is used to find the path to a solution
PATH_TRACKER = PathTracker()
WIDTH = 6
CARS_LIST = CarsList()
INITIAL_STATE = []
EXIT = 0



def main():
	bordVariables = bord(5) # return [carsList,width,exit]
	global WIDTH; WIDTH = bordVariables[1]
	global EXIT; EXIT = bordVariables[2]
	global CARS_LIST; CARS_LIST = bordVariables[0]
	# TEST dept first algorithme:
	global INITIAL_STATE; INITIAL_STATE = CARS_LIST.getFirstState()
	global STATES_ARCHIVE; STATES_ARCHIVE = Tree(WIDTH, CARS_LIST.getDirectionsList())
	algorithm(INITIAL_STATE)

	print "Algorithm is done"
	path1 = SOLUTION_PATHS[-1]
	print len(SOLUTION_PATHS)
	#print
	#for solution in SOLUTION_PATHS:
		#print len(solution)

	# print results
	# print "length solutions ", len(SOLUTIONS)
	# print SOLUTIONS
	# print SOLUTION_PATHS
	# print "START"
	# for i in range(0, 3100, 30):
	# 	print len(SOLUTION_PATHS[i])

	runSimulation(CARS_LIST.getVisualisationList(), path1, WIDTH, WIDTH, 0.2) # slordig dubble WIDTH meegeven

def algorithm(initialState):
	stack = Stack()
	# add first state
	stack.push(initialState)
	STATES_ARCHIVE.addState(initialState, initialState)
	MaxDepth = 100
	# loop all possible moves
	while stack.isNotEmpty():
		option = stack.pop();
		if len(PATH_TRACKER.path) >= MaxDepth:
			PATH_TRACKER.decreaseChildCount()
			PATH_TRACKER.goUpInTreeIfNeeded()
			continue
		allOptions = allMoves(option)
		PATH_TRACKER.push( option, len(allOptions) )

		# Loop all options and (conditionaly) store them on the stack to revisit later
		for newOption in allOptions:
			# Stop the loop if option is a repeat or the solution
			if optionIsNotNew(newOption):
				# decrease child count with one
				PATH_TRACKER.decreaseChildCount()
				continue
			elif optionIsSolution(newOption):
				SOLUTIONS.append([newOption, option])
				SOLUTION_PATHS.append(deepCopyList(PATH_TRACKER.path))
				SOLUTION_PATHS[-1].append(newOption)
				# decrease child count with one
				PATH_TRACKER.decreaseChildCount()
				#print "max dept wanneer oplossing is gevonden", MaxDepth
				#print "length path", len(PATH_TRACKER.path)
				# When a shorter solution is found the max depth of the search is set to that length
				MaxDepth = len(PATH_TRACKER.path) - 1
				# This will break the for loop so that solutions with equal length
				# are not evaluated
				return
				break
			else:
				# add the option to the stack for later evaluation
				stack.push(newOption)
				# add the option to the states archive
				STATES_ARCHIVE.addState(newOption, option)
		# If this node has no children go up as many levels as needed
		PATH_TRACKER.goUpInTreeIfNeeded()
	#getSolutionPaths()

def deepCopyList(list):
	copiedList = []
	# for item in list:
	# 	copiedList.append(item)
	copiedList = list[::]
	return copiedList

def getSolutionPaths():
	# count = 0
	for solution in SOLUTIONS:
		# if count == 10:
		# 	break
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
		# count += 1

def optionIsNotNew(option):
	# check tree for state
	return STATES_ARCHIVE.checkState(option)

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
