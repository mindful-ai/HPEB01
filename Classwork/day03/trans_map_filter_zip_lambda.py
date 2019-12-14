Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = lambda x,y:x+y
>>> type(f)
<class 'function'>
>>> f(10,20)
30
>>> f(5,4)
9
>>> L = ['zebra', 'coat', 'boat', 'ink', 'kite', 'purple', 'air']
>>> L.sort()
>>> L
['air', 'boat', 'coat', 'ink', 'kite', 'purple', 'zebra']
>>> L.sort(-1)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    L.sort(-1)
TypeError: sort() takes no positional arguments
>>> L.sort(key=lambda s:s[-1])
>>> L
['zebra', 'kite', 'purple', 'ink', 'air', 'boat', 'coat']
>>> L.sort(key=lambda x:x[1])
>>> L
['zebra', 'kite', 'air', 'ink', 'boat', 'coat', 'purple']
>>> def func(s):
	return s[-1]

>>> L.sort(key=func)
>>> L
['zebra', 'kite', 'purple', 'ink', 'air', 'boat', 'coat']
>>> #################################################################
>>> T = [12, 34, 56, 78, 100]
>>> def C2F(c):
	return c * 1.8 + 32

>>> TF = map(C2F, T)
>>> TF
<map object at 0x0000023CE36C8B00>
>>> list(TF)
[53.6, 93.2, 132.8, 172.4, 212.0]
>>> prices = ['12,345.00', '32,12,443.00', '1,23,333.00']
>>> sum(prices)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    sum(prices)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> def clean(x):
	m = x.split(',')
	return float(''.join(m))

>>> prices = clean(prices)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    prices = clean(prices)
  File "<pyshell#30>", line 2, in clean
    m = x.split(',')
AttributeError: 'list' object has no attribute 'split'
>>> prices = map(clean, prices)
>>> prices
<map object at 0x0000023CE383ACC0>
>>> list(prices)
[12345.0, 3212443.0, 123333.0]
>>> sum(prices)
0
>>> sum(list(prices))
0
>>> prices
<map object at 0x0000023CE383ACC0>
>>> prices = list(prices)
>>> prices
[]
>>> list(prices)
[]
>>> prices = ['12,345.00', '32,12,443.00', '1,23,333.00']
>>> p = map(clean, prices)
>>> p = list(p)
>>> p
[12345.0, 3212443.0, 123333.0]
>>> sum(p)
3348121.0
>>> #####################################################
>>> L = list(range(1, 100))
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> LF = filter(lambda n:n%11, L)
>>> LF
<filter object at 0x0000023CE383ACF8>
>>> list(LF)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]
>>> LF = filter(lambda n:not n%11, L)
>>> list(LF)
[11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> ###################################################################
>>> person = ('VIjay', 'Prasad', 'Chandan')
>>> address = ('Vijaynagar', 'RR Nagar', 'Rajajinagar')
>>> data = zip(person, address)
>>> data
<zip object at 0x0000023CE387EFC8>
>>> list(data)
[('VIjay', 'Vijaynagar'), ('Prasad', 'RR Nagar'), ('Chandan', 'Rajajinagar')]
>>> 
