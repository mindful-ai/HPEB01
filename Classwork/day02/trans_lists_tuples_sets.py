Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> text = 'Ratatouille'
>>> m = re.search('tat', text)
>>> m
<re.Match object; span=(2, 5), match='tat'>
>>>  ####################################################
>>> L = ['apples', 'box', 'zebra', 'goat']
>>> type(L)
<class 'list'>
>>> L1 = [1,2,3,4]
>>> L + L1
['apples', 'box', 'zebra', 'goat', 1, 2, 3, 4]
>>> L
['apples', 'box', 'zebra', 'goat']
>>> L1
[1, 2, 3, 4]
>>> L3 = L + L1
>>> L3
['apples', 'box', 'zebra', 'goat', 1, 2, 3, 4]
>>> L1 * 3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> 'apples' in L
True
>>> 'monkey' in L
False
>>> L
['apples', 'box', 'zebra', 'goat']
>>> L3
['apples', 'box', 'zebra', 'goat', 1, 2, 3, 4]
>>> del L3[2]
>>> L3
['apples', 'box', 'goat', 1, 2, 3, 4]
>>> len(L + L1)
8
>>> len(L)
4
>>> ########################################################
>>> L[0]
'apples'
>>> L[2:5]
['zebra', 'goat']
>>> L[:]
['apples', 'box', 'zebra', 'goat']
>>> L[::2]
['apples', 'zebra']
>>> L[::-1]
['goat', 'zebra', 'box', 'apples']
>>> L[0] = 'snaple'
>>> L
['snaple', 'box', 'zebra', 'goat']
>>> ###########################################################
>>> L
['snaple', 'box', 'zebra', 'goat']
>>> L.append('cat')
>>> L
['snaple', 'box', 'zebra', 'goat', 'cat']
>>> L.append('dog')
>>> L
['snaple', 'box', 'zebra', 'goat', 'cat', 'dog']
>>> L.insert(2, 'monkey')
>>> L
['snaple', 'box', 'monkey', 'zebra', 'goat', 'cat', 'dog']
>>> L1
[1, 2, 3, 4]
>>> L2 = [5,6,7]
>>> L1.append(L2)
>>> L1
[1, 2, 3, 4, [5, 6, 7]]
>>> L1.pop()
[5, 6, 7]
>>> L1
[1, 2, 3, 4]
>>> L1.extend(L2)
>>> L1
[1, 2, 3, 4, 5, 6, 7]
>>> L1
[1, 2, 3, 4, 5, 6, 7]
>>> L2
[5, 6, 7]
>>> L
['snaple', 'box', 'monkey', 'zebra', 'goat', 'cat', 'dog']
>>> L1
[1, 2, 3, 4, 5, 6, 7]
>>> L2
[5, 6, 7]
>>> L2 = [6,7,8]
>>> L1.append(L2)
>>> L1
[1, 2, 3, 4, 5, 6, 7, [6, 7, 8]]
>>> L1[-1]
[6, 7, 8]
>>> L1[-1][1]
7
>>> L1
[1, 2, 3, 4, 5, 6, 7, [6, 7, 8]]
>>> L1.pop()
[6, 7, 8]
>>> L1
[1, 2, 3, 4, 5, 6, 7]
>>> L1
[1, 2, 3, 4, 5, 6, 7]
>>> L1.extend(L2)
>>> L1
[1, 2, 3, 4, 5, 6, 7, 6, 7, 8]
>>> L
['snaple', 'box', 'monkey', 'zebra', 'goat', 'cat', 'dog']
>>> L.pop()
'dog'
>>> L
['snaple', 'box', 'monkey', 'zebra', 'goat', 'cat']
>>> L.pop()
'cat'
>>> L
['snaple', 'box', 'monkey', 'zebra', 'goat']
>>> L.pop(1)
'box'
>>> L
['snaple', 'monkey', 'zebra', 'goat']
>>> L.remove('zebra')
>>> L
['snaple', 'monkey', 'goat']
>>> L.find('monkey')
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    L.find('monkey')
AttributeError: 'list' object has no attribute 'find'
>>> L.index('monkey')
1
>>> L.count('monkey')
1
>>> L
['snaple', 'monkey', 'goat']
>>> L.insert(0, 'apple')
>>> L.insert(3, 'kettle')
>>> L
['apple', 'snaple', 'monkey', 'kettle', 'goat']
>>> sorted(L)
['apple', 'goat', 'kettle', 'monkey', 'snaple']
>>> L
['apple', 'snaple', 'monkey', 'kettle', 'goat']
>>> L.sort()
>>> L
['apple', 'goat', 'kettle', 'monkey', 'snaple']
>>> reversed(L)
<list_reverseiterator object at 0x000001FD29796518>
>>> list(reversed(L))
['snaple', 'monkey', 'kettle', 'goat', 'apple']
>>> L
['apple', 'goat', 'kettle', 'monkey', 'snaple']
>>> L.reverse()
>>> L
['snaple', 'monkey', 'kettle', 'goat', 'apple']
>>> ######################################################################
>>> L
['snaple', 'monkey', 'kettle', 'goat', 'apple']
>>> T = tuple(L)
>>> T
('snaple', 'monkey', 'kettle', 'goat', 'apple')
>>> T[0]
'snaple'
>>> T[3:6]
('goat', 'apple')
>>> T[::-1]
('apple', 'goat', 'kettle', 'monkey', 'snaple')
>>> T
('snaple', 'monkey', 'kettle', 'goat', 'apple')
>>> T[0] = 'apple'
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    T[0] = 'apple'
TypeError: 'tuple' object does not support item assignment
>>> T1 = ('zebra', 'kite')
>>> T + T1
('snaple', 'monkey', 'kettle', 'goat', 'apple', 'zebra', 'kite')
>>> T
('snaple', 'monkey', 'kettle', 'goat', 'apple')
>>> T1
('zebra', 'kite')
>>> T1 * 3
('zebra', 'kite', 'zebra', 'kite', 'zebra', 'kite')
>>> len(T)
5
>>> del T[0]
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    del T[0]
TypeError: 'tuple' object doesn't support item deletion
>>> T.sort()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    T.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> sorted(T)
['apple', 'goat', 'kettle', 'monkey', 'snaple']
>>> T
('snaple', 'monkey', 'kettle', 'goat', 'apple')
>>> reversed(T)
<reversed object at 0x000001FD29796518>
>>> tuple(reversed(T))
('apple', 'goat', 'kettle', 'monkey', 'snaple')
>>> T
('snaple', 'monkey', 'kettle', 'goat', 'apple')
>>> colors = ('red', 'green', 'blue')
>>> r,g,b = colors
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> a,b,c,d,e = T
>>> a
'snaple'
>>> b
'monkey'
>>> c
'kettle'
>>> d
'goat'
>>> e
'apple'
>>> L = list(colors)
>>> L
['red', 'green', 'blue']
>>> a,b,c = L
>>> a
'red'
>>> b
'green'
>>> c
'blue'
>>> L.append('black')
>>> L
['red', 'green', 'blue', 'black']
>>> a,b,c = L
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    a,b,c = L
ValueError: too many values to unpack (expected 3)
>>> #################################################
>>> s = 'mississippi'
>>> ls = list(ls)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    ls = list(ls)
NameError: name 'ls' is not defined
>>> ls = list(s)
>>> ts = tuple(s)
>>> ss = set(s)
>>> ls
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> ts
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> ss
{'s', 'i', 'p', 'm'}
>>> s1 = {'a', 'b', 'c', 'd', 'e', 'f'}
>>> s1
{'f', 'c', 'b', 'e', 'd', 'a'}
>>> s1
{'f', 'c', 'b', 'e', 'd', 'a'}
>>> s1
{'f', 'c', 'b', 'e', 'd', 'a'}
>>> s2 = set('defghi')
>>> s2
{'h', 'f', 'i', 'e', 'g', 'd'}
>>> s1 | s2
{'f', 'h', 'c', 'b', 'i', 'e', 'g', 'd', 'a'}
>>> s1 & s2
{'f', 'e', 'd'}
>>> s1 ^ s2
{'b', 'h', 'g', 'a', 'c', 'i'}
>>> s1.intersection(s2)
{'f', 'e', 'd'}
>>> s1.union(s2)
{'f', 'h', 'c', 'b', 'i', 'e', 'g', 'd', 'a'}
>>> s1.add('x')
>>> s1
{'f', 'c', 'b', 'x', 'e', 'd', 'a'}
>>> s3 = {'m', 'n', 'o', 'p'}
>>> s2.add(s3)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    s2.add(s3)
TypeError: unhashable type: 'set'
>>> s1.update(s3)
>>> s1
{'f', 'p', 'c', 'b', 'n', 'x', 'e', 'd', 'm', 'a', 'o'}
>>> 'm' in s1
True
>>> 'n' in s1
True
>>> 'o' in s1
True
>>> 
