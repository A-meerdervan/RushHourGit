
# This is used to emulate pass by value in the canMakeMove() function
from copy import deepcopy

from Car import Car
#from "..\Pim" import rushhour_visualize #" import RushhourVisualisation
#from "C:\Users\Alex\Documents\Mprog\ProgrammeerTheorie2015\RushHourGit\Pim\rushhour_visualize" import RushhourVisualisation  #RushHourGit.Pim.rushhour_visualize import RushhourVisualisation
import sys
#sys.path.insert(0, "C:\Users\daan\Desktop\Nieuwe map\RushHourGit\Pim")
#from rushhour_visualize import runSimulation #import RushhourVisualisation


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
RED_CAR_INT = 5
FIELD = []
CARSLIST = []


def run():
	createEmptyField()
	# insert Exit
	placeExit("Right", EXIT_HEIGHT)

	# insert cars
	Car1 = Car([0,5], "Horizontal", 3, 0)
	Car2 = Car([4,2], "Vertical", 3, 1)
	Car3 = Car([2,3], "Vertical", 2, 2)
	Car4 = Car([1,2], "Horizontal", 2, 3)
	Car5 = Car([3,0], "Horizontal", 2, 4)
	RedCar = Car([0,3], "Horizontal" , 2, 5)


	CARSLIST.append(Car1)
	CARSLIST.append(Car2)
	CARSLIST.append(Car3)
	CARSLIST.append(Car4)
	CARSLIST.append(Car5)
	CARSLIST.append(RedCar)

	blockingLists = []
	for car in CARSLIST:
		placeCar(car)
		blockingLists.append([ [], [], ])

	RED_CAR_INT = len(CARSLIST) - 1
	printFieldFlipped()

	# Algorithme
	# get block list red car
	BlokkadeList = getBlokkadeList(RED_CAR_INT, 0)
	blockingLists[RED_CAR_INT] = BlokkadeList

	# Loop the positive and the negative subLists of the RED car
	i = 0
	print "Hierna moet het komen"
	for subList in BlokkadeList:
		# if there is no car in the way of the red car this is a SOLUTION
		if (BlokkadeList[i][-1]) != 0 and len(BlokkadeList[i]) == 1:
			print "SOLUTIONFOUND!"
			break
		# Loop the cars that are in the way of the RED car (2 and 1)
		for carNumber in subList[:-1]:
			BlokkadeList = getBlokkadeList(carNumber, CARSLIST[RED_CAR_INT].MainCoordinate[1])
			blockingLists[carNumber] = BlokkadeList
			# Loop pos and negative subLists
			j = 0
			for subList in BlokkadeList:
			# if there is no car in the way of the car
				print "Carnumber", carNumber
				if (BlokkadeList[j][-1]) != 0 and len(BlokkadeList[j]) == 1:
					print "CAR Can be moved! and j = ", j
					# move car
					moveCar(carNumber, BlokkadeList[j][-1])
					# update map by popping something
					# break so you will not also check the negative list
					break

				# Loop the cars in the way (0 en 3) the first time, the second time (4)
				for carNumber1 in subList[:-1]:
					BlokkadeList = getBlokkadeList(carNumber1, CARSLIST[carNumber].MainCoordinate[0])
					blockingLists[carNumber1] = BlokkadeList
					# Loop pos and negative subLists
					k = 0
					keepGoing = True
					for subList in BlokkadeList:
						if not keepGoing:
							break
						else:
						# if there is no car in the way of the car
							print "Carnumber1", carNumber1
							if (BlokkadeList[k][-1]) != 0 and len(BlokkadeList[k]) == 1:
								print "CAR Can be moved! and j = ", k
								# move car
								moveCar(carNumber1, BlokkadeList[k][-1])
								# update map by popping something
								keepGoing = False
								break
								# notBreak = False
							print "DE BREAK HEEFT NIET GEWERKT want j is ", j
							# Loop the cars in the way (0 en 3)
							for carNumber2 in subList[:-1]:
								print "niets"
								print "CarNumber2 ", carNumber2 
						k += 1
				j += 1
		i += 1



	# # Dit is een zootje bullshit
	# BlokkadeList = getBlokkadeList(RED_CAR_INT, 0)
	# print "BlokkadeList RED_CAR: "
	# print BlokkadeList
	# # Loop the cars in the positive list
	# for CarNumber in BlokkadeList[0][0:-1]:
	# 	# The y of the Redcar is the height of conflict
	# 	BlokkadeList1 = getBlokkadeList(CarNumber, CARSLIST[RED_CAR_INT].MainCoordinate[1])
	# 	print "Per auto ", CarNumber, ": BlokkadeList: "
	# 	print BlokkadeList1
	# 	# If the positive blocking list is empty move 1 in pos direction
	# 	if BlokkadeList[0][-1] != 0 and len(BlokkadeList[0]) == 1:
	# 		if canMoveCar(CarNumber, BlokkadeList1[0][-1] ):
	# 			print "move pos"
	# 			moveCar(CarNumber, BlokkadeList1[0][-1] )
	# 	# or if the negative blocking list is empty, move 1 in neg direction
	# 	elif (BlokkadeList[0][-1]) != 0 and len(BlokkadeList[0]) == 1:
	# 		if canMoveCar(CarNumber, BlokkadeList1[1][-1] ):
	# 			print "move neg"
	# 			moveCar(CarNumber, BlokkadeList1[1][-1] )
	# # Test voor horizontale auto die een list wil krijgen
	# # Car 1 moet aan de kant voor Car3, die heeft conflict x = 2
	# BlokkadeList = getBlokkadeList(Car1.Number, 2)
	# print "De BlokkadeList van 1 wanneer hij aan de kant moet voor 3 is: "
	# print BlokkadeList
	# # If the positive blocking list is empty move 1 in pos direction
	# if (BlokkadeList[0][-1]) != 0 and len(BlokkadeList[0]) == 1:
	# 	print "in if"
	# 	if canMoveCar(Car1.Number, BlokkadeList[0][-1] ):
	# 		print "move pos"
	# 		moveCar(Car1.Number, BlokkadeList[0][-1] )

