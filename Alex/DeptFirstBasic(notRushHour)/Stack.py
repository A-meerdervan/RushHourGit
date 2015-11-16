class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
    def pop(self):
    	return self.items.pop()

    # return True if the stack is empty, else false is returned
    def isNotEmpty(self):
    	if self.items == []:
    		return False
    	else:
    		return True
