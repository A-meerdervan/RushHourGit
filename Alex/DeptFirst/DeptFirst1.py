
from Stack import Stack

# this contains the state and it's parent state like:
# [state, parentState]
STATES_ARCHIVE = []
# this contains the solution state and it's parent state like:
# [state, parentState]
SOLUTIONS = []
# This contains the path to the solution backwards. 
SOLUTION_PATHS = []
CARS_LIST = []


def main():
	# TEST dept first algorithme:

	initialState = 10
	algorithm(initialState)
	# print results
	print SOLUTIONS
	print SOLUTION_PATHS
	print STATES_ARCHIVE

	# TEST met Daans allMoves functie
	RedCar = [20, 'h', 2, 'red']
	Car1 = [22, 'v', 3, 'yellow']
	Car2 = [9, 'v', 2, 'green']
	Car3 = [10, 'h', 2, 'orange']
	
	CARS_LIST.append(RedCar)
	CARS_LIST.append(Car1)
	CARS_LIST.append(Car2)
	CARS_LIST.append(Car3)

	allMovesCopy()

def algorithm(initialState):
	stack = Stack()
	# add first state
	stack.push(initialState)
	STATES_ARCHIVE.append([initialState, 0])
	# loop all possible moves
	count = 0
	while stack.isNotEmpty():
		count += 1
		option = stack.pop();
		# Loop all options and (conditionaly) store them on the stack to revisit later
		for newOption in allMoves(option):
			# Stop the loop if option is a repeat or the solution
			if optionIsNotNew(newOption):
				continue
			elif optionIsSolution(newOption):
				SOLUTIONS.append([newOption, option])
				continue
			else:
				# add the option to the stack for later evaluation
				stack.push(newOption)
				# add the option to the states archive
				STATES_ARCHIVE.append([newOption, option])
	getSolutionPaths()

def getSolutionPaths():
	for solution in SOLUTIONS:
		path = [solution[0]]
		parent = solution[1]
		notAtRoot = True
		# find the parent of the parent until the root is reached
		while notAtRoot:
			#find parent state
			for state in STATES_ARCHIVE:
				if state[0] == parent: 
					path.append(parent)
					if state[1] == 0:
						notAtRoot = False
					parent = state[1]
					break
		SOLUTION_PATHS.append(path)

#recursive version (not used because memory will run out faster)
def dfs(option):
	#count = count + 1
	# Stop the loop if option is a repeat or the solution
	print option
	if optionIsNotNew(option):
		return
	if optionIsSolution(option):
		SOLUTIONS.append(option)
		return
	# add option to statelist
	STATES_ARCHIVE.append(option)
	# Loop all options while recusevely going deeper in 
	# the "tree" of possibilities
	for newOption in allMoves(option):
		dfs(newOption)

def allMoves(option):
	return [option +1, option - 1]
	
def optionIsNotNew(option):
	# kijk in de tree van Pim
	# BS:
	for state in STATES_ARCHIVE:
		if state[0] == option: 
			return True
	return False


def optionIsSolution(option):
	# Verzin hier iets voor, gewoon als alle dingen van rode auto tot uitgang
	# vrij zijn. 
	if option in [8,13]:
		return True
	return False

def allMovesCopy():


	occupied =[]
	moveOptions = [] # needs to be an stack
	for car in CARS_LIST: # moet een array zijn [20,22,9,10]
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
	print CARS_LIST[0][1] #yoo dit geeft mij de richting niet carslist[0].direction??
	# moet mijn input [20,22,9,10] zijn of word dit iets anders? Ik kijk er morgen ook nog naar
	i = 0
	for car in CARS_LIST:
		print car

		state = car
		if car[1] == 'h' and car[2] == 2 :
			if car[0] -1 not in occupied and car[0] not in range(0,36,6): # moet niet op een bezette tegel of buiten het bord belanden

				CARS_LIST[i][0] -= 1
				moveOptions.append([CARS_LIST[0][0],CARS_LIST[1][0],CARS_LIST[2][0],CARS_LIST[3][0]]) # moet een stack zijn :D kijk stack.py weet niet of dat goed is
				CARS_LIST[i][0] += 1
				print 'hier'
				print moveOptions
			if car[0] + 2 not in occupied and car[0] not in range(4,40,6): # range om te kijken of de positie binnen het bereik van het bord is.
				print car[0]
				CARS_LIST[i][0] += 1
				moveOptions.append([CARS_LIST[i][0],CARS_LIST[1][0],CARS_LIST[2][0],CARS_LIST[3][0]])
				print 'false'

		elif car[1] == 'v' and car[2] == 2:
			if car[0] - 6 not in occupied  and car[0] not in  range(6):
				car[0] -= 6
				moveOptions.append([CARS_LIST[0][0],CARS_LIST[1][0],CARS_LIST[2][0],CARS_LIST[3][0]])

			if car[0] + 12 not in occupied == False and car[0] != range(24,30):
				car[0] += 6
				moveOptions.append([CARS_LIST[0][0],CARS_LIST[1][0],CARS_LIST[2][0],CARS_LIST[3][0]])

		elif car[1] == 'h' and car[2] == 3:
			if car[0] - 1 not in occupied and car[0] not in  range(0,36,6) :
				car[0] -= 1
			if car[0] + 3 not in occupied and car[0] not in  range(3,39,6):
				car[0] += 1
		elif car[1] == 'v' and car[2] == 3:
			if car[0] -6 not in occupied and car[0] not in  range(6):
				print 'ga hierin'
				CARS_LIST[i][0] -= 6
				moveOptions.append([CARS_LIST[0][0],CARS_LIST[1][0],CARS_LIST[2][0],CARS_LIST[3][0]])
				CARS_LIST[i][0] += 6
			if car[0] + 18 not in occupied and car[0] < 18:
				CARS_LIST[i][0] += 6
				moveOptions.append([CARS_LIST[0][0],CARS_LIST[1][0],CARS_LIST[2][0],CARS_LIST[3][0]])
				CARS_LIST[i][0] -= 6
		print moveOptions
		i += 1
	print moveOptions
	return moveOptions
	
if __name__ == '__main__':
	main()
	allMovesCopy()