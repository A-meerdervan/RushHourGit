
from CarsList import CarsList 
from Car import Car 

carsList = CarsList()

def ewa():
	RedCar = Car(20, True, 2)
	Car1 = Car(22, False, 3)
	carsList.cars.append(RedCar)
	carsList.cars.append(Car1)
	print carsList.cars[1].isHorizontal

if False or ewa():
	print "yolo"