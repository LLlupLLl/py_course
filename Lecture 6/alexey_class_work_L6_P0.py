Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li = []
type(li)
<class 'list'>
tp = ()
type(tp)
<class 'tuple'>
tp2 = tuple()
type(tp2)
<class 'tuple'>
num = 2
num = 2.
num
2.0
type(num)
<class 'float'>
num = 2,
num
(2,)
type(num)
<class 'tuple'>
li = [12,33,44]
st "asdg"
SyntaxError: invalid syntax
st = "asdasd"
se = set(st)
se
{'a', 's', 'd'}
t = (1,2,3,4, 'asd')
t
(1, 2, 3, 4, 'asd')
t = tuple(se)
t
('a', 's', 'd')
isinstance(t, tuple)
True
n = (1,2,3,4,5)
n
(1, 2, 3, 4, 5)
type(n)
<class 'tuple'>
n[0]
1
n[-1]
5
n[1] = 123
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    n[1] = 123
TypeError: 'tuple' object does not support item assignment
LiN = list(n)
n
(1, 2, 3, 4, 5)
Lin
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    Lin
NameError: name 'Lin' is not defined. Did you mean: 'LiN'?
LiN
[1, 2, 3, 4, 5]
LiN[2] = 333
LiN
[1, 2, 333, 4, 5]
n
(1, 2, 3, 4, 5)
n = tuple(LiN)
n
(1, 2, 333, 4, 5)
t
('a', 's', 'd')
t = (1,2,4)
T
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    T
NameError: name 'T' is not defined
t
(1, 2, 4)
a,b,c = t
a
1
b
2
c
4
s = 'abg'
s
'abg'
a,b,c = s
a
'a'
b
'b'
c
'g'
t = (1,2,3,4,5,6,7)
a,b,c = t
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a,b,c = t
ValueError: too many values to unpack (expected 3)
a,b,*c = t
a
1
b
2
c
[3, 4, 5, 6, 7]
a,*,c = t
SyntaxError: invalid syntax
a,*b,c = t
a
1
b
[2, 3, 4, 5, 6]
c
7
*a,b,c = t
a
[1, 2, 3, 4, 5]
b
6
c
7
st = 'dffgfgeg'
st
'dffgfgeg'
a,b,*c = st
a
'd'
b
'f'
c
['f', 'g', 'f', 'g', 'e', 'g']
def number():
    return 1,2,3,4,5

number()
(1, 2, 3, 4, 5)
t
(1, 2, 3, 4, 5, 6, 7)
t[:]
(1, 2, 3, 4, 5, 6, 7)
aaa =t
aaa[1]=99
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    aaa[1]=99
TypeError: 'tuple' object does not support item assignment
t[1:]
(2, 3, 4, 5, 6, 7)
t[1:5]
(2, 3, 4, 5)
t
(1, 2, 3, 4, 5, 6, 7)
t[1:-1]
(2, 3, 4, 5, 6)
t[::2]
(1, 3, 5, 7)
t
(1, 2, 3, 4, 5, 6, 7)
t += 1
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    t += 1
TypeError: can only concatenate tuple (not "int") to tuple
t += (1,)
t
(1, 2, 3, 4, 5, 6, 7, 1)
t + t
(1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1)
t * 6
(1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1)
t *= 4
t
(1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1)
5 in t
True
t = (1,2,3,4)
t
(1, 2, 3, 4)
155
155
144
144
t[1:3]
(2, 3)
(155, )
(155,)
(144, )
(144,)
t = (155, ) + t[1:3] + (144, )
t
(155, 2, 3, 144)
t.coun(7)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    t.coun(7)
AttributeError: 'tuple' object has no attribute 'coun'. Did you mean: 'count'?
tp
()
t = (4,3,2,1)
t
(4, 3, 2, 1)
for value in t:
    print('-->', value)


--> 4
--> 3
--> 2
--> 1


n = len(t)
n
4
for index in t:
    print(t[index])


Traceback (most recent call last):
  File "<pyshell#118>", line 2, in <module>
    print(t[index])
IndexError: tuple index out of range
for i in range(n):
    print(t, ' value:', t[i])


(4, 3, 2, 1)  value: 4
(4, 3, 2, 1)  value: 3
(4, 3, 2, 1)  value: 2
(4, 3, 2, 1)  value: 1









di = {}
type(de)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    type(de)
NameError: name 'de' is not defined
type(di)
<class 'dict'>
>>> di1 = dict()
>>> di1
{}
>>> type(di1)
<class 'dict'>
>>> se
{'a', 's', 'd'}
>>> de = {1:'value', '':12312}
>>> se
{'a', 's', 'd'}
>>> di
{}
>>> de
{1: 'value', '': 12312}
>>> hash
<built-in function hash>
>>> a = 3
>>> b = 4.
>>> c = 'asdasd'
>>> li = [1,2,3]
>>> se = {3,2,4,2}
>>> tp = (1,2,3,4)
>>> hash(a)
3
>>> hash(b)
4
>>> hash(de)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    hash(de)
TypeError: unhashable type: 'dict'
>>> hash(li)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    hash(li)
TypeError: unhashable type: 'list'
>>> dd = {1:'a', 2,:'sdfsdf', 's':'asdasd'}
SyntaxError: ':' expected after dictionary key
>>> dd = {1:'a', 2.:'sdfsdf', 's':'asdasd'}
>>> dd
{1: 'a', 2.0: 'sdfsdf', 's': 'asdasd'}
>>> li = []
>>> li.pop()
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    li.pop()
IndexError: pop from empty list
>>> di = {i:i**3 for i in range(50, 60)}
>>> di
{50: 125000, 51: 132651, 52: 140608, 53: 148877, 54: 157464, 55: 166375, 56: 175616, 57: 185193, 58: 195112, 59: 205379}
