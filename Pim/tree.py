class Tree(object):
    def __init__(self, width, carsOrientation):
        self.counter = 0
        self.root = Node()
        self.width = width
        self.tiles = width-1
        self.root.makeChildren(self.tiles)
        self.carsOrientation = carsOrientation

    def encryptState(self, orientation, state):
        encryptedState = []
        for positions in range(0, len(state)):
            if orientation[positions]:
                encryptedState.append(state[positions] % self.width)
            else:
                encryptedState.append(state[positions] / self.width)
        return encryptedState

    def addState(self, state, parentState):
        self.counter += 1
        # print self.counter
        state = self.encryptState(self.carsOrientation, state)
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
                    pointer.setParentState(parentState)
            else:
                pointer = pointer.children[state[cars]]

    def checkState(self, state):
        # print 'self cars orient', self.carsOrientation
        # print 'state before adaptation', state
        state = self.encryptState(self.carsOrientation, state)
        pointer = self.root
        # print 'len state:', len(self.state)
        # print 'state:', self.state
        # print 'children len:', len(self.pointer.children)
        for cars in range(0, len(state)):
            if pointer.children[state[cars]].exist == False:
                return False
            else:
                pointer = pointer.children[state[cars]]
        return True

    def goToEndNode(self, state):
        state = self.encryptState(self.carsOrientation, state)
        pointer = self.root
        for cars in range(0, len(state)):
            pointer = pointer.children[state[cars]]
        return pointer

    def getParent(self, state):
        parent = self.goToEndNode(state).parentState
        return parent

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
