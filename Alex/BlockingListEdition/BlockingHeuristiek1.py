
# This is used to emulate pass by value in the canMakeMove() function
from copy import deepcopy

from Car import Car

from CarsList import CarsList
from allBords import *
import random
import copy
from rushhour_visualisation import *
import Queue

WIDTH = 6
HEIGHT = 6
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
FIELD = []
CARS_LIST = CarsList()
BLOCKERS_INFO = dict()
INITIAL_STATE = []
CARSLIST = []

def run():

	# insert cars
	Car1 = Car([0,5], True, 3)
	Car2 = Car([4,2], False, 3)
	Car3 = Car([2,3], False, 2)
	Car4 = Car([1,2], True, 2)
	Car5 = Car([3,0], True, 2)
	Car6 = Car([0,0], False, 3)
	RedCar = Car([0,3], True , 2)

	# This file  uses this list wich is not a class. This should change
	CARSLIST.append(Car1)
	CARSLIST.append(Car2)
	CARSLIST.append(Car3)
	CARSLIST.append(Car4)
	CARSLIST.append(Car5)
	CARSLIST.append(Car6)
	CARSLIST.append(RedCar)

	# This is in the new format
	CARS_LIST.cars.append(Car1)
	CARS_LIST.cars.append(Car2)
	CARS_LIST.cars.append(Car3)
	CARS_LIST.cars.append(Car4)
	CARS_LIST.cars.append(Car5)
	CARS_LIST.cars.append(Car6)
	CARS_LIST.cars.append(RedCar)


	# maak een state hiervan
	for car in CARS_LIST.cars:
		INITIAL_STATE.append(car.MainCoordinate[0] + car.MainCoordinate[1]*WIDTH)

	level3 = [0, 12, 2, 10, 15, 14, 17, 25, 28, 31, 33, 21, 18]
	level4 = [0, 1, 4, 5, 7, 11, 12, 17, 18, 22, 27, 45, 48, 44, 30, 59, 32, 63, 73, 50, 69, 37]
	level5 = [0, 1, 18, 2, 11, 4, 14, 8, 20, 21, 23, 24, 26, 38, 49, 51, 52, 57, 58, 72, 68, 69, 70, 42]
	level6 = [0, 1, 4, 11, 14, 17, 19, 20, 23, 30, 31, 33, 38, 49, 50, 51, 54, 56, 61, 64, 67, 68, 70, 72, 74, 36]

	heuristic1(level3)


	# # Create an empty field filled with 0 integers that uses x, y coordinates
	# createEmptyField()
	# placeCars(INITIAL_STATE)
	# printFieldFlipped()

	# RED_CAR_INT = len(CARSLIST) - 1

	# #Algorithme
	# #get block list red car
	# BlokkadeList = getBlokkadeList(RED_CAR_INT, 0)

	# # Loop the positive and the negative subLists of the RED car
	# i = 0
	# print "Hierna moet het komen"
	# # Loop the cars that are in the way of the RED car (2 and 1)
	# for carNumber in BlokkadeList[0][:-1]:
	# 	# initiate the global blockers info that will be set by the recursive funciton
	# 	# the steps are set to 100 so that the check: (if tempSteps < steps : update) can be done 
	# 	BLOCKERS_INFO[carNumber] = dict(steps = 100, noLoop = True)
	# 	# the red car should be added for when it is checked, it means there was a loop
	# 	singleCheck([RED_CAR_INT], carNumber, carNumber, CARSLIST[RED_CAR_INT].MainCoordinate[1], 0)


	# for carNumber in BLOCKERS_INFO:
	# 	print carNumber
	# 	print BLOCKERS_INFO[carNumber]


def heuristic1(state):
	# Create an empty field filled with 0 integers that uses x, y coordinates
	createEmptyField()
	placeCars(state)
	printFieldFlipped()
	redCarIndex = len(CARSLIST) - 1
	score = 0
	#get block list red car
	BlokkadeList = getBlokkadeList(redCarIndex, 0)

	# Loop the positive subList of the RED car
	i = 0
	print "Hierna moet het komen"
	# Loop the cars that are in the way of the RED car
	for carNumber in BlokkadeList[0][:-1]:
		score += getSubScore(carNumber, CARSLIST[RED_CAR_INT].MainCoordinate[1], 0)
	print score
	for carNumber in BLOCKERS_INFO:
		print carNumber
		print BLOCKERS_INFO[carNumber]


def getSubScore(ownCarNumber, conflictNumber, tempStepsParent):
	BlokkadeList = getBlokkadeList(ownCarNumber, conflictNumber)
	# the score is set to 100 so that the check: (if tempSteps < subScore : update) can be done 
	subScore = 100
	# Loop pos and negative subLists
	for subList in BlokkadeList:
		tempSteps = tempStepsParent + abs(subList[-1])
		print "Tempt steps van ", ownCarNumber, "zijn: ", tempSteps
		# if the way is free, update if better then before
		if (subList[-1] != 0) and (len(subList) == 1):
			print "CAR Can possibly be moved! carNumber = ", ownCarNumber
			# if this is shorter, update
			if (tempSteps < subScore):
				subScore = tempSteps
				# Go to the next sublist
				continue
		# If the list is length 1 and the value 0 the car cannot move,
		# so no reason to loop cars that are not in the way
		if len(subList) != 1:
			# Loop the cars in the way of this car
			for carNumber in subList[:-1]:
				tempSteps += 1
			print "Tempt steps van ", ownCarNumber, "zijn: ", tempSteps

			# if this is shorter, update
			if (tempSteps < subScore):
				subScore = tempSteps
	print subScore
	return subScore


