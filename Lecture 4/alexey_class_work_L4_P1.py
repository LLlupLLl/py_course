Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.



lit = [1,2,3]
a = [22, lit, 33, 44]

a
[22, [1, 2, 3], 33, 44]

bb = a[:]
bb
[22, [1, 2, 3], 33, 44]
lit[2] = 999
lit
[1, 2, 999]
a
[22, [1, 2, 999], 33, 44]
bb
[22, [1, 2, 999], 33, 44]
cc = a.copy()
lit[1] = 555
lit
[1, 555, 999]
a
[22, [1, 555, 999], 33, 44]
bb
[22, [1, 555, 999], 33, 44]
cc
[22, [1, 555, 999], 33, 44]
import copy
dd = copy.deepcopy(a)
dd
[22, [1, 555, 999], 33, 44]
lit[1] = 333
dd
[22, [1, 555, 999], 33, 44]
cc
[22, [1, 333, 999], 33, 44]
[22, [1, 333, 999], 33, 44]
[22, [1, 333, 999], 33, 44]




li = [1,2,3]
li[1] = 88
li
[1, 88, 3]
a = 88
a = 33
st ='12345'
st
'12345'
st[0]
'1'
st[0] = 'asdasd'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    st[0] = 'asdasd'
TypeError: 'str' object does not support item assignment
st
'12345'
len(st)
5
st
'12345'
st23 = 12345
st = '12345'
st
'12345'
id(at)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    id(at)
NameError: name 'at' is not defined
id(st)
1476548547744
id(st23)
1476547386672
jj = [1,2,3]
ff = [1,2,3]
st
'12345'
st23
12345
st = '12345'
id(st)
1476548547744
id(st23)
1476547386672
st
'12345'
st23
12345
st23 = '12345'
id(st)
1476548547744
id(st23)
1476548547744
st + st23
'1234512345'
st*6
'123451234512345123451234512345'
st*st23
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    st*st23
TypeError: can't multiply sequence by non-int of type 'str'
ch = 'f'
ch1 = 'v'
ord(ch)
102
oed(ch1)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    oed(ch1)
NameError: name 'oed' is not defined. Did you mean: 'ord'?
oed(ch1)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    oed(ch1)
NameError: name 'oed' is not defined. Did you mean: 'ord'?
ord(ch1)
118
for value in st:
    print(value)

    
1
2
3
4
5
excl = '25'
for value in st:
    if value in excl:
        continue
    print(value)

    
1
3
4
for i in range(len(st))
SyntaxError: expected ':'
for i in range(len(st))
SyntaxError: expected ':'
for i in range(len(st)):
    print('index:', i, '| value:', st[i])

    
index: 0 | value: 1
index: 1 | value: 2
index: 2 | value: 3
index: 3 | value: 4
index: 4 | value: 5
msg = "rome: grog, shakira."
secret = 8
secretMessage = ''
for char in msg:
    secretMessage += chr(ord(char)+secret)

    
secretMessage
'zwumB(ozwo4({pisqzi6'
msg
'rome: grog, shakira.'
result = ''
for char in secretMessage:
    reselt += chr(ord(char)-secret)

    
Traceback (most recent call last):
  File "<pyshell#91>", line 2, in <module>
    reselt += chr(ord(char)-secret)
NameError: name 'reselt' is not defined. Did you mean: 'result'?
for char in secretMessage:
    result += chr(ord(char)-secret)

    
result
'rome: grog, shakira.'
result = ''
for char in secretMessage:
    result += chr(ord(char)-5)

    
result
'urph=#jurj/#vkdnlud1'
st
'12345'
st{::1}
SyntaxError: invalid syntax
st[::1]
'12345'
st = 'hellohshshdjk'
st[::-1]
'kjdhshsholleh'
st ]= '[fix] asdasdasd.'
SyntaxError: unmatched ']'
st = '[fix asdasdasd]'
st1 = '[bug] asdasdasd'
st = '[fix] asdasdasd'
st3 = '[help] asdasdasd'
st[1:4]
'fix'
li = [st,st1,st3]
for s in li:
    res = s[1:4]
    if res == 'bug':
        print('баг')
    elif res == 'fix':
        print(fix)
    else:
        print(123)

        
Traceback (most recent call last):
  File "<pyshell#119>", line 6, in <module>
    print(fix)
NameError: name 'fix' is not defined
for s in li:
    res = s[1:4]
    if res == 'bug':
        print('баг')
    elif res == 'fix':
        print('fix')
    else:
        print(123)

        
fix
баг
123
st[2:]
'ix] asdasdasd'
print('asdasASDASDd'.lower())
asdasasdasdd
st
'[fix] asdasdasd'
st.upper    ()
'[FIX] ASDASDASD'
st.upper().lower().upper()
'[FIX] ASDASDASD'
name = input('->').upper()
->asdsfvsfv
name
'ASDSFVSFV'
st.index('d')
8
st.index(=)
SyntaxError: invalid syntax
st.index('=')
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    st.index('=')
ValueError: substring not found
name = 'John'
name[:2]+'K'+name[3:]
'JoKn'
name
'John'
name = 'asasdggggggrrrrvxcbhmjhmjmgn'
name.count('g')
7
name.count('=')
0
>>> name.isalpha()
True
>>> name = 'asdasdasc23sadcsadcsadc'
>>> name.isalpha
<built-in method isalpha of str object at 0x00000157C92886B0>
>>> name.isalpha()
False
>>> numbers = '12345'
>>> numbers.isdigit()
True
>>> name = '123123f'
>>> numbers.isdigit()
True
>>> name.isdigit()
False
>>> name = 'ggsdvsfdgggggergfbgfgbgh'
>>> st = '    sdfsdf    '
>>> st
'    sdfsdf    '
>>> st.strip()
'sdfsdf'
>>> st.lstrip()
'sdfsdf    '
>>> st.rstrip()
'    sdfsdf'
>>> st.title()
'    Sdfsdf    '
>>> st += st
>>> st
'    sdfsdf        sdfsdf    '
>>> st.title()
'    Sdfsdf        Sdfsdf    '
>>> st.swapcase()
'    SDFSDF        SDFSDF    '
>>> st.capitalize()
'    sdfsdf        sdfsdf    '
>>> st.split()
['sdfsdf', 'sdfsdf']
