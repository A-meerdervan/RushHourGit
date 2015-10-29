

class Car:
    """

    """

    def createCoordinateList(self):
        self.Coordinates.append(self.MainCoordinate)
        if self.Direction == "Vertical":
            for i in range(1, self.Length):
                self.Coordinates.append([self.MainCoordinate[0], self.MainCoordinate[1] + i])
        elif self.Direction == "Horizontal":
            for i in range(1, self.Length):
                self.Coordinates.append([self.MainCoordinate[0] + i, self.MainCoordinate[1] ])                
        else:
            print "ERROR:   De richting van de auto was niet Vertical noch Horizontal"        


    def __init__(self, MainCoordinate , Direction , Length, Number ):
        # Redirect output to a queue
        self.MainCoordinate = MainCoordinate
        self.Direction = Direction
        self.Number = Number
        self.Length = Length
        self.Coordinates = []
        
        self.createCoordinateList()


    



