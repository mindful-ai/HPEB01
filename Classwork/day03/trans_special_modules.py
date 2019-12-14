Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = [1,2,3,4,5]
>>> L1 = L
>>> L
[1, 2, 3, 4, 5]
>>> L1
[1, 2, 3, 4, 5]
>>> L1[2] = 9
>>> L1
[1, 2, 9, 4, 5]
>>> L
[1, 2, 9, 4, 5]
>>> from copy import deepcopy
>>> L2 = deepcopy(L1)
>>> L2 = deepcopy(L)
>>> L
[1, 2, 9, 4, 5]
>>> L1
[1, 2, 9, 4, 5]
>>> L2
[1, 2, 9, 4, 5]
>>> L2[4] = 10
>>> L2
[1, 2, 9, 4, 10]
>>> L
[1, 2, 9, 4, 5]
>>> L1
[1, 2, 9, 4, 5]
>>> L[0] = 13
>>> L
[13, 2, 9, 4, 5]
>>> L1
[13, 2, 9, 4, 5]
>>> L2
[1, 2, 9, 4, 10]
>>> ##########################################
>>> import datetime
>>> ct = datetime.datetime.now()
>>> ct
datetime.datetime(2019, 12, 12, 16, 45, 30, 674434)
>>> ct.year
2019
>>> ct.hour
16
>>> ct.minute
45
>>> format = "%a %b %d %H:%M:%S %Y"
>>> ct.strftime(format)
'Thu Dec 12 16:45:30 2019'
>>> dt = "Thu Dec 12 16:45:30 2019"
>>> t = dt.strptime(format)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    t = dt.strptime(format)
AttributeError: 'str' object has no attribute 'strptime'
>>> datetime.strptime(dt, format)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    datetime.strptime(dt, format)
AttributeError: module 'datetime' has no attribute 'strptime'
>>> 
KeyboardInterrupt
>>> strptime(dt, format)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    strptime(dt, format)
NameError: name 'strptime' is not defined
>>> datetime.datetime.strptime(dt, format)
datetime.datetime(2019, 12, 12, 16, 45, 30)
>>> dt
'Thu Dec 12 16:45:30 2019'
>>> format
'%a %b %d %H:%M:%S %Y'
>>> format = "%A %B %d  %Y  %H:%M:%S"
>>> ct.strftime(format)
'Thursday December 12  2019  16:45:30'
>>> format = "%A %B / %d  %Y / %H:%M:%S
SyntaxError: EOL while scanning string literal
>>> 
KeyboardInterrupt
>>> format = "%A %B / %d  %Y / %H:%M:%S"
>>> ct.strftime(format)
'Thursday December / 12  2019 / 16:45:30'
>>> ###############################################################
>>> from functools import reduce
>>> L = [1,2,3,4]
>>> D = reduce(lambda x,y:x+y, L)
>>> D
10
>>> ###############################################################
>>> 
>>> from itertools import permutations, combinations
>>> L = ['a', 'b', 'c', 'd']
>>> permutations(L, 3)
<itertools.permutations object at 0x000001BDBE27EE08>
>>> list(permutations(L, 3))
[('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'b'), ('a', 'c', 'd'), ('a', 'd', 'b'), ('a', 'd', 'c'), ('b', 'a', 'c'), ('b', 'a', 'd'), ('b', 'c', 'a'), ('b', 'c', 'd'), ('b', 'd', 'a'), ('b', 'd', 'c'), ('c', 'a', 'b'), ('c', 'a', 'd'), ('c', 'b', 'a'), ('c', 'b', 'd'), ('c', 'd', 'a'), ('c', 'd', 'b'), ('d', 'a', 'b'), ('d', 'a', 'c'), ('d', 'b', 'a'), ('d', 'b', 'c'), ('d', 'c', 'a'), ('d', 'c', 'b')]
>>> list(combinations(L, 3))
[('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd')]
>>> ###################################################################
>>> L = ['red', 'green', 'blue', 'red', 'green', 'yellow', 'red']
>>> D = {}
>>> for color in L:
	if(color in D.keys()):
		D[color] = D[color] + 1
	else:
		D[color] = 1

		
>>> D
{'red': 3, 'green': 2, 'blue': 1, 'yellow': 1}
>>> from collections import Counter
>>> z = Counter(L)
>>> z
Counter({'red': 3, 'green': 2, 'blue': 1, 'yellow': 1})
>>> ###################################################################
>>> from operator import itemgetter
>>> itemgetter(1)('ABCDE')
'B'
>>> itemgetter(1)(['a', 'v', 'g'])
'v'
>>> f = itemgetter(-1)
>>> f('AAPLES')
'S'
>>> f(range(10))
9
>>> L = ['apples', 'red', 'zebra']
>>> L.sort(key=f)
>>> L
['zebra', 'red', 'apples']
>>> ###################################################################
>>> import shelve
>>> D = {'name':'Vijay', 'place':'Vijaynagar', 'company':'HPE', 'country':'INDIA'}
>>> D
{'name': 'Vijay', 'place': 'Vijaynagar', 'company': 'HPE', 'country': 'INDIA'}
>>> f = shelve.open('data.db')
>>> f['mydata'] = D
>>> f.sync()
>>> f.close()
>>> import os
>>> os.getcwd()
'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37'
>>> os.listdir()
['data.db.bak', 'data.db.dat', 'data.db.dir', 'DLLs', 'Doc', 'examples', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python37.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll']
>>> 
