
from archive import StatesArchive
from CarsList import CarsList
from Car import Car
from allBords import *
import random
import copy
from rushhour_visualisation import *
import Queue


# q = Q.PriorityQueue()

# q.put((priotiteit, whatever))
# while not q.empty()
# q.get()


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
CARS_LIST = CarsList()
INITIAL_STATE = []
FIELD = []
RED_CAR_INT = 0
EMPTY_SPOT = "| _ "
EMPTY_SPOT_INT = 101
EMPTY_SPOT_RIGHT = "| _ |"

EMPTY_SPOT_RIGHT_INT = 102
EXIT_LEFT = "  _ "
EXIT_LEFT_INT = 103
EXIT_RIGHT = "| _ "
EXIT_RIGHT_INT = 104
EXIT_HEIGHT = 3
RED_CAR = "| R "
RED_CAR_INT = 6



def main():
	bordVariables = bord(3) # return [carsList,width,exit]
	global WIDTH; WIDTH = bordVariables[1]
	global EXIT; EXIT = bordVariables[2]
	global CARS_LIST; CARS_LIST = bordVariables[0]
	global CARS_LIST_LENGHT; CARS_LIST_LENGHT = len(CARS_LIST.cars)
	# TEST dept first algorithme:
	global INITIAL_STATE; INITIAL_STATE = CARS_LIST.getFirstState()
	global STATES_ARCHIVE; STATES_ARCHIVE = StatesArchive()
	global RED_CAR_INT; RED_CAR_INT = len(CARS_LIST.cars) - 1	
	algorithm(INITIAL_STATE)

	print "Algorithm is done"
	path1 = SOLUTION_PATHS[-1]
	print len(SOLUTION_PATHS)
	# #print
	for solution in SOLUTION_PATHS:
		print len(solution)
	# print results
	# print "length solutions ", len(SOLUTIONS)
	# print SOLUTIONS
	# print SOLUTION_PATHS
	# print "START"
	# for i in range(0, 3100, 30):
	# 	print len(SOLUTION_PATHS[i])

	# runSimulation(CARS_LIST.getVisualisationList(), path1, WIDTH, WIDTH, 0.2) # slordig dubble WIDTH meegeven

def algorithm(initialState):
	priorityQueue = Queue.PriorityQueue() # choose for Stack or PriorityStack
	# add first state
	priorityQueue.put((0, initialState))
	# queue = []
	# queue.append(initialState)
	STATES_ARCHIVE.setInitialState(initialState)
	statesCount = 0

	# loop all possible moves
	# while queue:
	while not priorityQueue.empty():
		# option = queue.pop(0)
		option = priorityQueue.get()[1]

		allOptions = allMoves(option)
		# Loop all options and (conditionaly) store them on the stack to revisit later
		# for optionIndex in random.sample(range(0, len(allOptions)), len(allOptions)):
		# 	newOption = allOptions[optionIndex]
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
				print statesCount
				# decrease child count with one
				SOLUTION_PATHS.append(STATES_ARCHIVE.getSolutionPath(newOption, option))
				#print "max dept wanneer oplossing is gevonden", MaxDepth
				#print "length path", len(PATH_TRACKER.path)
				# When a shorter solution is found the max depth of the search is set to that length
				# This will break the for loop so that solutions with equal length
				# are not evaluated
				# break
				return
			else:
				variables = getPriority(newOption, option)
				# If this is true than the option is a solution
				# if variables[1]:
				# 	print statesCount
				# 	SOLUTION_PATHS.append(STATES_ARCHIVE.getSolutionPath(newOption, option))
				# 	print "trucje was eerst"
				# 	return
				priorityQueue.put((variables[0], newOption))
				# queue.append(newOption)

				# add the option to the stack for later evaluation
				# priorityQueue.put((getPriority(newOption, option), newOption))
				# add the option to the states archive
				STATES_ARCHIVE.addState(newOption, option)
				if statesCount%10000 == 0:
					print "st added: ", statesCount
				statesCount += 1
		# If this node has no children go up as many levels as needed
	#getSolutionPaths()

