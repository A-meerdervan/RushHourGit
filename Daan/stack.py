class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        if self.items == []:
            print "The stack is empty"
        else:
            return self.items.pop(0)
stack = Stack()
stack.push(3)
stack.push(4)
print stack.items
stack.pop()
print stack.items