#	moveCar(Car2.Number, -1)
#	moveCar(RedCar.Number, -4)


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
		for x in range(car.MainCoordinate[0] + car.Length, WIDTH):
			movesNeeded += 1
			InPosDirection.append([x,y])
		InPosDirection.append(movesNeeded)
		InNegDirection.append(0)
	# For every other car:
	else:
		# if the direction is vertical only y changes
		if car.Direction == "Vertical":
			x = car.MainCoordinate[0]
			# Check if moving the car up would place it outside the field
			if (ConflictNumber + car.Length) < HEIGHT:
				# add the coordinates of where the car could move to
				for i in range((car.Length + car.MainCoordinate[1] - ConflictNumber), car.Length + 1):
					y = ConflictNumber + i
					InPosDirection.append([x,y])
					movesNeeded += 1
			# At the end of the list comes the number of moves that has to be done
			# before the car moves out of the way
			InPosDirection.append(movesNeeded)
			movesNeeded = 0
			# Check if moving the car down, would place it outside the field
			if (ConflictNumber - car.Length) >= 0:
				# Add all tiles that have to be free to move this car
				for i in range((1 + ConflictNumber  - car.MainCoordinate[1]), car.Length + 1):
					y = ConflictNumber - i
					InNegDirection.append([x,y])
					movesNeeded -= 1
			# At the end of the list comes the number of moves that has to be done
			# before the car moves out of the way
			InNegDirection.append(movesNeeded)
		
		#car.Direction == "Horizontal"
		else:
			y = car.MainCoordinate[1]
			# Check if moving the car to the right would place it outside the field
			print ConflictNumber + car.Length
			print WIDTH
			if (ConflictNumber + car.Length) < WIDTH:
				print "in if"
				# add the coordinates of where the car could move to
				for i in range(car.Length + car.MainCoordinate[0] - ConflictNumber, car.Length + 1):
					x = ConflictNumber + i
					InPosDirection.append([x,y])
					movesNeeded += 1
			# At the end of the list comes the number of moves that has to be done
			# before the car moves out of the way
			InPosDirection.append(movesNeeded)
			movesNeeded = 0
			
			# Check if moving the car to the left, would place it outside the field
			if (ConflictNumber - car.Length) >= 0:
				for i in range(1 + ConflictNumber - car.MainCoordinate[0], car.Length + 1):
					x = ConflictNumber - i
					InNegDirection.append([x,y])					
					movesNeeded -= 1
			# At the end of the list comes the number of moves that has to be done
			# before the car moves out of the way
			InNegDirection.append(movesNeeded)

	# Add the tiles that could be freed in both negative as positive direction
	CoordinatesToFree.append(InPosDirection)
	CoordinatesToFree.append(InNegDirection)

	return CoordinatesToFree