def getPriority(newOption, option):
	priority = 0
	priority += STATES_ARCHIVE.states[listToTuple(option)][2] + 1
	variables = heuristic1(newOption)
	priority += variables[0]
	return [priority, variables[1]]

	# priority += numberOfCarsBlocking(newOption)

	# if newOption[-1] > option[-1]:
	# 	return priority + STATES_ARCHIVE.states[listToTuple(option)][2] + 1
	# elif newOption[-1] == option[-1]:
	# 	# Check the parent state's depth
	# 	return priority + STATES_ARCHIVE.states[listToTuple(option)][2] + 1 + 20
	# 	# if the car moves to the left, the score is one extra
	# else:
	# 	return priority + STATES_ARCHIVE.states[listToTuple(option)][2] +  2 + 20 # + 2

def heuristic1(state):
	# Create an empty field filled with 0 integers that uses x, y coordinates
	createEmptyField()
	placeCars(state)
	redCarIndex = len(CARS_LIST.cars) - 1
	score = 0
	#get block list red car
	BlokkadeList = getBlokkadeList(redCarIndex, 0)

	# Loop the positive subList of the RED car
	i = 0
	# Loop the cars that are in the way of the RED car
	carCount = 0
	freePathCount = 0
	for carNumber in BlokkadeList[0][:-1]:
		carCount += 1
		variables = getSubScore(carNumber, CARS_LIST.cars[RED_CAR_INT].mainCoordinate[1], 0)
		score += variables[0]
		freePathCount += variables[1]
	# if carCount is freePathCount this means that this is actualy certainly a position close to a solution. 
	return [score, freePathCount == carCount]


def getSubScore(ownCarNumber, conflictNumber, tempStepsParent):
	BlokkadeList = getBlokkadeList(ownCarNumber, conflictNumber)
	# the score is set to 100 so that the check: (if tempSteps < subScore : update) can be done 
	subScore = 100
	freePath = 0
	# Loop pos and negative subLists
	for subList in BlokkadeList:
		tempSteps = tempStepsParent + abs(subList[-1])
		# if the way is free, update if better then before
		if (subList[-1] != 0) and (len(subList) == 1):
			# if this is shorter, update
			if (tempSteps < subScore):
				subScore = tempSteps
				freePath = 1
				# Go to the next sublist
				continue
		# If the list is length 1 and the value 0 the car cannot move,
		# so no reason to loop cars that are not in the way
		if len(subList) != 1:
			# Loop the cars in the way of this car
			for carNumber in subList[:-1]:
				tempSteps += 2

			# if this is shorter, update
			if (tempSteps < subScore):
				subScore = tempSteps
	return [subScore, freePath]


	# This function returns the a list of car numbers that block the path
def getBlokkadeList(Number, ConflictNumber):
	BlokkadeList = [ [], [] ]
	CoordinatesToFree = getCoordinatesToFree(Number, ConflictNumber)
	i = 0
	# Loop for pos and neg coordinate lists
	for subCoordinates in CoordinatesToFree:
		for j in range(0, len(subCoordinates) - 1):
			Coordinate = subCoordinates[j]
			Item = FIELD[Coordinate[1] ][ Coordinate[0] ]
			# only add if it is a different car
			if Item < 100 and Item != Number:
				# Prevent duplicates when adding
				if Item not in BlokkadeList[i]:
					BlokkadeList[i].append(Item)
		# Add the moves needed at the back of the list
		BlokkadeList[i].append(subCoordinates[-1])
		i += 1
	return BlokkadeList

	# This function returns a list of coordinates that have to be free
	# to allow the car to move away from a line of conflict.
