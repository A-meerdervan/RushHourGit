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
        # print self.counter
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
        # print 'self cars orient', self.carsOrientation
        # print 'state before adaptation', state
        self.state = self.encryptState(self.carsOrientation, state)
        self.pointer = self.root
        # print 'len state:', len(self.state)
        # print 'state:', self.state
        # print 'children len:', len(self.pointer.children)
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

    def getParent(self, state):
        self.parent = self.goToEndNode(state).parentState
        return self.parent

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
        self.parentState = parentState
