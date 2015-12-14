from operator import itemgetter

class PriorityStack:
    def __init__(self):
        self.items = []
        self.sortOption = False

    def push(self,item, priority):
        self.items.append([item, priority])
        self.items = sorted(self.items, key=itemgetter(1), reverse= self.sortOption)

    def pop(self):
    	return self.items.pop()[0]

    # return True if the stack is empty, else false is returned
    def isNotEmpty(self):
    	if self.items == []:
    		return False
    	else:
    		return True

