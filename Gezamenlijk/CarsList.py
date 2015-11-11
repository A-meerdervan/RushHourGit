
class CarsList:
    def __init__(self):
        self.cars = []
        self.directionsList = []

    def getFirstState(self):
    	firstState = []
    	for car in self.cars:
    		firstState.append(car.firstMainTile)
    	return firstState

    def getDirectionsList(self):
        for cars in self.cars:
            self.directionsList.append(cars.isHorizontal)
        return self.directionsList
