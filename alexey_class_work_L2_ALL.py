Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
input("Дай мне пароль?")
Дай мне пароль?123
'123'
password = input("Дай мне пароль?")
Дай мне пароль?123
print(password)
123
msg = """asd
asd
qwe

c
a
sd

we
qew
-->"""
a = input(msq)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a = input(msq)
NameError: name 'msq' is not defined. Did you mean: 'msg'?
a = input(msg)
asd
asd
qwe

c
a
sd

we
qew
-->
print(a)

a = input(msg)
asd
asd
qwe

c
a
sd

we
qew
-->asadqweqe
print(a)
asadqweqe
type(a)
<class 'str'>
a = input(msg)
asd
asd
qwe

c
a
sd

we
qew
-->12312
type(a)
<class 'str'>
a*2
'1231212312'
number = input("Дай мне число:")
Дай мне число:123
result = number ** 2
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    result = number ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
a = "123"
b = "3.5"
c = 123
type(a)
<class 'str'>
type(b)
<class 'str'>
type(c)
<class 'int'>
d = 5.5
type(d)
<class 'float'>
int()
0
float()
0.0
str()
''
d
5.5
int(d)
5
str(d)
'5.5'
float(s)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    float(s)
NameError: name 's' is not defined
float(d)
5.5
d = str(d)
d
'5.5'
type(d)
<class 'str'>
d
'5.5'
a = .777
print(a)
0.777
print(2 ** 3)
8
print (2. ** 4)
16.0
print (2 ** 4.)
16.0
12 / 0
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    12 / 0
ZeroDivisionError: division by zero
0 / 6
0.0
0 // 555
0
s, ss = "Hello", "lol"
print(s, ss)
Hello lol
s
'Hello'
ss
'lol'
s + ss
'Hellolol'
res = s + s + ss
res
'HelloHellolol'
ss * 5
'lollollollollol'
5 * ss
'lollollollollol'
ss * 5.
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    ss * 5.
TypeError: can't multiply sequence by non-int of type 'float'
len(s)
5
len(ss)
3
a = "asdasdasd" "ewrfdfbv" "123123123"
a
'asdasdasdewrfdfbv123123123'
print("1", "asdasdasd", "12" "234234")
1 asdasdasd 12234234
a = "*" * 50
a
'**************************************************'
len(a)
50
print(1, "+", 2, "=", 1+2)
1 + 2 = 3
a, b = 1, 2
a
1
b
2
print(a, "+", b, "=", a+b)
1 + 2 = 3
print(f"{a}+{b}={a+b}")
1+2=3
import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
a = int(input("-->"))
-->123
type(a)
<class 'int'>
a ** 2
15129
a, b = 1, 2
a == b
False
a != b
True
a < b
True
a <= b
True
a, b = 9, 9
a == b
True
a =! b
SyntaxError: invalid syntax
a != b
False
a <= b
True
a >= b
True
type(a <= b)
<class 'bool'>
password = input("/login:")
/login:12345
if password == "12345":
    print("ok")

    
ok
password = input("/login:")
/login:123
secret = "123"
if password == secret:
    print("ok")

    
ok
password = input("/login:")
/login:333
if password == secret:
    print("ok")

    
if password == secret:
    print("ok")
else:
    print("wrong pass")

    
wrong pass


secret = "123"
secret1 = "bond"
if password == secret:
    print("ok")
elif password == secret1:
    print("spy ok")
else:
    print(-1)

    
-1
a = 123
if a == 123:
    res = True
else:
    res = False

    

res
True
res = True if a == 123 else False
res
True
password = "123"
secret
'123'
secret1
'bond'
if password == secret:
    print("ok")
elif password == secret1:
    print("spy ok")
else:
    print(-1)

    
ok
match password:
    case 'ok':
        print("ok")
    case 'bond':
        print("spy ok")
    case _:
        print("-1")

        
-1
match password:
    case '123':
        print("ok")
    case 'bond':
        print("spy ok")
    case _:
        print("-1")

        
