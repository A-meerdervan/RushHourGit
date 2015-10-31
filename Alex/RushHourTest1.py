
from Car import Car
#from "..\Pim" import rushhour_visualize #" import RushhourVisualisation
#from "C:\Users\Alex\Documents\Mprog\ProgrammeerTheorie2015\RushHourGit\Pim\rushhour_visualize" import RushhourVisualisation  #RushHourGit.Pim.rushhour_visualize import RushhourVisualisation
import sys
sys.path.insert(0, "C:\Users\Alex\Documents\Mprog\ProgrammeerTheorie2015\RushHourGit\Pim")
from rushhour_visualize import runSimulation #import RushhourVisualisation


WIDTH = 5
HEIGHT = 5
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
	placeExit("Left", 2)

	# insert Red Car
	RedCar = Car([0,2], "Horizontal" , 2, RED_CAR_INT)
	CarsList.append(RedCar)
	placeCar(RedCar)
	print canMoveCar(RedCar, 2)
	print RedCar.Coordinates
	moveCar(CarsList, RedCar.Number, 2)

	# insert other car
	OtherCar = Car([0,1], "Horizontal", 3, 1)
	CarsList.append(OtherCar)
	placeCar(OtherCar)

	Bus = Car([3,0], "Vertical", 3, 2)
	placeCar(Bus)
	CarsList.append(Bus)

	moveCar(CarsList, Bus.Number, 2)
	printFieldFlipped()
	print
	moveCar(CarsList, Bus.Number, -2)
	printFieldFlipped()

	#print canMoveCar(Bus, 1)
	#placeCar(Bus)

	# van Pim:
	# runSimulation wil een list van die dingen hieronder
	"""
	car1 = [1, 4, 'v', 2, 'green']
	car2 = [2, 5, 'h', 3, 'yellow']
	car3 = [5, 4, 'v', 2, 'light sky blue']
	car4 = [0, 3, 'h', 2, 'red']
	car5 = [3, 3, 'v', 2, 'orange']
	car6 = [4, 2, 'v', 3, 'violet']
	car7 = [2, 0, 'v', 2, 'pink']
	car8 = [3, 0, 'h', 2, 'cyan']
	car9 = [5, 0, 'v', 2, 'magenta']
	car10 = [1, 2, 'h', 3, 'blue']
	carList = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]
	runSimulation(carList, 6, 6)
	"""
	# in python one has no pointers, but wrapping something in list allows the 
	#function to change it outside the scope of the function. 
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
	print CarsList[Number].Coordinates
	placeCar(CarsList[Number])


# Steps can be positive or negative, positive x is to the right, positive y is up
def canMoveCar(carCopy, Steps):
	car = carCopy
	if car.Direction == "Horizontal":
		car.setMainCoordinate([car.MainCoordinate[0] + Steps, car.MainCoordinate[1] ])
	# Car is Vertical
	else:
		car.setMainCoordinate([car.MainCoordinate[0], car.MainCoordinate[1] + Steps])
	# Loop the coordinates, when a space is not empty or the car itself, return false
	CanMoveCar = True
	for Coordinate in car.Coordinates:
		if FIELD[Coordinate[1]][Coordinate[0]] < 100 and not car.Number:
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


def giveErrorMessage(ErrorMessage):
	print "ERROR:	" + ErrorMessage

if __name__ == '__main__':
	run()
	#for Row in FIELD:
		#print Row