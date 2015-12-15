from operator import itemgetter

class PriorityStack:
    def __init__(self):
        self.items = []
        self.sortOption = False

    def push(self,item):
        self.items.append([item, self.setPriority(item)])
        self.items = sorted(self.items, key=itemgetter(1), reverse= self.sortOption)

    def pop(self):
    	return self.items.pop()[0]

    # return True if the stack is empty, else false is returned
    def isNotEmpty(self):
    	if self.items == []:
    		return False
    	else:
    		return True

    def setPriority(self, item):
        counter = item[-1]
        self.sortOption = False
        return counter
