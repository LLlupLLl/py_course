Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n = 10
user = []
user_a
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    user_a
NameError: name 'user_a' is not defined. Did you mean: 'user'?
user_a_password = input('pass:')
pass:12345
user_a_name = input('name:')
name:vasia
user.append([user_a_name, user_a_password],)
user
[['vasia', '12345']]
def register():
    user_a_password = input('pass:')
    user_a_name = input('name:')
    user.append([user_a_name, user_a_password],)
    print('done')

    
register()
pass:123
name:asdasd
done
user
[['vasia', '12345'], ['asdasd', '123']]
n = 8
for i in range(n):
register()
SyntaxError: expected an indented block after 'for' statement on line 1
for i in range(n):
    register()

    
pass:123
name:123
done
pass:
name:dsf
done
pass:324r
name:d
done
pass:
name:34r
done
pass:fw
name:324r
done
pass:
name:svd
done
34pass:r
name:
done
dpass:s
name:32r
done

user
[['vasia', '12345'], ['asdasd', '123'], ['123', '123'], ['f', ''], ['d', '24r'], ['r', ''], ['r', 'fw'], ['', ''], ['', 'r'], ['32r', 's']]
def hello():
    print('hello')

    

hello()
hello








def hello():
    user = input('yoye name')
    print('hello')

    
hello()
yoye nameasd
hello
def hello():
    user = input('yoye name')
    print(f'hello, {user}')

    
hello()
yoye nameasd
hello, asd



def hello():
    user = input('yoye name')
    print(f'hello, {user}')
    for i in range(3):
        print(i, end=' ')
    d = 88
    if d == 88:
        print('xxx')
    print(asdasd)

    
hello()
yoye nameasd
hello, asd
0 1 2 xxx
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    hello()
  File "<pyshell#50>", line 9, in hello
    print(asdasd)
NameError: name 'asdasd' is not defined




def hello(user):
    print('heloo', user)

    
hello(2)
heloo 2
hello()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    hello()
TypeError: hello() missing 1 required positional argument: 'user'
hello(1,2,3)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    hello(1,2,3)
TypeError: hello() takes 1 positional argument but 3 were given


def hello(a,b,c):
    print('heloo', a,b,c)

    
hello(1,2,3)
heloo 1 2 3
hello(2)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    hello(2)
TypeError: hello() missing 2 required positional arguments: 'b' and 'c'
hello(b=2,1,c=3)
SyntaxError: positional argument follows keyword argument
def hello(name,age):
    print('heloo', name,age)

    
hello(21,asdf)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    hello(21,asdf)
NameError: name 'asdf' is not defined
hello(123,'asd')
heloo 123 asd
hello(1,34)
heloo 1 34
def create_order(name, ph, age='', msg=''):
    print('Order 12312: created.')
    print('order details:')
    print(f'   name:{name}')
    print(f'   ph:{ph}')
    print(f'   age:{age}')
    print(f'   msg:{msg}')

    
create_order(1,2,3,4)
Order 12312: created.
order details:
   name:1
   ph:2
   age:3
   msg:4


create_order(1,2)
Order 12312: created.
order details:
   name:1
   ph:2
   age:
   msg:
create_order(age=1,name=1)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    create_order(age=1,name=1)
TypeError: create_order() missing 1 required positional argument: 'ph'
\



name = input('-->')
-->1231234
name
'1231234'
def hello():
    pass


res = hello()
res
print(res)
None


def create_order(name, ph, age='', msg=''):
    if len(name) < 2:
        return False
    if str(ph).isallnum() != True:
        return False
    print('Order 12312: created.')
    print('order details:')
    print(f'   name:{name}')
    print(f'   ph:{ph}')
    print(f'   age:{age}')
    print(f'   msg:{msg}')
    print()
    return True

res = create_order('', 123213)
res
False


def create_order(name, ph, age='', msg=''):
    if len(name) < 2:
        return False
    if ph.isalnum() != True:
        return False
    print('Order 12312: created.')
    print('order details:')
    print(f'   name:{name}')
    print(f'   ph:{ph}')
    print(f'   age:{age}')
    print(f'   msg:{msg}')
    print()
    return True

create_order('asd', 123)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    create_order('asd', 123)
  File "<pyshell#108>", line 6, in create_order
    if ph.isalnum() != True:
AttributeError: 'int' object has no attribute 'isalnum'




def create_order(name, ph, age='', msg=''):
    '''
    параметры:
    1
    2
    3
    4
    5
    6
    

    '''
    if len(name) < 2:
        return False
    if str(ph).isallnum() != True:
        return False
    print('Order 12312: created.')
    print('order details:')
    print(f'   name:{name}')
    print(f'   ph:{ph}')
    print(f'   age:{age}')
    print(f'   msg:{msg}')
    print()
    return True

help(create_order)
Help on function create_order in module __main__:

create_order(name, ph, age='', msg='')
    параметры:
    1
    2
    3
    4
    5
    6

def a():
    print(1)

    
def b():
    print(2)

    

def c():
    print(3)

    
a
<function a at 0x0000028AB5C518A0>
b
<function b at 0x0000028AB5C51800>
c
<function c at 0x0000028AB5C51940>
b()
2
a()
1
c()
3
id(a)
2794778335392
id(b)
2794778335232



def number(num):
    if num % 2 == 0:
        return True

    
number(1)

print(number(1))
None

a = 10
s  = 'adad'

isinstance(a, int)
True
isinstance(s, str)
True
total = 0
def add_to_toral(n):
    toral = total + n

    
def add_to_total(n):
    total = total + n

    
add_to_total(5)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    add_to_total(5)
  File "<pyshell#154>", line 2, in add_to_total
    total = total + n
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
x = 1233
def add(x):
    print('inside:'x, id(x))
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
x
1233



def add(number):
    print('inside', number, id(number))
    number += 888
    print('inside', number, id(number))

    
add(3)
inside 3 140728317576168
inside 891 2794777271504

def a():
    print(1)

    
def b():
    print(2)

    
for i in li:
    i()

    
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    for i in li:
NameError: name 'li' is not defined
li = [a,b]

for i in li:
    i()

    
1
2



def noname(number):
    if number > 20:
        return True
    return number + number(number + 4)

noname(4)
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    noname(4)
  File "<pyshell#190>", line 4, in noname
    return number + number(number + 4)
TypeError: 'int' object is not callable
def noname(number):
    if number > 20:
        return True
    return number + noname(number + 4)
noname(1)
SyntaxError: invalid syntax
noname(1)
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    noname(1)
  File "<pyshell#190>", line 4, in noname
    return number + number(number + 4)
TypeError: 'int' object is not callable
import sys
>>> sys.getrecursionlimit()
1000
>>>  f1=f2=1
...  
SyntaxError: unexpected indent
>>> f1
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    f1
NameError: name 'f1' is not defined
>>> f2
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    f2
NameError: name 'f2' is not defined
>>> f1=f2
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    f1=f2
NameError: name 'f2' is not defined
>>> f1=f2=1
>>> f1
1
>>> f2
1
>>> f1,f2 = f2, f1+f2
>>> f1
1
>>> f2
2
>>> f1=f2=1
>>> for i in range(10):
...     f1,f2 = f2, f1+f2
... 
...     
>>> f2
144
>>> f1
89
