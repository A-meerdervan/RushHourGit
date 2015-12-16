

class Car:
    """
maintile is the tile with the closest path to the origin
isHorizontal is a booleyan that gives true if Horizontal and is vertical if not Horizontal
length is the length of a car
    """

    def __init__(self, firstMainTile , isHorizontal , Length):
        # Redirect output to a queue
        self.firstMainTile = firstMainTile
        self.isHorizontal = isHorizontal
        self.length = Length
        self.mainCoordinate = [0,0]

    def getTileNumbers(self, mainTileNumber, width):
    	# this function is used to check wheter a car is in the way of the red car,
    	# a horizontal car is never in the way
    	if self.isHorizontal:
    		return []
    		# if self.length == 2:
    		# 	return [mainTileNumber, mainTileNumber + 1]
    		# else:
    		# 	return [mainTileNumber, mainTileNumber + 1, mainTileNumber + 2]
    	# The car is Vertical
    	else:
    		if self.length == 2:
    			return [mainTileNumber, mainTileNumber + width]
    		else:
    			return [mainTileNumber, mainTileNumber + width, mainTileNumber + 2*width]

    def getCoordinates(self, mainTileNumber, width):
        y = mainTileNumber/width
        x = mainTileNumber%width
        self.mainCoordinate[0] = x
        self.mainCoordinate[1] = y
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

