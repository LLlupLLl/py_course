Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li = []
print(li)
[]
li1 = []
print(li1)
[]
a= [1,2,3,True, "edfe"]
a
[1, 2, 3, True, 'edfe']
a[3]
True
a[4]
'edfe'
a["1"]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a["1"]
TypeError: list indices must be integers or slices, not str
a[5]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[5]
IndexError: list index out of range
type(li)
<class 'list'>
type(a)
<class 'list'>
a[0]
1
type(a[0])
<class 'int'>
st = "Hello"
st.upper()
'HELLO'
st
'Hello'
q = 100
q.uppper()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    q.uppper()
AttributeError: 'int' object has no attribute 'uppper'
a.upper()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.upper()
AttributeError: 'list' object has no attribute 'upper'
st.upper()
'HELLO'
"khghjhj".upper()
'KHGHJHJ'





a = [4, 3, 45, 6, 7, 8, 93]
a.append(777)
a
[4, 3, 45, 6, 7, 8, 93, 777]
a.insert(2, 9)
a
[4, 3, 9, 45, 6, 7, 8, 93, 777]
a.insert(4, 10)
a
[4, 3, 9, 45, 10, 6, 7, 8, 93, 777]
len(a)
10
a.reverse()
a
[777, 93, 8, 7, 6, 10, 45, 9, 3, 4]
a.reverse()
a
[4, 3, 9, 45, 10, 6, 7, 8, 93, 777]
a.pop()
777
a
[4, 3, 9, 45, 10, 6, 7, 8, 93]
a.pop(3)
45
a
[4, 3, 9, 10, 6, 7, 8, 93]
res = a.pop(4)
a
[4, 3, 9, 10, 7, 8, 93]
res
6
del a[0]
a
[3, 9, 10, 7, 8, 93]
li[]
SyntaxError: invalid syntax
li
[]
del li
li
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    li
NameError: name 'li' is not defined
a
[3, 9, 10, 7, 8, 93]
a.remove(1)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
a.remove(8)
a
[3, 9, 10, 7, 93]
a.pop(8)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.pop(8)
IndexError: pop index out of range
toDel = 555
if toDel in a:
    a.remove(toDel)

    

a.count()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
a.count(6)
0
a.count(93)
1
a.append(93)
a
[3, 9, 10, 7, 93, 93]
a.count(93)
2
a.clear()
a
[]
a = [3, 9, 10, 7, 93, 93]
a.index(10)
2
a.index(93)
4
a.index(93, a.index(93)+1)
5
li = [7,7,7]
a += li
a
[3, 9, 10, 7, 93, 93, 7, 7, 7]
a *= 2
a
[3, 9, 10, 7, 93, 93, 7, 7, 7, 3, 9, 10, 7, 93, 93, 7, 7, 7]



q = [1, 3, 5, 7, 2, 4, 6]
q
[1, 3, 5, 7, 2, 4, 6]
q[0]
1
q[-1]
6
q[-2]
4
q[-5]
5
q[2]=555
q
[1, 3, 555, 7, 2, 4, 6]
[1, 3, 555, 7, 2, 4, 6]
[1, 3, 555, 7, 2, 4, 6]



li = [}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
li = []
li
[]

li
[]
li = [44, 55, 66, 777]
li
[44, 55, 66, 777]
li.reverse()
li
[777, 66, 55, 44]
li.append(1000)
li
[777, 66, 55, 44, 1000]
sorted(li)
[44, 55, 66, 777, 1000]
liu
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    liu
NameError: name 'liu' is not defined. Did you mean: 'li1'?
li
[777, 66, 55, 44, 1000]
for i in sorted(li):
    print(i)

    
44
55
66
777
1000

for i in sorted(li):
    print(i, end=" ")

    
44 55 66 777 1000 
li
[777, 66, 55, 44, 1000]
sorted(li, reverse=True)
[1000, 777, 66, 55, 44]
li
[777, 66, 55, 44, 1000]



li = [3, 5, 0, -10, 4]
li
[3, 5, 0, -10, 4]

a, b = 66, 77
tmp = a
a = b
b = tmp
a
77
b
66
a, b = 66, 77
a=b
b=a
a
77
b
77
a, b = 66, 77
a, b = b, a
a
77
b
66
li
[3, 5, 0, -10, 4]
li[1], li[2] = li[2], li[1]
li
[3, 0, 5, -10, 4]
li[2], li[3] = li[3], li[2]
li
[3, 0, -10, 5, 4]
li[3], li[4] = li[4], li[3]
li
[3, 0, -10, 4, 5]
li[0], li[1] = li[1], li[0]
li
[0, 3, -10, 4, 5]
li[1], li[2] = li[2], li[1]
li
[0, -10, 3, 4, 5]
li[0], li[1] = li[1], li[0]
li
[-10, 0, 3, 4, 5]
max(li)
5
min(li)
-10
print
<built-in function print>
sum(li)
2
len(li)
5
sum(li)/len(li)
0.4



li = [1, 2, 3, 4]
a = li
a
[1, 2, 3, 4]
li
[1, 2, 3, 4]
id(li)
2653787151488
id(a)
2653787151488
a[1] = 99999
a
[1, 99999, 3, 4]
li
[1, 99999, 3, 4]
li = [1, 2, 3, 4]
li
[1, 2, 3, 4]
a = li.copy()
a
[1, 2, 3, 4]
li
[1, 2, 3, 4]
id(li)
2653823789056
id(a)
2653823803520
a[1] = 5555
a
[1, 5555, 3, 4]
li
[1, 2, 3, 4]
li = [1, 2, 3, 4]
a = li[:}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a = li[:]
id(a)
2653823789120
id(li)
2653823802048



