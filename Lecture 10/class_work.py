Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
hasattr
<built-in function hasattr>
setattr
<built-in function setattr>
getattr
<built-in function getattr>
class Animal:
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def eat(self):
        print('животное {self.color} кушает')
    def go(self):
        print('Животное двигается')
    def sleep(self):
        print('Zzzzz....')

        

class DomesticCat(Animal):
    def __init__(self, name, color, age):
        self.name = name
        super().__init__(coloe, age)

        
cat = DomesticCat('Dima', 'black', 0)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    cat = DomesticCat('Dima', 'black', 0)
  File "<pyshell#16>", line 4, in __init__
    super().__init__(coloe, age)
NameError: name 'coloe' is not defined. Did you mean: 'color'?
class DomesticCat(Animal):
    def __init__(self, name, color, age):
        self.name = name
        super().__init__(color, age)

        
cat = DomesticCat('Dima', 'black', 0)
cat.color
'black'
cat.name
'Dima'
cat.age
0
cat.eat()
животное {self.color} кушает
class Animal:
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def eat(self):
        print(f'животное {self.color} кушает')
    def go(self):
        print('Животное двигается')
    def sleep(self):
        print('Zzzzz....')

        
cat.eat()
животное {self.color} кушает
class DomesticCat(Animal):
    def __init__(self, name, color, age):
        self.name = name
        super().__init__(color, age)

        
cat.eat()
животное {self.color} кушает
class DomesticCat(Animal):
    def __init__(self, name, color, age):
        self.name = name
        super().__init__(color, age)
    def __repr__(self):
        return f'Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}'

    
cat = DomesticCat('Dima', 'black', 0)
cat
Name:Dima
	Age:0
	Color:black
class DomesticCat(Animal):
    def __init__(self, name, color, age):
        self.name = name
        super().__init__(color, age)
    def __repr__(self):
        return f'Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}'

        

cat = DomesticCat('Dima', 'black', 0)
cat
Cat Name:Dima
	Age:0
	Color:black
cat.eat()
животное black кушает
class DomesticCat(Animal):
    caunter = 123
    def __init__(self, name, color, age):
        self.name = name
        self.id = DomesticCat.counter
        DomesticCat.counter + =1
        super().__init__(color, age)
    def __repr__(self):
        return f'Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}'
    
SyntaxError: invalid syntax
class DomesticCat(Animal):
    caunter = 123
    def __init__(self, name, color, age):
        self.name = name
        self.id = DomesticCat.counter
        DomesticCat.counter += 1
        super().__init__(color, age)
    def __repr__(self):
        return f'Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}'

    
cat = DomesticCat('Dima', 'black', 0)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    cat = DomesticCat('Dima', 'black', 0)
  File "<pyshell#45>", line 5, in __init__
    self.id = DomesticCat.counter
AttributeError: type object 'DomesticCat' has no attribute 'counter'. Did you mean: 'caunter'?
class DomesticCat(Animal):
    counter = 123
    def __init__(self, name, color, age):
        self.name = name
        self.id = DomesticCat.counter
        DomesticCat.counter += 1
        super().__init__(color, age)
    def __repr__(self):
        return f'Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}'

    
cat = DomesticCat('Dima', 'black', 0)
cat
Cat Name:Dima
	Age:0
	Color:black
cat.__dict__
{'name': 'Dima', 'id': 123, 'color': 'black', 'age': 0}
class DomesticCat(Animal):
    counter = 123
    def __init__(self, name, color, age):
        self.name = name
        self.__id = DomesticCat.counter
        DomesticCat.counter += 1
        super().__init__(color, age)
    def __repr__(self):
        return f'Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}'

    
cat = DomesticCat('Dima', 'black', 0)
cat.__id
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    cat.__id
AttributeError: 'DomesticCat' object has no attribute '__id'
cat.__dict__
{'name': 'Dima', '_DomesticCat__id': 123, 'color': 'black', 'age': 0}




stack = []
def push(value):
    stack.append(value)

    
def pop():
    stack.pop()

    
push(1)
push(2)
push(3)
push(4)
stack
[1, 2, 3, 4]
pop()
stack
[1, 2, 3]
pop()
stack
[1, 2]
pop()
sta
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    sta
NameError: name 'sta' is not defined. Did you mean: 'str'?
stack
[1]



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

    
class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.summa = 0
    def push(self, value):
        self.counter += 1
        self.summa += value
        super().push(value)

        
s1 = CountingStack()
s1.show()
[]
s1.pop()
'ne ok'
s1.counter
0
s1.summa
0

s1.push(2)
s1.push(3)
s1.push(1)
s1.show
<bound method Stack.show of <__main__.CountingStack object at 0x000002BC5EACACF0>>
s`.show()
SyntaxError: invalid syntax
s1.show()
[2, 3, 1]
s1.counter
3
s1.summa
6
s1.pop()
'ok'
s1.pop()
'ok'
s1.pop()
'ok'
s1.pop()
'ne ok'
s1.pop()
'ne ok'



s1.show()
[]




a = 10
b = 11
a + b
21
a.__add__(b)
21
a - b
-1
a.__sub__(b)
-1
a / b
0.9090909090909091
help(int)





a.__truediv__(b)
0.9090909090909091
s = 'asdsadfdsf'
s1 = 'er454544'
s.__contains__('s')
True
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __add__(self, nextcat):
        return self.age + nextcat.age
    def __contains__(self, key):
        return key in self.name
    def __len__(self):
        return self.age
    def __lt__(self, nextcat):
        return self.age < nextcat.age

    
cat = Cat('cat', 5)
cat2 = Cat('vova', 6)
c + c2
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    c + c2
NameError: name 'c' is not defined
>>> cat + cat2
11
>>> len(cat)
5
>>> len(cat2)
6
>>> cat < cat2
True
>>> cat2 < cat
False
>>> 'a' in cat
True
>>> 'd' in cat
False
>>> cat
<__main__.Cat object at 0x000002BC5EACACF0>
>>> 
>>> 
>>> 
>>> 
>>> class Wallet:
...     def __init__(self, amount):
...         self.amount = amount
...     def __add__(self, int_value):
...         return self.amount += int_value
...     def __sub__(self, int_value):
...         return self.amount - int_value
...     
SyntaxError: invalid syntax
>>> class Wallet:
...     def __init__(self, amount):
...         self.amount = amount
...     def __add__(self, int_value):
...         self.amount += int_value
...         return self.amount
...     def __sub__(self, int_value):
...         self.amount -= int_value
...         return self.amount 
...     def __len__(self):
...         return self.amount
... 
...     
>>> my_wallet = Wallet(1000)
>>> my_wallet + 100
1100
>>> len(my_wallet)
1100
>>> my_wallet - 50
1050
>>> len(my_wallet)
1050
