
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
	# insert Red Car
	RedCar = Car([1,2], "Horizontal" , 2, RED_CAR_INT)
	placeCar(RedCar)
	# insert Exit
	placeExit("Left", 2)
	# insert other car
	OtherCar = Car([0,0], "Horizontal", 3, 1)
	placeCar(OtherCar)

	Bus = Car([3,0], "Vertical", 3, 2)
	placeCar(Bus)

	printField()
	# van Pim:
	# runSimulation wil een list van die dingen hieronder
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

def moveCar():
	"""
	Deze moet nog geimplementeerd worden, dus argumenten welke richting die 
	op moet ofzo, de car zelf natuurlijk en miss wel allerlei andere leipe shit.
	"""

def placeCar(car):
	for Coordinate in car.Coordinates:
		# Coordinate is (x,y) but FIeld takes[y][x]
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

def giveErrorMessage(ErrorMessage):
	print "ERROR:	" + ErrorMessage

if __name__ == '__main__':
	run()
	for Row in FIELD:
		print Row