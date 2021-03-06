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

    def addState(self, stateIn, parentState, startDepth = -1):
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
                    if startDepth == -1:
                        depthInput = self.goToEndNode(parentState).depth + 1
                    else:
                        depthInput = startDepth
                    pointer.makeEndChildren(self.tiles, depthInput)
                else:
                    pointer.setParentState(parentState)
                    self.goToEndNode(parentState).children.append(pointer)
            else:
                pointer = pointer.children[state[cars]]

    def checkState(self, stateIn, parentState):
        state = self.encryptState(self.carsOrientation, stateIn)
        pointer = self.root
        for cars in range(0, len(state)):
            if pointer.children[state[cars]].exist == False:
                return False
            else:
                pointer = pointer.children[state[cars]]

        newDepth = self.goToEndNode(parentState).depth + 1
        currentDepth = pointer.depth
        if currentDepth > newDepth:
            self.adjustedDepth = newDepth
            statePointer = self.goToEndNode(stateIn)
            statePointer.parent = parentState
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
            print len(pointer.children)
            pointer = pointer.children[state[cars]]
        return pointer

    def getParent(self, stateIn):
        parent = self.goToEndNode(stateIn).parentState
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

    def makeEndChildren(self, children, parent, depth):
        for child in range(0, children):
            self.children.append(EndNode(depth, parent))

class EndNode(object):
    def __init__(self, parent, depth):
        self.exist = False
        self.children = []
        self.state = []
        self.parent = parent
        self.depth = depth
