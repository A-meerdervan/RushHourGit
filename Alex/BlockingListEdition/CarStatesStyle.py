

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
        self.Length = Length

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

