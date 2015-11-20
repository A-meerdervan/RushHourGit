
from Stack import Stack
from CarsList import CarsList
from tree import Tree
from Car import Car
import copy
import Queue
from rushhour_visualisation import *
# this contains the state and it's parent state like:
# [state, parentState]
STATES_ARCHIVE = []
# this contains the solution state and it's parent state like:
# [state, parentState]
SOLUTION = []
# This contains the path to the solution backwards.
SOLUTION_PATH = []
WIDTH = 6
HEIGHT = 6
CARS_LIST = CarsList()
INITIAL_STATE = []



def main():

	# Initialize cars
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

	#Print some results
	#print "Algorithm is done"
	#print len(SOLUTION_PATH)

	#runSimulation(CARS_LIST.getVisualisationList(), SOLUTION_PATH, WIDTH, HEIGHT, 0.8)

def algorithm(initialState):
	queue = []
	queue.append(initialState)
	# add first state
	STATES_ARCHIVE.addState(initialState, initialState)
	# loop all possible moves
	solutionNotFound = True
	while (not (queue == []) and solutionNotFound) :
		option = queue.pop(0)
		# Loop all options and (conditionaly) store them on the stack to revisit later
		for newOption in allMoves(option):
			# Stop the loop if option is a repeat or the solution
			if optionIsNotNew(newOption):
				continue
			elif optionIsSolution(newOption):
				SOLUTION.append(newOption)
				SOLUTION.append(option)
				solutionNotFound = False
				break
			else:
				# add the option to the queue for later evaluation
				queue.append(newOption)
				# add the option to the states archive
				STATES_ARCHIVE.addState(newOption, option)
	getSolutionPath()

def deepCopyList(list):
	copiedList = []
	# for item in list:
	# 	copiedList.append(item)
	copiedList = list[::]
	return copiedList

def getSolutionPath():

	path = [SOLUTION[0]]
	parent = SOLUTION[1]
	notAtRoot = True
	# find the parent of the parent until the root is reached
	while notAtRoot:
		# print "Not at root"
		#find parent state
		parentOfParrent = STATES_ARCHIVE.getParent(parent) # dit is [ding zelf, zijn pap]
		path.append(parent)

		if parentOfParrent == INITIAL_STATE:
			notAtRoot = False
			# print "bij de root"
		parent = parentOfParrent
	# store the path (but the path needs to be flipped)
	global SOLUTION_PATH; SOLUTION_PATH = path[::-1]

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

def allMoves(state):
	moveOptions = []
	i = 0
	occupied = getOccupiedTiles(state)

	for car in CARS_LIST.cars:
		bord = deepCopyList(state)
		bord2 = deepCopyList(state)

		if car.isHorizontal and car.length == 2 :
			if state[i] -1 not in occupied and state[i] not in range(0,36,6): # moet niet op een bezette tegel of buiten het bord belanden
				bord[i] -= 1
				moveOptions.append(bord)
			if state[i] + 2 not in occupied and state[i] not in range(4,40,6): # range om te kijken of de positie binnen het bereik van het bord is.
				bord2[i] += 1
				moveOptions.append(bord2)

		elif not car.isHorizontal and car.length == 2:
			if state[i] - WIDTH not in occupied  and state[i] not in  range(6):
				bord[i] -= WIDTH
				moveOptions.append(bord)
			if state[i] + 12 not in occupied and state[i] not in range(24,30):
				bord2[i] += WIDTH
				moveOptions.append(bord2)

		elif car.isHorizontal and car.length == 3:
			if state[i] - 1 not in occupied and state[i] not in  range(0,36,6) :
				bord[i] -= 1
				moveOptions.append(bord)
			if state[i] + 3 not in occupied and state[i] not in  range(3,39,6):
				bord2[i] += 1
				moveOptions.append(bord2)

		elif not car.isHorizontal and car.length == 3:
			if state[i] - HEIGHT not in occupied and state[i] not in  range(6):
				bord[i] -= HEIGHT
				moveOptions.append(bord)
			if state[i] + 3*HEIGHT not in occupied and state[i] < 18:
				bord2[i] += HEIGHT
				moveOptions.append(bord2)
		i += 1

	return moveOptions

if __name__ == '__main__':
	main()
