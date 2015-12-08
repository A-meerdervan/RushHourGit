class Tree(object):
    def __init__(self, width, carsOrientation):
        self.counter = 0
        self.root = Node()
        self.width = width
        self.tiles = width-1
        self.root.makeChildren(self.tiles)
        self.carsOrientation = carsOrientation
        self.adjustedDepth = -1

    def encryptState(self, orientation, state):
        encryptedState = []
        for positions in range(0, len(state)):
            if orientation[positions]:
                encryptedState.append(state[positions] % self.width)
            else:
                encryptedState.append(state[positions] / self.width)
        return encryptedState

    def addState(self, stateIn, depth):
        self.counter += 1
        state = self.encryptState(self.carsOrientation, stateIn)
        pointer = self.root
        for cars in range(0, len(state)):
            if pointer.children[state[cars]].exist == False:
                pointer = pointer.children[state[cars]]
                pointer.exist = True
                if cars < len(state) - 2:
                    pointer.makeChildren(self.tiles)
                elif cars < len(state) - 1:
                    pointer.makeEndChildren(self.tiles)
                else:
                    pointer.depth = depth
            else:
                pointer = pointer.children[state[cars]]

    def checkState(self, stateIn, depth):
        state = self.encryptState(self.carsOrientation, stateIn)
        pointer = self.root
        for cars in range(0, len(state)):
            if pointer.children[state[cars]].exist == False:
                return False
            else:
                pointer = pointer.children[state[cars]]

        if pointer.depth > depth:
            pointer.depth = depth
        return True

    def goToEndNode(self, stateIn):
        state = self.encryptState(self.carsOrientation, stateIn)
        pointer = self.root
        for cars in range(0, len(state)):
            pointer = pointer.children[state[cars]]
        return pointer

    def lengthArchive(self):
        return self.counter

class Node(object):
    def __init__(self):
        self.exist = False
        self.children = []

    def makeChildren(self, children):
        for child in range(0, children):
            self.children.append(Node())

    def makeEndChildren(self, children):
        for child in range(0, children):
            self.children.append(EndNode())

class EndNode(object):
    def __init__(self):
        self.exist = False
        self.depth = -1
