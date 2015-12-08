class PathTracker:
    def __init__(self):
        self.path = []
        self.childCounts = []

    def push(self, node, childCount):
        self.path.append(node)
        self.childCounts.append(childCount)

    def pop(self):
    	self.path.pop()
        self.childCounts.pop()

    def decreaseChildCount(self):
        self.childCounts[-1] -= 1

    def childCountIsZero(self):
        return self.childCounts[-1] == 0

    def atRoot(self):
    	return self.path == []

    def goUpInTreeIfNeeded(self):
        while self.childCountIsZero():
            self.pop()
            # Stop if at the root
            if self.atRoot() :
                break
            self.decreaseChildCount()
