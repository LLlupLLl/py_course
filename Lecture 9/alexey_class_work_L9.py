Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Dog:
    pass

class Wallet:
    pass

class Car:
    pass

class User:
    pass

d = Dog()
type(d)
<class '__main__.Dog'>
class Dog:
    def __init__(self, name, age, ):
        self.name = name
        self.age = age

        
d = Dog()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    d = Dog()
TypeError: Dog.__init__() missing 2 required positional arguments: 'name' and 'age'
d = Dog('tay', 34)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        
dima =User('Dima', 'dima@asd.com')

type(dima)
<class '__main__.User'>
type(a)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
type(d)
<class '__main__.Dog'>
dima.name
'Dima'
dima.email
'dima@asd.com'
d.name
'tay'
d.age
34


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

vova =User('vova', 'dima@asd.com')

dima.name
'Dima'
vova.name
'vova'
dima =User('Dima', 'dima@asd.com')


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        


class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email

        
User.users_counter
0
        
User.users_counter = 888
        
User.users_counter
888
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.users_counter += 1

        
User.users_counter
0

dima = User('dima', 'sf')

vika = User('dvika', 'sf')
User.users_counter
2
vika.users_counter
2
dima.users_counter
2
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.users.counter = 1

        
User.users_counter
0
d = User('di', 'asd')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d = User('di', 'asd')
  File "<pyshell#62>", line 6, in __init__
    self.users.counter = 1
AttributeError: 'User' object has no attribute 'users'
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.users_counter += 1

        
d = User('di', 'asd')
e = User('e', 'asd')

e.users_counter
2
d.mobile = '375'

d.mobile
'375'
v.moblie
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    v.moblie
NameError: name 'v' is not defined
class WALLET:






    
KeyboardInterrupt


class Wallet:
    '''Представляет'''

    counter = 0
    def __init__(self, owner, currency, amount, adress='', color='silver'):
        self.owner = owner
        self.currency - currency
        self.amount = amount
        self.adress = adress
        self.color = color
        Wallet.counter += 1
        self.wallet_id = Wallet.couner * 10

        
Wallet.counter
0

fw = Wallet('s F', 'BYN', 1000)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    fw = Wallet('s F', 'BYN', 1000)
  File "<pyshell#95>", line 7, in __init__
    self.currency - currency
AttributeError: 'Wallet' object has no attribute 'currency'
class Wallet:
    '''Представляет'''

    counter = 0
    def __init__(self, owner, currency, amount, adress='', color='silver'):
        self.owner = owner
        self.currency = currency
        self.amount = amount
        self.adress = adress
        self.color = color
        Wallet.counter += 1
        self.wallet_id = Wallet.couner * 10

        

fw = Wallet('s F', 'BYN', 1000)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    fw = Wallet('s F', 'BYN', 1000)
  File "<pyshell#100>", line 12, in __init__
    self.wallet_id = Wallet.couner * 10
AttributeError: type object 'Wallet' has no attribute 'couner'. Did you mean: 'counter'?
class Wallet:
    '''Представляет'''

    counter = 0
    def __init__(self, owner, currency, amount, adress='', color='silver'):
        self.owner = owner
        self.currency = currency
        self.amount = amount
        self.adress = adress
        self.color = color
        Wallet.counter += 1
        self.wallet_id = Wallet.couner * 10

        
class Wallet:
    '''Представляет'''

    counter = 0
    def __init__(self, owner, currency, amount, adress='', color='silver'):
        self.owner = owner
        self.currency = currency
        self.amount = amount
        self.adress = adress
        self.color = color
        Wallet.counter += 1
        self.wallet_id = Wallet.counter * 10

        
fw = Wallet('s F', 'BYN', 1000)

fw.owner
's F'
fw.currency
'BYN'
fw.adress
''
sw = Wallet('sDG', 'RUB', 13000, color='gold')

fw.color
'silver'
fw.co
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    fw.co
AttributeError: 'Wallet' object has no attribute 'co'
fw.color
'silver'