def recursiveCheck(carsCheckedParrent, carNumberTop, ownCarNumber, conflictNumber, tempStepsParent):
	print carNumberTop, ownCarNumber, carsCheckedParrent, conflictNumber	
	carsChecked = deepCopyList(carsCheckedParrent)
	carsChecked.append(ownCarNumber)
	print carsChecked
	BlokkadeList = getBlokkadeList(ownCarNumber, conflictNumber)
	# Loop pos and negative subLists
	for subList in BlokkadeList:
		tempSteps = tempStepsParent + abs(subList[-1])
		# if the way is free, update if better then before
		if (subList[-1] != 0) and (len(subList) == 1):
			print "CAR Can possibly be moved! carNumber = ", ownCarNumber
			# if no update was done before, update
			if (BLOCKERS_INFO[carNumberTop]["steps"] == 0):
				BLOCKERS_INFO[carNumberTop]["steps"] = tempSteps
				return 
			# if there was a loop, free path is better so update
			if (BLOCKERS_INFO[carNumberTop]["noLoop"] == False):
				BLOCKERS_INFO[carNumberTop]["steps"] = tempSteps
				noLoop = True
				return
			# if there was a previous update of a free path, check if this is shorter
			if (tempSteps < BLOCKERS_INFO[carNumberTop]["steps"]):
				BLOCKERS_INFO[carNumberTop]["steps"] = tempSteps
				return
			# update was not an improvement but quit this branch
			print "update was niet beter"

			return
			# # This is optional, it might increase the speed of the program
			# # break so you will not also check the negative list
			# break
		# Loop the cars in the way
		for carNumber in subList[:-1]:
			# if the carNumber is in carsChecked there was a loop
			if carNumber in carsChecked:
				print "loop was found"
				# if no update was done before, update
				if (BLOCKERS_INFO[carNumberTop]["steps"] == 0):
					# A loop was found
					BLOCKERS_INFO[carNumberTop]["noLoop"] = False
					BLOCKERS_INFO[carNumberTop]["steps"] = tempSteps
					return 
				# If there already was a loop and this reaches it sooner, update
				if (BLOCKERS_INFO[carNumberTop]["noLoop"] == False and (tempSteps < BLOCKERS_INFO[carNumberTop][steps])):
					BLOCKERS_INFO[carNumberTop]["steps"] = tempSteps
					return
				# If there was an update of a free path: do nothing
				print "loop update was geen verbetering"
				return
			# the direction of the car decides whether the conflict is in y or x
			if CARSLIST[ownCarNumber].isHorizontal:
				conflictNumber = CARSLIST[ownCarNumber].MainCoordinate[1]
			else:	conflictNumber = CARSLIST[ownCarNumber].MainCoordinate[0]
			# Recursively checkout the next car
			
			recursiveCheck(carsChecked, carNumberTop, carNumber, conflictNumber, tempSteps)
	


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
	print "BlokkadeList van ", Number, BlokkadeList
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
	car = CARSLIST[Number]
	# The red car is different because it should not move backwards
	if Number == RED_CAR_INT:
		y = EXIT_HEIGHT		
		for x in range(car.MainCoordinate[0] + car.length, WIDTH):
			movesNeeded += 1
			InPosDirection.append([x,y])
		InPosDirection.append(movesNeeded)
		InNegDirection.append(0)
	# For every other car:
	else:
		# if the direction is horizontal only x changes
		if car.isHorizontal:
			y = car.MainCoordinate[1]
			# Check if moving the car to the right would place it outside the field
			if (ConflictNumber + car.length) < WIDTH:
				# add the coordinates of where the car could move to
				for i in range(car.length + car.MainCoordinate[0] - ConflictNumber, car.length + 1):
					x = ConflictNumber + i
					InPosDirection.append([x,y])
					movesNeeded += 1
			# At the end of the list comes the number of moves that has to be done
			# before the car moves out of the way( if it cannot move this is 0)
			InPosDirection.append(movesNeeded)
			movesNeeded = 0
			
			# Check if moving the car to the left, would place it outside the field
			if (ConflictNumber - car.length) >= 0:
				for i in range(1 + ConflictNumber - car.MainCoordinate[0], car.length + 1):
					x = ConflictNumber - i
					InNegDirection.append([x,y])					
					movesNeeded -= 1
			# At the end of the list comes the number of moves that has to be done
			# before the car moves out of the way( if it cannot move this is 0)
			InNegDirection.append(movesNeeded)

		# if the direction is vertical only y changes
		else:
			x = car.MainCoordinate[0]
			# Check if moving the car up would place it outside the field
			if (ConflictNumber + car.length) < HEIGHT:
				# add the coordinates of where the car could move to
				for i in range((car.length + car.MainCoordinate[1] - ConflictNumber), car.length + 1):
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
				for i in range((1 + ConflictNumber  - car.MainCoordinate[1]), car.length + 1):
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

def placeCars(state):
	i = 0
	for tileNumber in state:
		for Coordinate in CARS_LIST.cars[i].getCoordinates(tileNumber, WIDTH):
			# Coordinate is (x,y) but Field takes[y][x]
			FIELD[Coordinate[1]][Coordinate[0]] = i
		i += 1

def createEmptyField():
	global FIELD; FIELD = []
	for y in range(0,WIDTH):
		# create new row
		FIELD.append([])
		# fill row with ints
		for x in range(0, WIDTH):
			FIELD[y].append(EMPTY_SPOT_INT)

def printFieldFlipped():
	for i in range(HEIGHT - 1, -1, -1):
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


def giveErrorMessage(ErrorMessage):
	print "ERROR:	" + ErrorMessage

def deepCopyList(List):
	return list(List)

if __name__ == '__main__':
	run()
	#for Row in FIELD:
		#print Row
