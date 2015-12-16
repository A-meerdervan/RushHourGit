

class Car:
    """

    """

    def __init__(self, MainCoordinate , isHorizontal , length):
        # Redirect output to a queue
        self.MainCoordinate = MainCoordinate
        self.isHorizontal = isHorizontal
        self.length = length
        self.Coordinates = []

        # self.createCoordinateList()

    def setMainCoordinate(self, NewMainCoordinate):
        self.MainCoordinate = NewMainCoordinate
        self.createCoordinateList()

        # transform a tile number to x, y coordinates of the car
    def getCoordinates(self, mainTileNumber, width):
        y = mainTileNumber/width
        x = mainTileNumber%width
        if self.isHorizontal:
            if self.length == 2 :
                return [ [x,y], [x + 1, y] ]
            # The car is 3 long
            else:
                return [ [x,y], [x + 1, y], [x + 2, y] ]
        # The car is vertical
        else:
            if self.length == 2:
                return [ [x,y], [x, y + 1]]
            else:
                return [ [x,y], [x, y +1], [x, y + 2] ]

    # def createCoordinateList(self):
    #     self.Coordinates = []
    #     self.Coordinates.append(self.MainCoordinate)
    #     if self.isHorizontal:
    #         for i in range(1, self.length):
    #             self.Coordinates.append([self.MainCoordinate[0] + i, self.MainCoordinate[1] ])                
    #     # if Vertical:
    #     else:
    #         for i in range(1, self.length):
    #             self.Coordinates.append([self.MainCoordinate[0], self.MainCoordinate[1] + i])


