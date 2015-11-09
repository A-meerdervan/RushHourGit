from Car import Car
from CarsList import CarsList
CARS_LIST = CarsList()

WIDTH = 6
HEIGHT = 6
def main():

	# TEST met Daans allMoves functie
	RedCar = Car(20, True, 2)
	Car1 = Car(22, False, 3)
	Car2 = Car(9, False, 2)
	Car3 = Car(10, True, 2)

	CARS_LIST.cars.append(Car1)
	CARS_LIST.cars.append(Car2)
	CARS_LIST.cars.append(Car3)
	CARS_LIST.cars.append(RedCar)
	state = [20,22,9,10]
	allMoves(state)
def allmoves(state):

	occupied =[]
	moveOptions = [] # needs to be an stack

	print 'hier'
	k = 0
	for car in CARS_LIST.cars: # moet een array zijn [20,22,9,10]
		print car.isHorizontal
		print 'hier'
		if car.isHorizontal and car.length == 2 : # moet niet car[1] maar een link naar de class zijn
			occupied.append(state[k])
			occupied.append(state[k]+1)
		elif not car.isHorizontal and car.length == 2:
			occupied.append(state[k])
			occupied.append(state[k]+WIDTH)
		# The car is 3 long and horizontal:
		elif car.isHorizontal == 'h':
			occupied.append(state[k])
			occupied.append(state[k]+WIDTH)
			occupied.append(state[k]+WIDTH*2)
		# The car is 3 long and veritcal:
		else:
			occupied.append(state[k])
			occupied.append(state[k]+HEIGHT)
			occupied.append(state[k]+HEIGHT*2)
	k += 1
	print occupied

	i = 0
	print 'hier'
	for car in CARS_LIST.cars:
		print car.isHorizontal
		if car.isHorizontal and car.length == 2 :
			if state[i] -1 not in occupied and state[0] not in range(0,36,6): # moet niet op een bezette tegel of buiten het bord belanden
				state[i] -= 1
				moveOptions.append(state)

				#moveOptions.insert(0,state)
				#moveOptions[0][i] -= 1


				state[i] += 1
				print 'hier'
				print moveOptions
			if state[i] + 2 not in occupied and state[i] not in range(4,40,6): # range om te kijken of de positie binnen het bereik van het bord is.
				print
				state[i] += 1
				moveOptions.append(state)

				print 'false'

		elif not car.isHorizontal and car.length == 2:
			if state[i] - WIDTH not in occupied  and state[i] not in  range(6):
				state[i] -= WIDTH
				moveOptions.append(state)
				state[i] =+ WIDTH
			if state[i] + 12 not in occupied and state[i] != range(24,30):
				state[i] += WIDTH
				moveOptions.append(state)
				state[i] -= WIDTH

		elif car.isHorizontal and car.length == 3:
			if state[i] - 1 not in occupied and state[i] not in  range(0,36,6) :
				state[i] -= 1
				moveOptions.append(state)
				state[i] += 1
			if state[i] + 3 not in occupied and state[i] not in  range(3,39,6):
				state[i] += 1
				moveOptions.append(state)
				state[i] -= 1
		elif not car.isHorizontal and car.length == 3:
			if state[i] - HEIGHT not in occupied and state[i] not in  range(6):
				print 'ga hierin'
				state[i] -= HEIGHT
				moveOptions.append(state)
				state[i] += HEIGHT
			if state[i] + 3*HEIGHT not in occupied and state[i] < 18:
				state[i] += HEIGHT
				moveOptions.append(state)
				state[i] -= HEIGHT
		print moveOptions
		i += 1
	print moveOptions
	print 'hello'
# crap
	# stateList = []
	# startState = []
	# for cars in carsList:
	#         startState.append(cars[0]+cars[1]*6)

	# stateList.append(startState)
	# stateList.append([19,22,9,10])
	# stateList.append([19,22,15,10])
	# stateList.append([19,22,21,10])
	# stateList.append([19,22,27,10])
	# stateList.append([19,22,27,9])
	# stateList.append([19,22,27,8])
	# stateList.append([19,16,27,8])
	# stateList.append([19,10,27,8])
	# stateList.append([19,4,27,8])
	# stateList.append([20,4,27,8])
	# stateList.append([21,4,27,8])
	# stateList.append([22,4,27,8])

	#print stateList

if __name__ == '__main__':

	allmoves()