li
[1, 2, 3, 4]
li[:]
[1, 2, 3, 4]
li[:3]
[1, 2, 3]
li[1:]
[2, 3, 4]
li
[1, 2, 3, 4]
li += li
i
1000
li
[1, 2, 3, 4, 1, 2, 3, 4]
kk = li[::2]
kk
[1, 3, 1, 3]
li[::-1]
[4, 3, 2, 1, 4, 3, 2, 1]
4 in li
True
77 in li
False




s = {}
type(s)
<class 'dict'>
s = set()
type(s)
<class 'set'>
s = {"df", 1, 2, 3, 1, 1, 2, 3}
s
{'df', 1, 2, 3}
s.add(1)
s
{'df', 1, 2, 3}
s.update({1,2,3,4,6666})
s
{1, 2, 3, 4, 6666, 'df'}
s.clear()
s
set()
s = {1, 2, 3, 4, 6666, 'df'}
s.remove(555)
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    s.remove(555)
KeyError: 555
s.remove(4)
s
{'df', 1, 2, 3, 6666}
s.discard(444)
s
{'df', 1, 2, 3, 6666}
s.discard(2)
s
{'df', 1, 3, 6666}
len(s)
4
type(s)
<class 'set'>

li
[1, 2, 3, 4, 1, 2, 3, 4]
li = list(set(li))
li
[1, 2, 3, 4]
set(li)
{1, 2, 3, 4}
s
{'df', 1, 3, 6666}
list(s)
['df', 1, 3, 6666]

st
'Hello'
list(st)
['H', 'e', 'l', 'l', 'o']
set(st)
{'H', 'o', 'l', 'e'}
li
[1, 2, 3, 4]
s
{'df', 1, 3, 6666}
st
'Hello'
int(li)
Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    int(li)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
st(li)
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    st(li)
TypeError: 'str' object is not callable
str(li)
'[1, 2, 3, 4]'
ppp = srt(li)
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    ppp = srt(li)
NameError: name 'srt' is not defined. Did you mean: 'st'?
ppp = str(li)
ppp
'[1, 2, 3, 4]'
list(ppp)
['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ']']



my_list = [1,2,4,4,1,4,2,6,2,9]
li = list(set(my_list))
li
[1, 2, 4, 6, 9]





li = [1, 2, 3, 4, 5]
resList = []
dor v in li:
    
SyntaxError: invalid syntax
for v in li:
    resList.append(v**2)

    
li
[1, 2, 3, 4, 5]
resList
[1, 4, 9, 16, 25]
li = [1, 2, 3, 4, 5]
resList = [v**2 for v in li]
resList
[1, 4, 9, 16, 25]
li = [1, 2, 3, 4, 5,6,7,8,9,10]
resList = [v**2 for v in li if v%2==0]
resList
[4, 16, 36, 64, 100]


li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



numbers = [int(input("-->")) for i in range(int(input("-->")))]
-->6
-->44
-->55
-->66
-->1
-->2
-->3
numbers
[44, 55, 66, 1, 2, 3]


number = []
n = int(input("-->"))
-->6
for i in range(n):
    numbers.append(int(input("-->")))

    
-->5
-->5
-->5
-->5
-->5
-->5


li = input("x x x x:-->")
x x x x:-->1 2 3 4
li
'1 2 3 4'
li = li.split()
li
['1', '2', '3', '4']
li = [int(v) for v in li]
li
[1, 2, 3, 4]
sum(li)
10
li = [li = [int(v) for v in input("x x x x:-->").split()]
      
SyntaxError: '[' was never closed
li = [int(v) for v in input("x x x x:-->").split()]
      
x x x x:-->4 5 6 7 8
li
      
[4, 5, 6, 7, 8]
summa
      
Traceback (most recent call last):
  File "<pyshell#299>", line 1, in <module>
    summa
NameError: name 'summa' is not defined


li
      
[4, 5, 6, 7, 8]




li = [1,2,3,4]
      
li[0]
      
1
li[1]
      
2
li = [[], [], []]
      
li[0]
      
[]
li[-1]
...       
[]
>>> li = [[1,2,3], [11,22,33], [0,5,8]]
...       
>>> li[0]
...       
[1, 2, 3]
>>> li[1]
...       
[11, 22, 33]
>>> li[2]
...       
[0, 5, 8]
>>> li[0][2]
...       
3
>>> li[1][1]
...       
22
>>> li[2][0]
...       
0
>>> li = [[1,2,3], [11,22,33], [0,5,8]]
...       
>>> li[0].append(333)
...       
>>> li
...       
[[1, 2, 3, 333], [11, 22, 33], [0, 5, 8]]
>>> li[0][2] = 222
...       
>>> li
...       
[[1, 2, 222, 333], [11, 22, 33], [0, 5, 8]]
>>> li = [[[1,2,3,][1,2,3]]]
...       
Traceback (most recent call last):
  File "<pyshell#324>", line 1, in <module>
    li = [[[1,2,3,][1,2,3]]]
TypeError: list indices must be integers or slices, not tuple
>>> 
>>> li = [[[1,2,3][1,2,3]]]
...       
Traceback (most recent call last):
  File "<pyshell#326>", line 1, in <module>
    li = [[[1,2,3][1,2,3]]]
TypeError: list indices must be integers or slices, not tuple
>>> li = [[[1,2,3],[1,2,3]]]
...       
>>> li
...       
[[[1, 2, 3], [1, 2, 3]]]
