
class CarsList:
    def __init__(self):
        self.cars = []

    def getFirstState(self):
    	firstState = []
    	for car in self.cars:
    		firstState.append(car.firstMainTile)
    	return firstState
