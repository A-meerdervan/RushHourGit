
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
EXIT = 43 # LET OP !! 6x6=22 9x9=43 12x12 = 82
WIDTH = 9
HEIGHT = 9
CARS_LIST = CarsList()
INITIAL_STATE = []



def main():

	#6x6
	#game #1
	# RedCar = Car(21, True, 2)
	# Car1 = Car(0, False, 2)
	# Car2 = Car(7, True, 2)
	# Car3 = Car(3, False, 2)
	# Car4 = Car(4, True, 2)
	# Car5 = Car(16, True, 2)
	# Car6 = Car(33, True, 2)
	# Car7 = Car(20, False, 2)
	# Car8 = Car(23, False, 3)
	# state = [0,7,3,4,16,33,20,23,21] #add red car at last to minimize stack!
	# #game #2
	# RedCar = Car(20, True, 2)
	# Car1 = Car(0, False, 2)
	# Car2 = Car(12, True, 2)
	# Car3 = Car(3, False, 2)
	# Car4 = Car(4, True, 2)
	# Car5 = Car(10, True, 2)
	# Car6 = Car(14, True, 2)
	# Car7 = Car(16, False, 2)
	# Car8 = Car(17, False, 3)
	# Car9 = Car(25, True, 2)
	# Car10 = Car(27, True, 2)
	# Car11 = Car(32, True, 2)
	# Car12 = Car(34, True, 2)
	# state = [0,12,3,4,10,14,16,17,25,27,32,34,20]
	# #game #3
	# RedCar = Car(18, True, 2)
	# Car1 = Car(0, False, 2)
	# Car2 = Car(12, True, 2)
	# Car3 = Car(2, False, 2)
	# Car4 = Car(10, True, 2)
	# Car5 = Car(14, True, 2)
	# Car6 = Car(16, False, 2)
	# Car7 = Car(17, False, 3)
	# Car8 = Car(25, True, 2)
	# Car9 = Car(27, True, 2)
	# Car10 = Car(32, True, 2)
	# Car11 = Car(34, True, 2)
	# state = [0,12,2,10,14,16,17,25,27,32,34,18]
	#9x9
	#game #4
	# RedCar = Car(37, True, 2)
	# Car1 = Car(0, False, 2)
	# Car2 = Car(1, True, 3)
	# Car3 = Car(4, False, 2)
	# Car4 = Car(5, True, 2)
	# Car5 = Car(7, True, 2)
	# Car6 = Car(11, False, 3)
	# Car7 = Car(12, False, 2)
	# Car8 = Car(17, False, 3)
	# Car9 = Car(18, True, 2)
	# Car10 = Car(21, True, 2)
	# Car11 = Car(27, False, 2)
	# Car12 = Car(30, False, 2)
	# Car13 = Car(12, True, 3)
	# Car14 = Car(44, False, 3)
	# Car15 = Car(29, True, 2)
	# Car16 = Car(32, False, 3)
	# Car17 = Car(34, True, 3)
	# Car18 = Car(63, False, 2)
	# Car19 = Car(73, True, 3)
	# Car20 = Car(59, False, 3)
	# Car21 = Car(69, True, 3)
	# state = [0,1,4,5,7,11,12,17,18,21,27,30,12,44,29,32,34,63,73,59,69,37]
	#game #5
	# RedCar = Car(42, True, 2)
	# Car1 = Car(0, False, 2)
	# Car2 = Car(1, False, 2)
	# Car3 = Car(18, False, 2)
	# Car4 = Car(2, True, 2)
	# Car5 = Car(11, True, 2)
	# Car6 = Car(4, False, 2)
	# Car7 = Car(14, True, 3)
	# Car8 = Car(8, False, 2)
	# Car9 = Car(20, False, 2)
	# Car10 = Car(21, True, 2)
	# Car11 = Car(23, False, 3)
	# Car12 = Car(24, True, 2)
	# Car13 = Car(26, False, 3)
	# Car14 = Car(38, True, 3)
	# Car15 = Car(49, True, 2)
	# Car16 = Car(51, False, 2)
	# Car17 = Car(52, True, 2)
	# Car18 = Car(57, False, 3)
	# Car19 = Car(58, True, 2)
	# Car20 = Car(72, True, 3)
	# Car21 = Car(68, False, 2)
	# Car22 = Car(69, False, 2)
	# Car23 = Car(70, True, 2)
	# state = [0,1,18,2,11,4,14,8,20,21,23,24,26,38,49,51,52,57,58,72,68,69,70,42]
	# #game #6
	RedCar = Car(36, True, 2)
	Car1 = Car(0, False, 3)
	Car2 = Car(1, True, 3)
	Car3 = Car(4, False, 3)
	Car4 = Car(11, True, 2)
	Car5 = Car(14, True, 2)
	Car6 = Car(17, False,3)
	Car7 = Car(19, False, 2)
	Car8 = Car(20, True, 2)
	Car9 = Car(23, True, 3)
	Car10 = Car(30, False, 3)
	Car11 = Car(31, True, 2)
	Car12 = Car(33, True, 2)
	Car13 = Car(38, False, 2)
	Car14 = Car(49, False, 2)
	Car15 = Car(50, False, 2)
	Car16 = Car(51, True, 3)
	Car17 = Car(54, False, 2)
	Car18 = Car(56, True, 2)
	Car19 = Car(61, True, 2)
	Car20 = Car(64, True, 3)
	Car21 = Car(67, False, 2)
	Car22 = Car(68,True, 2)
	Car23 = Car(70, False, 2)
	Car24 = Car(72,True,2)
	Car24 = Car(74,True,2)
	state = [0,1,4,11,14,17,19,20,23,30,31,33,38,49,50,51,54,56,61,64,67,68,70,72,74,36]
	# #12x12 #7
	# RedCar = Car(74, True, 2)
	# Car1 = Car(1, True, 2)
	# Car2 = Car(3, True, 3)
	# Car3 = Car(6, False, 3)
	# Car4 = Car(7, True, 2)
	# Car5 = Car(9, False, 2)
	# Car6 = Car(10, False,3)
	# Car7 = Car(11, False, 2)
	# Car8 = Car(26, False, 2)
	# Car9 = Car(27, True, 3)
	# Car10 = Car(32, True, 2)
	# Car11 = Car(35, False, 2)
	# Car12 = Car(36, True, 2)
	# Car13 = Car(39, True, 3)
	# Car14 = Car(42, False, 3)
	# Car15 = Car(43, True, 3)
	# Car16 = Car(48, True, 3)
	# Car17 = Car(51, False, 2)
	# Car18 = Car(52, True, 2)
	# Car19 = Car(55,False, 2)
	# Car20 = Car(57, False, 2)
	# Car21 = Car(58, True, 2)
	# Car22 = Car(60,True, 3)
	# Car23 = Car(64, False, 2)
	# Car24 = Car(65,False,2)
	# Car25 = Car(70, True,2)
	# Car26 = Car(72, False, 3)
	# Car27 = Car(73, False, 3)
	# Car28 = Car(86, True, 3)
	# Car29 = Car(89, False, 2)
	# Car30 = Car(90, False,3)
	# Car31 = Car(91, True, 3)
	# Car32 = Car(103, True, 2)
	# Car33 = Car(105, True, 2)
	# Car34 = Car(108, True, 3)
	# Car35 = Car(111, True, 2)
	# Car36 = Car(113, False, 2)
	# Car37 = Car(115, True, 2)
	# Car38 = Car(118, False, 2)
	# Car39 = Car(119, False, 2)
	# Car40 = Car(120, False, 2)
	# Car41 = Car(126, False, 2)
	# Car42 = Car(139, True, 3)
	# Car43 = Car(142, True, 2)
	# state = [1,3,6,7,9,10,11,26,27,32,35,36,39,42,43,48,51,52,55,57,58,60,64,65,70,72,73,86,
	# 89,90,91,103,105,108,111,113,115,118,119,120,126,139,142]

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
	CARS_LIST.cars.append(Car13)
	CARS_LIST.cars.append(Car14)
	CARS_LIST.cars.append(Car15)
	CARS_LIST.cars.append(Car16)
	CARS_LIST.cars.append(Car17)
	CARS_LIST.cars.append(Car18)
	CARS_LIST.cars.append(Car19)
	CARS_LIST.cars.append(Car20)
	CARS_LIST.cars.append(Car21)
	CARS_LIST.cars.append(Car22)
	CARS_LIST.cars.append(Car23)
	CARS_LIST.cars.append(Car24)
	# CARS_LIST.cars.append(Car25)
	# CARS_LIST.cars.append(Car26)
	# CARS_LIST.cars.append(Car27)
	# CARS_LIST.cars.append(Car28)
	# CARS_LIST.cars.append(Car29)
	# CARS_LIST.cars.append(Car30)
	# CARS_LIST.cars.append(Car31)
	# CARS_LIST.cars.append(Car32)
	# CARS_LIST.cars.append(Car33)
	# CARS_LIST.cars.append(Car34)
	# CARS_LIST.cars.append(Car35)
	# CARS_LIST.cars.append(Car36)
	# CARS_LIST.cars.append(Car37)
	# CARS_LIST.cars.append(Car38)
	# CARS_LIST.cars.append(Car39)
	# CARS_LIST.cars.append(Car40)
	# CARS_LIST.cars.append(Car41)
	# CARS_LIST.cars.append(Car42)
	# CARS_LIST.cars.append(Car43)
	CARS_LIST.cars.append(RedCar)

	global INITIAL_STATE; INITIAL_STATE = CARS_LIST.getFirstState()
	global STATES_ARCHIVE; STATES_ARCHIVE = Tree(WIDTH, CARS_LIST.getDirectionsList())

	algorithm(INITIAL_STATE)
	
	# Print some results

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
				print "lq:" , len(queue)
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
