
from archive import StatesArchive
from CarsList import CarsList
from Car import Car
from allBords import *
import copy
from rushhour_visualisation import *
import Queue
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
	global STATES_ARCHIVE; STATES_ARCHIVE = StatesArchive()
	algorithm(INITIAL_STATE)

	print "Algorithm is done"
	path1 = SOLUTION_PATHS[-1]
	print len(SOLUTION_PATHS)
	#print
	for solution in SOLUTION_PATHS:
		print len(solution)
	# print results
	# print "length solutions ", len(SOLUTIONS)
	# print SOLUTIONS
	# print SOLUTION_PATHS
	# print "START"
	# for i in range(0, 3100, 30):
	# 	print len(SOLUTION_PATHS[i])

	runSimulation(CARS_LIST.getVisualisationList(), path1, WIDTH, WIDTH, 0.5) # slordig dubble WIDTH meegeven

def algorithm(initialState):
	priorityQueue = Queue.PriorityQueue() # choose for Stack or PriorityStack
	# add first state
	priorityQueue.put((1, initialState))
	STATES_ARCHIVE.setInitialState(initialState)
	MaxDepth = 1000
	statescount = 0
	statesgen = 0
	# loop all possible moves
	while not priorityQueue.empty():
		#print "qeueu voor get:", list(priorityQueue.queue)
		option = priorityQueue.get();
		#print "dit gaat de qeueu out:", option
		#print "qeueu na get:", list(priorityQueue.queue)
		#print ""
		option = option[1]

		if STATES_ARCHIVE.getStateDepth(option) >= MaxDepth:
			continue
		allOptions = allMoves(option)
		statesgen += len(allOptions)
		# Loop all options and (conditionaly) store them on the stack to revisit later
		for newOption in allOptions:
			# Stop the loop if option is a repeat or the solution
			if optionIsNotNew(newOption):
				# decrease child count with one
				# replace the if and else statements by a single continue to disable
				# the search for the best option
				#if STATES_ARCHIVE.getStateDepth(newOption) > (STATES_ARCHIVE.getStateDepth(option) + 1):
				#	STATES_ARCHIVE.setState(newOption, (STATES_ARCHIVE.getStateDepth(option))+1, option)
				#	stack.push(newOption)
				#else:
				continue
			elif optionIsSolution(newOption):
				# decrease child count with one
				SOLUTION_PATHS.append(STATES_ARCHIVE.getSolutionPath(newOption, option))
				#print "max dept wanneer oplossing is gevonden", MaxDepth
				#print "length path", len(PATH_TRACKER.path)
				# When a shorter solution is found the max depth of the search is set to that length
				MaxDepth = STATES_ARCHIVE.getStateDepth(option) - 1
				# This will break the for loop so that solutions with equal length
				# are not evaluated
				break
				#return
			else:
				# add the option to the stack for later evaluation
				priorityQueue.put((getPriority(newOption), newOption))
				# add the option to the states archive
				STATES_ARCHIVE.addState(newOption, option)
				if statescount%10000 == 0:
					print "st added: ", statescount
					print "st gen: ", statesgen
				statescount += 1
		# If this node has no children go up as many levels as needed
	#getSolutionPaths()

def deepCopyList(list):
	copiedList = []
	# for item in list:
	# 	copiedList.append(item)
	copiedList = list[::]
	return copiedList

def optionIsNotNew(option):
	# check tree for state
	return STATES_ARCHIVE.checkState(option)

def getPriority(item):
	return (45- item[-1])
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

def listToTuple(inputList):
	newTuple = ()
	for item in inputList:
		newTuple += (item,)
	return newTuple

if __name__ == '__main__':
	main()
