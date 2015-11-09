class Tree(object):
    def __init__(self, width, carsOrientation):
        self.counter = 0
        self.root = Node()
        self.width = width
        self.tiles = width-1
        self.root.makeChildren(self.tiles)
        self.carsOrientation = carsOrientation

    def encryptState(self, orientation, state):
        self.encryptedState = []
        for positions in range(0, len(state)):
            if orientation[positions]:
                self.encryptedState.append(state[positions] % self.width)
            else:
                self.encryptedState.append(state[positions] / self.width)
        return self.encryptedState

    def addState(self, state, parentState):
        self.counter += 1
        self.state = self.encryptState(self.carsOrientation, state)
        self.pointer = self.root
        for cars in range(0, len(self.state)):
            if self.pointer.children[self.state[cars]].exist == False:
                self.pointer = self.pointer.children[self.state[cars]]
                self.pointer.exist = True
                if cars < len(self.state) - 2:
                    self.pointer.makeChildren(self.tiles)
                elif cars < len(self.state) - 1:
                    self.pointer.makeEndChildren(self.tiles)
                else:
                    self.pointer.setParentState(parentState)
            else:
                self.pointer = self.pointer.children[self.state[cars]]

    def checkState(self, state):
        self.state = self.encryptState(self.carsOrientation, state)
        self.pointer = self.root
        for cars in range(0, len(self.state)):
            if self.pointer.children[self.state[cars]].exist == False:
                return False
            else:
                self.pointer = self.pointer.children[self.state[cars]]
        return True

    def goToEndNode(self, state):
        self.state = self.encryptState(self.carsOrientation, state)
        self.pointer = self.root
        for cars in range(0, len(self.state)):
            self.pointer = self.pointer.children[self.state[cars]]
        return self.pointer

    def getPath(self, currentState):
        self.path = [currentState]
        self.tmpPath = []
        self.pointer = goToEndNode(currentState)
        while self.pointer.parentState != currentState:
            self.tmpPath.append(pointer.parentState)
            self.pointer = self.pointer.goToEndNode(pointer.parentState)
        self.path.append(self.tmpPath.reverse())
        return self.path

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
        self.children = []
        self.parentState = []

    def setParentState(self, parentState):
        self.parent = parentState
