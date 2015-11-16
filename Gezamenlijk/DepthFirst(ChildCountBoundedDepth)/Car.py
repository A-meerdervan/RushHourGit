

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
