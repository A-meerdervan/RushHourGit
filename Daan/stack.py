class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item) # insert(0,item)??

    def pop(self):
        if self.items == []:
            print "The stack is empty"
        else:
            return self.items.pop()