ok
counter = 1
while counter < 10:
    print(counter)
    counter += 2

    
1
3
5
7
9
counter = 1
while counter < 10:
    print(counter)
    if counter == 5:
        print("exit")
        break
    counter += 2

    
1
3
5
exit
counter = 1
while counter < 10:
    counter += 2
    if counter == 5:
        print("exit")
        break
    
SyntaxError: multiple statements found while compiling a single statement
counter = 1
while counter < 10:
    counter += 2
    if counter == 5:
        print("go")
        continue
    print(counter)
    
SyntaxError: multiple statements found while compiling a single statement
counter = 1
while counter < 10:
    counter += 2
    if counter == 5:
        print("go")
        continue
    print(counter)
    
SyntaxError: multiple statements found while compiling a single statement

==================================================================== RESTART: Shell ====================================================================
counter = 1
while counter < 10:
    counter += 2
    if counter == 5:
        print("go")
        continue
    print(counter)
    
SyntaxError: multiple statements found while compiling a single statement
counter = 1
while counter < 10:
    counter += 2
    if counter == 5:
        print("go")
        continue
    print(counter)

    
3
go
7
9
11
for i in range(5):
    print(i)

    
0
1
2
3
4
for i in range(1,6)
SyntaxError: expected ':'
for i in range(1,6):
    print(i)

    
1
2
3
4
5
for i in range(1,6, 3):
    print(i)

    
1
4
for i in range(6, 2):
    print(i)

    


import time
time.sleep(3)
for i in range(6):
    print("sleep ", i)
    time.sleep(1)

    
sleep  0
sleep  1
sleep  2
sleep  3
sleep  4
sleep  5
st = "hello 1234"
to_find = "2"
to_find in st
True
to_find in st
True
to_find = "0"
to_find in st
False
if to_find in st:
    print(to_find, "in st")
else:
    print("nope")

    
nope
to_find = "23"
if to_find in st:
    print(to_find, "in st")
else:
    print("nope")

    
23 in st
if to_find not in st:
    print(to_find, "in st")
else:
    print("nope")

    
nope


noPrint = "нгорафывлося"
word = input("дай мне слова")
дай мне словангораффывфывывлося
word
'нгораффывфывывлося'
for char in word:
    print(char)

    
н
г
о
р
а
ф
ф
ы
в
ф
ы
в
ы
в
л
о
с
я
for char in word:
    if char in noPrint:
        continue
    print(char)

    

word
'нгораффывфывывлося'
noPrint
'нгорафывлося'
for char in word:
    if char in noPrint:
        continue
    print(char)

    

word = input("дай мне слова")
дай мне словангораф345ывлося
for char in word:
    if char in noPrint:
        continue
    print(char)

    
3
4
5
word
'нгораф345ывлося'
noPrint
'нгорафывлося'


for char in noPrint:
    if char in word:
        continue
    print(char)

    

noPrint = "нгора88фывлося"
noPrint
'нгора88фывлося'
word
'нгораф345ывлося'
for char in noPrint:
    if char in word:
        continue
    print(char)

    
8
8
for char in word:
    if char not in noPrint:
        continue
    print(char)

    
н
г
о
р
а
ф
ы
в
л
о
с
я


age = 21
money = 1000
if age > 18 and money > 900:
    print("GRIND")

    
GRIND
age = 16
if age > 18 and money > 900:
...     print("GRIND")
... 
...     
>>> if age > 18 and money > 900:
...     print("GRIND")
... 
...     
>>> True and True and False
False
>>> age = 17
>>> if age > 18 or money > 900:
...     print("GRIND")
... 
...     
GRIND
>>> money = -1
>>> if age > 18 or money > 900:
...     print("GRIND")
... 
...     
>>> False or False or False
False
>>> False or False or True
True
>>> not True
False
>>> age
17
>>> age > 10
True
>>> not age > 10
False
>>> age > 20
False
>>> not age > 20
True
>>> not False
True
>>> not not not False
True
>>> 60
60
