
from random import randint


def main():

	# voeg vaak een state toe aan de tree
	for i in range(0, 8000000):
		randomState = []
		for j in range(0, 20):
			randomState.append(randint(0, 20))

	print "ik ben klaar met states toevoegen"



if __name__ == '__main__':
	main()
