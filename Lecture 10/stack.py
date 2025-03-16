class Stack:
    pass


class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        self.srack.pop()

        
s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.stack
[1, 2, 3]
s2 = Stack()
\

s1.pop()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    s1.pop()
  File "<pyshell#93>", line 7, in pop
    self.srack.pop()
AttributeError: 'Stack' object has no attribute 'srack'. Did you mean: 'stack'?
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        try:
            self.stack.pop()
        except:
            return 'ne ok'
        return: 'ok'
    
SyntaxError: invalid syntax
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        try:
            self.stack.pop()
        except:
            return 'ne ok'
        return 'ok'
    def show(self):
        return self.stack

    
s1 = Stack()
s1.pop()
'ne ok'
s1.push(123)
s1.push(1)
s1.push(2)
s1.push(3)
s1.show()
[123, 1, 2, 3]
s1.pop()
'ok'
s1.show()
[123, 1, 2]
