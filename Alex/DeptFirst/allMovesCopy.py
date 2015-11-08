
#from Car import Car


def allmoves():
	RedCar = [20, 'h', 2, 'red']
	Car1 = [22, 'v', 3, 'yellow']
	Car2 = [9, 'v', 2, 'green']
	Car3 = [10, 'h', 2, 'orange']
	carsList = []
	carsList.append(RedCar)
	carsList.append(Car1)
	carsList.append(Car2)
	carsList.append(Car3)

	occupied =[]
	moveOptions = [] # needs to be an stack
	for car in carsList: # moet een array zijn [20,22,9,10]
		if car[1] == 'h' and car[2] == 2 : # moet niet car[1] maar een link naar de class zijn
			occupied.append(car[0])
			occupied.append(car[0]+1)
		elif car[1] == 'v' and car[2] == 2:
			occupied.append(car[0])
			occupied.append(car[0]+6)
		elif car[1] == 'h':
			occupied.append(car[0])
			occupied.append(car[0]+6)
			occupied.append(car[0]+12)
		else:
			occupied.append(car[0])
			occupied.append(car[0]+6)
			occupied.append(car[0]+12)

	print occupied
	print carsList[0][1] #yoo dit geeft mij de richting niet carslist[0].direction??
	# moet mijn input [20,22,9,10] zijn of word dit iets anders? Ik kijk er morgen ook nog naar
	i = 0
	for car in carsList:
		print car

		state = car
		if car[1] == 'h' and car[2] == 2 :
			if car[0] -1 not in occupied and car[0] not in range(0,36,6): # moet niet op een bezette tegel of buiten het bord belanden

				carsList[i][0] -= 1
				moveOptions.append([carsList[0][0],carsList[1][0],carsList[2][0],carsList[3][0]]) # moet een stack zijn :D kijk stack.py weet niet of dat goed is
				carsList[i][0] += 1
				print 'hier'
				print moveOptions
			if car[0] + 2 not in occupied and car[0] not in range(4,40,6): # range om te kijken of de positie binnen het bereik van het bord is.
				print car[0]
				carsList[i][0] += 1
				moveOptions.append([carsList[i][0],carsList[1][0],carsList[2][0],carsList[3][0]])
				print 'false'

		elif car[1] == 'v' and car[2] == 2:
			if car[0] - 6 not in occupied  and car[0] not in  range(6):
				car[0] -= 6
				moveOptions.append([carsList[0][0],carsList[1][0],carsList[2][0],carsList[3][0]])

			if car[0] + 12 not in occupied == False and car[0] != range(24,30):
				car[0] += 6
				moveOptions.append([carsList[0][0],carsList[1][0],carsList[2][0],carsList[3][0]])

		elif car[1] == 'h' and car[2] == 3:
			if car[0] - 1 not in occupied and car[0] not in  range(0,36,6) :
				car[0] -= 1
			if car[0] + 3 not in occupied and car[0] not in  range(3,39,6):
				car[0] += 1
		elif car[1] == 'v' and car[2] == 3:
			if car[0] -6 not in occupied and car[0] not in  range(6):
				print 'ga hierin'
				carsList[i][0] -= 6
				moveOptions.append([carsList[0][0],carsList[1][0],carsList[2][0],carsList[3][0]])
				carsList[i][0] += 6
			if car[0] + 18 not in occupied and car[0] < 18:
				carsList[i][0] += 6
				moveOptions.append([carsList[0][0],carsList[1][0],carsList[2][0],carsList[3][0]])
				carsList[i][0] -= 6
		print moveOptions
		i += 1
	print moveOptions
	print 'hello'
# # crap
# 	stateList = []
# 	startState = []
# 	for cars in carsList:
# 	        startState.append(cars[0]+cars[1]*6)

# 	stateList.append(startState)
# 	stateList.append([19,22,9,10])
# 	stateList.append([19,22,15,10])
# 	stateList.append([19,22,21,10])
# 	stateList.append([19,22,27,10])
# 	stateList.append([19,22,27,9])
# 	stateList.append([19,22,27,8])
# 	stateList.append([19,16,27,8])
# 	stateList.append([19,10,27,8])
# 	stateList.append([19,4,27,8])
# 	stateList.append([20,4,27,8])
# 	stateList.append([21,4,27,8])
# 	stateList.append([22,4,27,8])

# 	print stateList

if __name__ == '__main__':

	allmoves()