def moveCar(Number, Steps):
	# First clear the car in the field
	for Coordinate in CARSLIST[Number].Coordinates:
		FIELD[Coordinate[1] ][ Coordinate[0] ] = EMPTY_SPOT_INT
	# Now Set the new Coordinates and place the car
	if CARSLIST[Number].Direction == "Horizontal":
		CARSLIST[Number].setMainCoordinate([CARSLIST[Number].MainCoordinate[0] + Steps, CARSLIST[Number].MainCoordinate[1] ])
	# Car is Vertical
	else:
		CARSLIST[Number].setMainCoordinate([CARSLIST[Number].MainCoordinate[0], CARSLIST[Number].MainCoordinate[1] + Steps])
	placeCar(CARSLIST[Number])
	# print the field after each move
	printFieldFlipped()


# Steps can be positive or negative, positive x is to the right, positive y is up
def canMoveCar(carNumber, Steps):
	# Do a deep copy to emulate pass by value, since when the car cannot move, the
	# Coordinates should not change
	car = deepcopy(CARSLIST[carNumber])
	if car.Direction == "Horizontal":
		# Check if the car will be within the Field bounds, if not return False
		if car.MainCoordinate[0] + Steps < 0:
			return False
		elif car.MainCoordinate[0] + car.Length -1 + Steps >= WIDTH:
			return False
		# Move the copy of the car
		car.setMainCoordinate([car.MainCoordinate[0] + Steps, car.MainCoordinate[1] ])
	# Car is Vertical:
	else:
		# Check if the car will be within the Field bounds, if not return False
		if car.MainCoordinate[1] + Steps < 0:
			return False
		elif car.MainCoordinate[1] + car.Length -1 + Steps >= HEIGHT:
			return False
		# Move the copy of the car
		car.setMainCoordinate([car.MainCoordinate[0], car.MainCoordinate[1] + Steps])
	# Loop the coordinates, when a space is not empty or the car itself, return false
	CanMoveCar = True
	for Coordinate in car.Coordinates:
		if FIELD[Coordinate[1]][Coordinate[0]] < 100 and FIELD[Coordinate[1]][Coordinate[0]] != car.Number:
			CanMoveCar = False
			break
	return CanMoveCar


def placeCar(car):
	for Coordinate in car.Coordinates:
		# Coordinate is (x,y) but Field takes[y][x]
		FIELD[Coordinate[1]][Coordinate[0]] = car.Number

def placeExit(Side, Y):
	if Side == "Left":
		FIELD[Y][0] = EXIT_LEFT_INT
	elif Side == "Right":
		FIELD[Y][WIDTH - 1] = EXIT_RIGHT_INT
	else:
		ErrorMessage = "Exit was placed neather right nor left"
		giveError(ErrorMessage)


def createEmptyField():
	for y in range(0,HEIGHT):
		# create new row
		FIELD.append([])
		# fill row with strings
		for x in range(0, WIDTH - 1):
			FIELD[y].append(EMPTY_SPOT_INT)
		FIELD[y].append(EMPTY_SPOT_RIGHT_INT)


def printField():
	for Row in FIELD:
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
			elif Item > 0:
				ItemString = "| " + str(Item) + " "
			RowString += ItemString
		print RowString

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

if __name__ == '__main__':
	run()
	#for Row in FIELD:
		#print Row
