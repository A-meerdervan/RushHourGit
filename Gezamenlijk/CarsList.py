
class CarsList:
    def __init__(self):
        self.cars = []
        self.directionsList = []

    def getFirstState(self):
<<<<<<< HEAD
        firstState = []
        for car in self.cars:
            firstState.append(car.firstMainTile)
        return firstState
=======
    	firstState = []
    	for car in self.cars:
    		firstState.append(car.firstMainTile)
    	return firstState
>>>>>>> df5d95f6b4ea9a64b058599ace445313837de7c6

    def getDirectionsList(self):
        for cars in self.cars:
            self.directionsList.append(cars.isHorizontal)
        return self.directionsList
<<<<<<< HEAD
        
    def getVisualisationList(self):
        visualisationList = []
        for car in self.cars:
            tmpList = []
            tmpList.append(car.firstMainTile)
            tmpList.append(car.isHorizontal)
            tmpList.append(car.length)
            visualisationList.append(tmpList)
        return visualisationList
=======
>>>>>>> df5d95f6b4ea9a64b058599ace445313837de7c6
