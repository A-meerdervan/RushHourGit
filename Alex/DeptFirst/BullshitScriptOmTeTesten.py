import CarsList from CarsList
import Car from Car

carsList = CarsList()

def ewa():
	RedCar = Car(20, True, 2)
	Car1 = Car(22, False, 3)
	carsList.cars.append(RedCar)
	carsList.cars.append(Car1)
	return True

if False or ewa():
	print "yolo"