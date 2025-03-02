#Stack is Dynamic Array

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, i):
        return self.stack.append(i)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
object = Stack()
object.push(1)
object.push(2)
object.push(3)
print(object.stack)
object.pop()
print(object.stack)
print(object.peek())
object.pop()
print(object.stack)
print(object.peek())