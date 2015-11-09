
class Tree(object):
    def __init__(self, width, cars):
        self.root = Node()
        self.width = width
        self.tiles = width-1
        self.root.makeChildren(self.tiles)
        self.carsOrientation = []
        for car in cars:
            self.carsOrientation.append(car[2])

    def encryptState(self, orientation, state):
        self.encryptedState = []
        for positions in range(0, len(state)):
            if 'h' in orientation[positions] or 'x' in orientation[positions]:
                self.encryptedState.append(state[positions] % self.width)
            elif 'v' in orientation[positions] or 'y' in orientation[positions]:
                self.encryptedState.append(state[positions] / self.width)
        return self.encryptedState

    def addState(self, state):
        self.state = self.encryptState(self.carsOrientation, state)
        self.pointer = self.root
        for cars in range(0, len(self.state)):
            if self.pointer.children[self.state[cars]].exist == False:
                self.pointer = self.pointer.children[self.state[cars]]
                self.pointer.exist = True
                if cars < len(self.state) - 1:
                    self.pointer.makeChildren(self.tiles)
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

class Node(object):
    def __init__(self):
        self.exist = False
        self.children = []

    def makeChildren(self, children):
        for child in range(0, children):
            self.children.append(Node())
