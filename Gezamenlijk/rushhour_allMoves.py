from Car import Car
from CarsList import CarsList
CARS_LIST = CarsList()
import copy
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
	state = [22,9,10,20]
	allMoves(state)
def allMoves(state):

	occupied =[]
	moveOptions = [] # needs to be an stack

	k = 0

	for car in CARS_LIST.cars: # moet een array zijn [20,22,9,10]

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
	print occupied
	#  ctrl d geeft select voor veranderen variabele
	# werkt niet er moet eerst nog een aparte variabele aangemaakt worden om de state niet te veranderen anders krijg je eeuwig linkende dingen en stuff kutzooi!.
	# werkt niet want na 1 auto moet het weer terug naar he begin
	i = 0
	bord = copy.deepcopy(state)
	bord2 = copy.deepcopy(state)
	print bord
	for car in CARS_LIST.cars:
		bord = copy.deepcopy(state)
		bord2 = copy.deepcopy(state)
		print car.isHorizontal
		if car.isHorizontal and car.length == 2 :
			if state[i] -1 not in occupied and state[0] not in range(0,36,6): # moet niet op een bezette tegel of buiten het bord belanden
				bord[i] -= 1
				moveOptions.append(bord)

				#moveOptions.insert(0,bord)
				#moveOptions[0][i] -= 1



				print 'hier'
				print moveOptions
			if state[i] + 2 not in occupied and state[i] not in range(4,40,6): # range om te kijken of de positie binnen het bereik van het bord is.
				print

				bord2[i] += 1
				moveOptions.append(bord2)

				print 'false'

		elif not car.isHorizontal and car.length == 2:
			if state[i] - WIDTH not in occupied  and state[i] not in  range(6):
				bord[i] -= WIDTH
				moveOptions.append(bord)
				#bord[i] =+ WIDTH
			if state[i] + 12 not in occupied and state[i] != range(24,30):
				bord2[i] += WIDTH
				moveOptions.append(bord2)
				#bord2[i] -= WIDTH

		elif car.isHorizontal and car.length == 3:
			if state[i] - 1 not in occupied and state[i] not in  range(0,36,6) :
				bord[i] -= 1
				moveOptions.append(bord)
				#bord[i] += 1
			if state[i] + 3 not in occupied and state[i] not in  range(3,39,6):
				bord2[i] += 1
				moveOptions.append(bord2)
				#bord[i] -= 1
		elif not car.isHorizontal and car.length == 3:
			if state[i] - HEIGHT not in occupied and state[i] not in  range(6):

				bord[i] -= HEIGHT

				moveOptions.append(bord)
				print moveOptions
				#bord[i] += HEIGHT

			if state[i] + 3*HEIGHT not in occupied and state[i] < 18:
				bord2[i] += HEIGHT
				moveOptions.append(bord2)
				#bord[i] -= HEIGHT
		i += 1
return moveOptions

if __name__ == '__main__':

	main()
