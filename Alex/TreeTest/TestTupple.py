
from CarsList import CarsList
from tree import Tree
from Car import Car
from allBords import *
import copy
import Queue
from random import randint

INITIAL_STATE = []
WIDTH = 0
EXIT = 0
CARS_LIST = CarsList()


def main():
	bordVariables = bord(2) # return [carsList,width,exit]
	global WIDTH; WIDTH = bordVariables[1]
	global CARS_LIST; CARS_LIST = bordVariables[0]
	global INITIAL_STATE; INITIAL_STATE = CARS_LIST.getFirstState()
	global STATES_ARCHIVE; STATES_ARCHIVE = dict()

	aantalCars = len(CARS_LIST.cars)
	# voeg vaak een state toe aan de tree
	for i in range(0, 100000):
		randomState = []
		randomStateTupple = ()
		for j in range(0, aantalCars):
			randomState.append(randint(0,WIDTH-2)*WIDTH + randint(0,WIDTH - 2))
			randomStateTupple = randomStateTupple + (randint(0,WIDTH-2)*WIDTH + randint(0,WIDTH - 2) , )
		# print randomState
		STATES_ARCHIVE[randomStateTupple] = [randomState, INITIAL_STATE]

	print "ik ben klaar met states toevoegen"

	# zoek een state in de tree
	for i in range(0, 100000):
		randomStateTupple = ()
		for j in range(0, aantalCars):
			randomStateTupple = randomStateTupple + (randint(0,WIDTH-2)*WIDTH + randint(0,WIDTH - 2) , )
		checkState(randomStateTupple)
	print "klaar met states checken"


def checkState(state):
	# check if key in dictionairy
	return state in STATES_ARCHIVE









if __name__ == '__main__':
	main()
