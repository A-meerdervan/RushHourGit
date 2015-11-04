
class Trie(object):
    def __init__(self, width):
        self.root = Node()
        self.tiles = width**2
        self.root.makeChildren(self.tiles)

    def addState(self, state):
        self.pointer = self.root
        for cars in range(0, len(state)):
            if self.pointer.children[state[cars]].exist == False:
                self.pointer = self.pointer.children[state[cars]]
                self.pointer.exist = True
                if cars < len(state) - 1:
                    self.pointer.makeChildren(self.tiles)
            else:
                self.pointer = self.pointer.children[state[cars]]

    def checkState(self, state):
        self.pointer = self.root
        for cars in range(0, len(state)):
            if self.pointer.children[state[cars]].exist == False:
                return False
            else:
                self.pointer = self.pointer.children[state[cars]]
        return True

class Node(object):
    def __init__(self):
        self.exist = False
        self.children = []

    def makeChildren(self, children):
        for child in range(0, children):
            self.children.append(Node())

if __name__ == '__main__':
    trie = Trie(3)
    trie.addState([1,1,1])
    trie.addState([0,1,2])
    trie.addState([2,2,0])
    trie.addState([2,0,0])
    print trie.checkState([1,1,1])
    print trie.checkState([2,2,0])
    print trie.checkState([0,1,0])
