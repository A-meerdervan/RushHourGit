from Car import Car
from CarsList import CarsList
CARS_LIST = CarsList()
import copy
WIDTH = 6
HEIGHT = 6
EXIT = 22 # LET OP !! 6x6=22 9x9=43 12x12 = 82
def main():
	# de EXIT kan niet gehardcode worden dus moet voor 6*6 9*9 en 12*12 apart gedefineerd worden
	# TEST met Daans allMoves functie
	#6x6
	#game #1
	RedCar = Car(21, True, 2)
	Car1 = Car(0, False, 2)
	Car2 = Car(7, True, 2)
	Car3 = Car(3, False, 2)
	Car4 = Car(4, True, 2)
	Car5 = Car(16, True, 2)
	Car6 = Car(33, True, 2)
	Car7 = Car(20, False, 2)
	Car8 = Car(23, False, 3)
	#game #2
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
	#game #3
	RedCar = Car(18, True, 2)
	Car1 = Car(0, False, 2)
	Car2 = Car(12, True, 2)
	Car3 = Car(2, False, 2)
	Car4 = Car(10, True, 2)
	Car5 = Car(14, True, 2)
	Car6 = Car(16, False, 2)
	Car7 = Car(17, False, 3)
	Car8 = Car(25, True, 2)
	Car9 = Car(27, True, 2)
	Car10 = Car(32, True, 2)
	Car11 = Car(34, True, 2)

	#9x9
	#game #4
	RedCar = Car(37, True, 2)
	Car1 = Car(0, False, 2)
	Car2 = Car(1, True, 3)
	Car3 = Car(4, False, 2)
	Car4 = Car(5, True, 2)
	Car5 = Car(7, True, 2)
	Car6 = Car(11, False, 3)
	Car7 = Car(12, False, 2)
	Car8 = Car(17, False, 3)
	Car9 = Car(18, True, 2)
	Car10 = Car(21, True, 2)
	Car11 = Car(27, False, 2)
	Car12 = Car(30, False, 2)
	Car13 = Car(12, True, 3)
	Car14 = Car(44, False, 3)
	Car15 = Car(29, True, 2)
	Car16 = Car(32, False, 3)
	Car17 = Car(34, True, 3)
	Car14 = Car(63, False, 2)
	Car15 = Car(73, True, 3)
	Car16 = Car(59, False, 3)
	Car17 = Car(69, True, 3)
	#game #5
	RedCar = Car(42, True, 2)
	Car1 = Car(0, False, 2)
	Car2 = Car(1, False, 2)
	Car3 = Car(18, False, 2)
	Car4 = Car(2, True, 2)
	Car5 = Car(11, True, 2)
	Car6 = Car(4, False, 2)
	Car7 = Car(14, True, 3)
	Car8 = Car(8, False, 2)
	Car9 = Car(20, False, 2)
	Car10 = Car(21, True, 2)
	Car11 = Car(23, False, 3)
	Car12 = Car(24, True, 2)
	Car13 = Car(26, False, 3)
	Car14 = Car(38, True, 3)
	Car15 = Car(49, True, 2)
	Car16 = Car(51, False, 2)
	Car17 = Car(52, True, 2)
	Car18 = Car(57, False, 3)
	Car19 = Car(58, True, 2)
	Car20 = Car(72, True, 3)
	Car21 = Car(68, False, 2)
	Car22 = Car(69, False, 2)
	Car23 = Car(70, True, 2)
	#game #6
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
	#12x12 #7

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
	state = [0,12,3,4,10,14,16,17,25,27,32,34,20]
	# Car1 = Car(18,True,2)
	# Car2 = Car(9,False,2)
	# CARS_LIST.cars.append(Car2)
	# CARS_LIST.cars.append(Car1)
	# state = [9,18]
	allMoves(state)
	occupiedo = getOccupiedTiles(state)
	# optionIsSolution(state,occupiedo)

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
	bord = copy.deepcopy(state)
	bord2 = copy.deepcopy(state)
	occupied = getOccupiedTiles(state)

	for car in CARS_LIST.cars:
		bord = copy.deepcopy(state)
		bord2 = copy.deepcopy(state)

		if car.isHorizontal and car.length == 2 :
			if state[i] -1 not in occupied and state[i] not in range(0,WIDTH*WIDTH,WIDTH): # moet niet op een bezette tegel of buiten het bord belanden
				bord[i] -= 1
				moveOptions.append(bord)
			if state[i] + 2 not in occupied and state[i] not in range(WIDTH-2,(WIDTH*WIDTH+WIDTH-2),WIDTH): # range om te kijken of de positie binnen het bereik van het bord is.
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
	print moveOptions


def optionIsSolution(state,occupied):
	#checkt nog te veel maar Alex zeurt
	# print occupied
	arraycounter =[]
	counter = 1
	# print state[-1]
	while state[-1] < EXIT:
		counter += 1
		arraycounter.append(counter)
		state[-1] += 1
	state[-1] = state[-1] - counter + 1
	# print arraycounter

	for number in arraycounter:
		# print number,state[-1]
		tileCheck = state[-1] + number
		# print tileCheck
		if tileCheck in occupied:
			#print 'false'
			return False
	#print 'hier'
	return True

if __name__ == '__main__':

	main()