def getCoordinatesToFree(Number, ConflictNumber):
	CoordinatesToFree = []
	InPosDirection = []
	InNegDirection = []
	# This is the number of moves needed for the car to move out of the way
	# it is 0 when the car cannot move
	movesNeeded = 0
	car = CARS_LIST.cars[Number]
	# The red car is different because it should not move backwards
	if Number == RED_CAR_INT:
		# WIDTH/2 is the position of the exit
		y = WIDTH/2		
		for x in range(car.mainCoordinate[0] + car.length, WIDTH):
			movesNeeded += 1
			InPosDirection.append([x,y])
		InPosDirection.append(movesNeeded)
		InNegDirection.append(0)
	# For every other car:
	else:
		# if the direction is horizontal only x changes
		if car.isHorizontal:
			y = car.mainCoordinate[1]
			# Check if moving the car to the right would place it outside the field
			if (ConflictNumber + car.length) < WIDTH:
				# add the coordinates of where the car could move to
				for i in range(car.length + car.mainCoordinate[0] - ConflictNumber, car.length + 1):
					x = ConflictNumber + i
					InPosDirection.append([x,y])
					movesNeeded += 1
			# At the end of the list comes the number of moves that has to be done
			# before the car moves out of the way( if it cannot move this is 0)
			InPosDirection.append(movesNeeded)
			movesNeeded = 0
			
			# Check if moving the car to the left, would place it outside the field
			if (ConflictNumber - car.length) >= 0:
				for i in range(1 + ConflictNumber - car.mainCoordinate[0], car.length + 1):
					x = ConflictNumber - i
					InNegDirection.append([x,y])					
					movesNeeded -= 1
			# At the end of the list comes the number of moves that has to be done
			# before the car moves out of the way( if it cannot move this is 0)
			InNegDirection.append(movesNeeded)

		# if the direction is vertical only y changes
		else:
			x = car.mainCoordinate[0]
			# Check if moving the car up would place it outside the field
			if (ConflictNumber + car.length) < WIDTH:
				# add the coordinates of where the car could move to
				for i in range((car.length + car.mainCoordinate[1] - ConflictNumber), car.length + 1):
					y = ConflictNumber + i
					InPosDirection.append([x,y])
					movesNeeded += 1
			# At the end of the list comes the number of moves that has to be done
			# before the car moves out of the way( if it cannot move this is 0)
			InPosDirection.append(movesNeeded)
			movesNeeded = 0
			# Check if moving the car down, would place it outside the field
			if (ConflictNumber - car.length) >= 0:
				# Add all tiles that have to be free to move this car
				for i in range((1 + ConflictNumber  - car.mainCoordinate[1]), car.length + 1):
					y = ConflictNumber - i
					InNegDirection.append([x,y])
					movesNeeded -= 1
			# At the end of the list comes the number of moves that has to be done
			# before the car moves out of the way( if it cannot move this is 0)
			InNegDirection.append(movesNeeded)
		


	# Add the tiles that could be freed in both negative as positive direction
	CoordinatesToFree.append(InPosDirection)
	CoordinatesToFree.append(InNegDirection)

	return CoordinatesToFree

def createEmptyField():
	global FIELD; FIELD = []
	for y in range(0,WIDTH):
		# create new row
		FIELD.append([])
		# fill row with ints
		for x in range(0, WIDTH):
			FIELD[y].append(EMPTY_SPOT_INT)

def placeCars(state):
	i = 0
	for tileNumber in state:
		for Coordinate in CARS_LIST.cars[i].getCoordinates(tileNumber, WIDTH):
			# Coordinate is (x,y) but Field takes[y][x]
			FIELD[Coordinate[1]][Coordinate[0]] = i
		i += 1

def numberOfCarsBlocking(state):
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

def deepCopyList(list):
	copiedList = []
	# for item in list:
	# 	copiedList.append(item)
	copiedList = list[::]
	return copiedList

def optionIsNotNew(option):
	# check tree for state
	return STATES_ARCHIVE.checkState(option)

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

def printFieldFlipped():
	for i in range(WIDTH - 1, -1, -1):
		Row = FIELD[i]
		RowString = "	"
		for Item in Row:
			if Item == EMPTY_SPOT_INT:
				ItemString = EMPTY_SPOT
			elif Item == EMPTY_SPOT_RIGHT_INT:
				ItemString = EMPTY_SPOT_RIGHT
			elif Item == EXIT_LEFT_INT:
			 	ItemString = EXIT_LEFT
			elif Item == EXIT_RIGHT_INT:
				ItemString = EXIT_RIGHT
			elif Item == RED_CAR_INT:
				ItemString = RED_CAR
			elif Item >= 0:
				ItemString = "| " + str(Item) + " "
			RowString += ItemString
		print RowString
	print

if __name__ == '__main__':
	main()
