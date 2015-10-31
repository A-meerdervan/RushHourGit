
# This is used to emulate pass by value in the canMakeMove() function
from copy import deepcopy

from Car import Car
#from "..\Pim" import rushhour_visualize #" import RushhourVisualisation
#from "C:\Users\Alex\Documents\Mprog\ProgrammeerTheorie2015\RushHourGit\Pim\rushhour_visualize" import RushhourVisualisation  #RushHourGit.Pim.rushhour_visualize import RushhourVisualisation
import sys
sys.path.insert(0, "C:\Users\Alex\Documents\Mprog\ProgrammeerTheorie2015\RushHourGit\Pim")
from rushhour_visualize import runSimulation #import RushhourVisualisation


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
RED_CAR = "| R "
RED_CAR_INT = 0
FIELD = []


def run():
	createEmptyField()
	CarsList = []

	# insert Exit
	placeExit("Left", 3)

	# insert cars
	RedCar = Car([4,3], "Horizontal" , 2, RED_CAR_INT)
	Car1 = Car([0,2], "Horizontal", 3, 1)
	Car2 = Car([3,1], "Vertical", 3, 2)

	CarsList.append(RedCar)
	CarsList.append(Car1)
	CarsList.append(Car2)

	for car in CarsList:
		placeCar(car)

	printFieldFlipped()
	moveCar(CarsList, Car2.Number, -1)
	printFieldFlipped()
	moveCar(CarsList, RedCar.Number, -4)
	printFieldFlipped()

	# in python one has no pointers, but wrapping something in list allows the 
	# function to change it outside the scope of the function. 
def moveCar(CarsList, Number, Steps):
	# First clear the car in the field
	for Coordinate in CarsList[Number].Coordinates:
		FIELD[Coordinate[1] ][ Coordinate[0] ] = EMPTY_SPOT_INT 
	# Now Set the new Coordinates and place the car
	if CarsList[Number].Direction == "Horizontal":
		CarsList[Number].setMainCoordinate([CarsList[Number].MainCoordinate[0] + Steps, CarsList[Number].MainCoordinate[1] ])
	# Car is Vertical
	else:
		CarsList[Number].setMainCoordinate([CarsList[Number].MainCoordinate[0], CarsList[Number].MainCoordinate[1] + Steps])
	placeCar(CarsList[Number])


# Steps can be positive or negative, positive x is to the right, positive y is up
def canMoveCar(carCopy, Steps):
	# Do a deep copy to emulate pass by value, since when the car cannot move, the 
	# Coordinates should not change
	car = deepcopy(carCopy)
	if car.Direction == "Horizontal":
		# Check if the car will be within the Field bounds, if not return False
		if car.MainCoordinate[0] + Steps < 0:
			print "(horiz) eerste false door car met number: " + str(car.Number)
			return False
		elif car.MainCoordinate[0] + car.Length -1 + Steps >= WIDTH:
			print "(horiz) tweede false door car met number: " + str(car.Number)
			return False
		# Move the copy of the car
		car.setMainCoordinate([car.MainCoordinate[0] + Steps, car.MainCoordinate[1] ])	
		print "move hori car: " + str(car.Number)
	# Car is Vertical:
	else:
		# Check if the car will be within the Field bounds, if not return False
		if car.MainCoordinate[1] + Steps < 0:
			print "(verti) eerste false door car met number: " + str(Car.Number)
			return False
		elif car.MainCoordinate[1] + car.Length -1 + Steps >= HEIGHT:
			print "(verti) tweede false door car met number: " + str(Car.Number)
			return False
		# Move the copy of the car
		car.setMainCoordinate([car.MainCoordinate[0], car.MainCoordinate[1] + Steps])
		print "move verti car: " + str(car.Number)
	# Loop the coordinates, when a space is not empty or the car itself, return false
	CanMoveCar = True
	for Coordinate in car.Coordinates:
		if FIELD[Coordinate[1]][Coordinate[0]] < 100 and FIELD[Coordinate[1]][Coordinate[0]] != car.Number:
			print FIELD[Coordinate[1]][Coordinate[0]]
			print Coordinate
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
			elif Item > 0:
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