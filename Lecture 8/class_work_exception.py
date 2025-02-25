Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1 / 0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    1 / 0
ZeroDivisionError: division by zero
s = 'asdasd'
s.capitalize()
'Asdasd'
s.decapitalize()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.decapitalize()
AttributeError: 'str' object has no attribute 'decapitalize'. Did you mean: 'capitalize'?
li = [1,2,3,4]
li[0.5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    li[0.5]
TypeError: list indices must be integers or slices, not float
1 / 0
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    1 / 0
ZeroDivisionError: division by zero
try:
    1 / 0
except:
    print(-1)

    
-1
try:
    li = [1,2,3]
    li[0.5]
except:
    print(-1)

    
-1
try:
    int('-asdsad-a..5')
except:
    print(-1)

    
-1
try:
    1 / 0
except ZeroDivisionError:
    print('zero')
except:
    print(-1)

    
zero
try:
    1 / 0
except ZeroDivisionError:
    print('zero')
except TypeError:
    li = [1,2,3]
    li[0.5]
    print('type')
except:
    print(-1)

    
zero
try:
    li = [1,2,3]
    li[0.5]
except ZeroDivisionError:
    print('zero')
except TypeError:
    print('type')
except:
    print(-1)

    
type


try:
    li = [1,2,3]
    li[0.5]
except ZeroDivisionError as zde:
    print('zero', zde.args)
except TypeError as te:
    print('type', tr.args)
except:
    print(-1)

    
Traceback (most recent call last):
  File "<pyshell#25>", line 3, in <module>
    li[0.5]
TypeError: list indices must be integers or slices, not float

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#25>", line 7, in <module>
    print('type', tr.args)
NameError: name 'tr' is not defined
try:
    li = [1,2,3]
    li[0.5]
except ZeroDivisionError as zde:
    print('zero', zde.args)
except TypeError as te:
    print('type', te.args)
except:
    print(-1)

...     
type ('list indices must be integers or slices, not float',)
>>> try:
...     raise ZeroDivisionError
... except ZeroDivisionError as zde:
...     print('zero', zde.args)
... except TypeError as te:
...     print('type', te.args)
... except:
...     print(-1)
... 
...     
zero ()
>>> 
>>> 
>>> 
>>> try:
...     raise ZeroDivisionError
... except ZeroDivisionError as zde:
...     print('zero', zde.args)
... except TypeError as te:
...     print('type', te.args)
... except:
...     print(-1)
... 
...     
zero ()
>>> 
>>> import elchuasasd
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    import elchuasasd
ModuleNotFoundError: No module named 'elchuasasd'
>>> a = 6
>>> if a  == 8:
...     try:
...         import time
...     except:
...         pass
... else:
...     print('делай без модуля time')
... 
...     
делай без модуля time
>>> time.sleep(12)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    time.sleep(12)
NameError: name 'time' is not defined. Did you forget to import 'time'?
>>> a = 8
>>> if a  == 8:
...     try:
...         import time
...     except:
...         pass
... else:
...     print('делай без модуля time')
... 
...     
>>> time.sleep(2)
