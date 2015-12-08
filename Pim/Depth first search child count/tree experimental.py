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

    def addState(self, stateIn, depth, parentState):
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
                    self.goToEndNode(parentState).children.append(pointer)
            else:
                pointer = pointer.children[state[cars]]

    def checkState(self, stateIn, depth, parentState):
        state = self.encryptState(self.carsOrientation, stateIn)
        pointer = self.root
        for cars in range(0, len(state)):
            if pointer.children[state[cars]].exist == False:
                return False
            else:
                pointer = pointer.children[state[cars]]

        newDepth = depth
        archiveDepth = pointer.depth
        if archiveDepth > newDepth:
            self.adjustedDepth = newDepth
            statePointer = self.goToEndNode(stateIn)
            self.adjustDepth(statePointer)
        return True

    def adjustDepth(self, nodePointer):
        nodePointer.depth = self.adjustedDepth
        self.adjustedDepth += 1
        for childs in range(0, len(nodePointer.children)):
            self.adjustDepth(nodePointer.children[childs])
        self.adjustedDepth -= 1

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
        self.children = []
        self.depth = -1