Wallet.__doc__
'Представляет'
Wallet.name
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    Wallet.name
AttributeError: type object 'Wallet' has no attribute 'name'
Wallet.__name__
'Wallet'
Wallet.__module__
'__main__'
Wallet.__bases__
(<class 'object'>,)
fw.__dict__
{'owner': 's F', 'currency': 'BYN', 'amount': 1000, 'adress': '', 'color': 'silver', 'wallet_id': 10}
sw.__dict__
{'owner': 'sDG', 'currency': 'RUB', 'amount': 13000, 'adress': '', 'color': 'gold', 'wallet_id': 20}
for k, v in fw.__dict__.items():
    print(k, v)

    
owner s F
currency BYN
amount 1000
adress 
color silver
wallet_id 10
for k, v in sw.__dict__.items():
    print(k, v)

    
owner sDG
currency RUB
amount 13000
adress 
color gold
wallet_id 20
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f'{self.name} says {message}!')

        

d1 = User('mida', 'as')

d1.name
'mida'
d1.email
'as'
d1.hello('hello ther')
mida says hello ther!
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f'{self.name} says {message}!')
    def bye(self):
        print(f'{self.name} says bye')

        

d1 = User('asd', 'a')


d1.hello('asd')
asd says asd!
d1.bye
<bound method User.bye of <__main__.User object at 0x00000269C576AF90>>
d1.bye()
asd says bye




st = 'hello'
print(st)
hello
print(d1)
<__main__.User object at 0x00000269C576AF90>
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f'{self.name} says {message}!')
    def bye(self):
        print(f'{self.name} says bye')
    def __str__(self):
        return f'User name-{self.name}, email-{self.email}'

    
kate = User('kate', 'telaksdn@mkasmd.com')


kate.hello
<bound method User.hello of <__main__.User object at 0x00000269C576AE40>>
kate.hello('asd')
kate says asd!
print(kate)
User name-kate, email-telaksdn@mkasmd.com
a = 123
print(123)
123

dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
dir(User)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'bye', 'hello']
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f'{self.name} says {message}!')
    def bye(self):
        print(f'{self.name} says bye')
    def __str__(self):
        return f'User name-{self.name}, email-{self.email}'

    
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storade.counter_id += 1
        self.storage.update({counter_id:user})
    def show_all(self):
        for k, v in self.storagee.items():
        for k, v in self.storagee.items():
            
SyntaxError: expected an indented block after 'for' statement on line 9
    
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storade.counter_id += 1
        self.storage.update({counter_id:user})
    def show_all(self):
        for user_id, user in self.storage.items():
            print(f'User id:{user_id}')
            print(f'   name:{user.name}')
            print(f'   email:{user.email}')
            print('str')
            print(user)
            print(user.bye())

            
strg = Storage()
dima = User('Dima', 'asdasdas')
kate = User('Kate', 'asdasd' )
vasya = User('vasya', 'asdasd' )
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storade.counter_id += 1
        self.storage.update({Storage.counter_id:user})
    def show_all(self):
        for user_id, user in self.storage.items():
            print(f'User id:{user_id}')
            print(f'   name:{user.name}')
            print(f'   email:{user.email}')
            print('str')
            print(user)
            print(user.bye())

            
            
strg = Storage()
dima = User('Dima', 'asdasdas')
kate = User('Kate', 'asdasd' )
vasya = User('vasya', 'asdasd' )
strg.add_user(dima)
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    strg.add_user(dima)
  File "<pyshell#200>", line 6, in add_user
    Storade.counter_id += 1
NameError: name 'Storade' is not defined. Did you mean: 'Storage'?
strg = Storade()
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    strg = Storade()
NameError: name 'Storade' is not defined. Did you mean: 'Storage'?
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({Storage.counter_id:user})
    def show_all(self):
        for user_id, user in self.storage.items():
            print(f'User id:{user_id}')
            print(f'   name:{user.name}')
            print(f'   email:{user.email}')
            print('str')
            print(user)
            print(user.bye())

            

strg = Storage()
dima = User('Dima', 'asdasdas')
kate = User('Kate', 'asdasd' )
vasya = User('vasya', 'asdasd' )
strg.add_user(dima)





