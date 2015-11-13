from Car import Car
from CarsList import CarsList
CARS_LIST = CarsList()
import copy
WIDTH = 6
HEIGHT = 6
def main():

	# TEST met Daans allMoves functie
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

def optionIsSolution(state,occupied):
	#checkt nog te veel maar Alex zeurt
	# print occupied
	arraycounter =[]
	EXIT = 22
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
