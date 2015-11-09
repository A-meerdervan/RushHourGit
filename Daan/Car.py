

class Car:
    """
maintile is the tile with the closest path to the origin
isHorizontal is a booleyan that gives true if Horizontal and is vertical if not Horizontal
length is the length of a car
    """

    def __init__(self, mainTile , isHorizontal , length):
        # Redirect output to a queue
        self.firstMainTile = mainTile
        self.isHorizontal = isHorizontal
        self.length = length