hatckback'
SyntaxError: unterminated string literal (detected at line 1)
sedan
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    sedan
NameError: name 'sedan' is not defined
wagon
Traceback (most recent call last):
  File "<pyshell#222>", line 1, in <module>
    wagon
NameError: name 'wagon' is not defined
car
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    car
NameError: name 'car' is not defined. Did you mean: 'Car'?


class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__(self):
        return 'привет из родиельиского класса'

    

class Sedan:
    pass

class Wagon:
    pass

Sedan.__bases__
(<class 'object'>,)
s = Sedan()


class Sedan(Car):
    pass

class Wagon(Car):
    pass


Sedan.__bases__
(<class '__main__.Car'>,)
s = Sedan('adasdasd', 1.2, 'asdasd')

print(s)
привет из родиельиского класса


class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__(self):
        return 'привет из родиельиского класса'
    def drive(self):
        print('asdasda')

        

class Sedan(Car):
    pass
class Wagon(Car):
    
SyntaxError: invalid syntax
class Wagon(Car):
    pass


class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__(self):
        return 'привет из родиельиского класса'
    def drive(self):
        print('asdasda')

        
class Wagon(Car):
    pass

class Sedan(Car):
    def drive(self):
        super().drive()
        print('asdasd')

        
w = Wagon(1111, 121, '1221')
s = Sedan(1111, 121, '122fdgre1')

print(w)
привет из родиельиского класса
print(s)
привет из родиельиского класса
w.drive()
asdasda
s.drive()
asdasda
asdasd
class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__(self):
        return 'привет из родиельиского класса'
    def drive(self):
        print('asdasda')
    def show_car(self):
        print(self.vin, self.volume, self.model_name)

        

class Sedan(Car):
    def drive(self):
        super().drive()
        print('asdasd')


s = Sedan(1111, 121, '122fdgre1')


s = Sedan()
Traceback (most recent call last):
  File "<pyshell#294>", line 1, in <module>
    s = Sedan()
TypeError: Car.__init__() missing 3 required positional arguments: 'vin', 'volume', and 'model_name'


money = 12312312312
class Wallet:
    def __init__(self, money):
        self.money = money

        

wall = Wallet(123123)
wall
<__main__.Wallet object at 0x00000269C576A900>
wall.money = -1213
wall.money
-1213
class Wallet:
    def __init__(self, money):
        self.__money = money

        
>>> wall = Wallet(123123)
>>> wall.money
Traceback (most recent call last):
  File "<pyshell#310>", line 1, in <module>
    wall.money
AttributeError: 'Wallet' object has no attribute 'money'
>>> class Wallet:
...     def __init__(self, money):
...         self.__money = money
...     def read(self):
...         if secret == 123:
...             return self.__money
...         return 'unaasdas'
...     def add(self, amount, secret):
...         if secret != 123:
...             return 'unnasd'
...         if amount > 0:
...             self.__money += amount
... 
>>> class Wallet:
...     def __init__(self, money):
...         self.__money = money
...     def read(self):
...         if secret == 123:
...             return self.__money
...         return 'unaasdas'
...     def add(self, amount, secret):
...         if secret != 123:
...             return 'unnasd'
...         if amount > 0:
...             self.__money += amount
...         return 'uasndasd'
... 
...     
>>> my_wallet = wallet(100)
Traceback (most recent call last):
  File "<pyshell#322>", line 1, in <module>
    my_wallet = wallet(100)
NameError: name 'wallet' is not defined. Did you mean: 'Wallet'?
>>> my_wallet = Wallet(100)
>>> 
>>> 
>>> my_wallet.money
Traceback (most recent call last):
  File "<pyshell#326>", line 1, in <module>
    my_wallet.money
AttributeError: 'Wallet' object has no attribute 'money'
>>> my_wallet.read(321)
Traceback (most recent call last):
  File "<pyshell#327>", line 1, in <module>
    my_wallet.read(321)
TypeError: Wallet.read() takes 1 positional argument but 2 were given
