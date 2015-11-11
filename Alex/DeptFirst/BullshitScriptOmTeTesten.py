
from CarsList import CarsList 
from Car import Car 

carsList = Car(12, True, 4)

def ewa():
	carsList.cars.append(Car(13,True, 5))
	print carsList.cars[0].FirstMainTile
def fallaG():
	print carsList.cars[0].FirstMainTile

def main():
	global carsList; carsList = CarsList()
	ewa()
	fallaG()

if __name__ == '__main__':
	main()