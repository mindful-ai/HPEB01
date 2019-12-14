Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'enterprise'
>>> type(s)
<class 'str'>
>>> ################################
>>> s1 = 'py'
>>> s2 = 'thon'
>>> s1 + s2
'python'
>>> s1 + 10
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s1 + 10
TypeError: can only concatenate str (not "int") to str
>>> s1 + str(10)
'py10'
>>> s1 * 3
'pypypy'
>>> len(s)
10
>>> s1
'py'
>>> s2
'thon'
>>> del s1
>>> del s2
>>> s1
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s1
NameError: name 's1' is not defined
>>> s2
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s2
NameError: name 's2' is not defined
>>> #################################################
>>> s
'enterprise'
>>> s[0]
'e'
>>> s[2]
't'
>>> s[-1]
'e'
>>> s[len(s)]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s[len(s)]
IndexError: string index out of range
>>> s[len(s) - 1]
'e'
>>> s[3:7]
'erpr'
>>> s[0:3]
'ent'
>>> s[:3]
'ent'
>>> s[6:9]
'ris'
>>> s[6:10]
'rise'
>>> s[6:]
'rise'
>>> s[:]
'enterprise'
>>> s[::2]
'etrrs'
>>> s[2:5] + s[-3:-1]
'teris'
>>> d = '13 OCT 2019'
>>> d = '13/10/2019'
>>> d.split('/')
['13', '10', '2019']
>>> D = d.split('/')
>>> D[0] + D[-1]
'132019'
>>> ' '.join([D[0], D[-1])
	 
SyntaxError: invalid syntax
>>> ' '.join([D[0], D[-1]])
'13 2019'
>>> s
'enterprise'
>>> s[::-1]
'esirpretne'
>>> s[::-2]
'eipen'
>>> ###################################################
>>> s
'enterprise'
>>> s.upper()
'ENTERPRISE'
>>> s.lower()
'enterprise'
>>> s.capitalize()
'Enterprise'
>>> s1 = '123'
>>> s2 = 'A23F'
>>> s3 = '&^%&^'
>>> s4 = ' '
>>> s1.isdigit()
True
>>> s2.isdigit()
False
>>> s2.isalpha()
False
>>> s2.isalnum()
True
>>> s3.isspace()
False
>>> s4.isspace()
True
>>> s3
'&^%&^'
>>> type(s3)
<class 'str'>
>>> name = 'Grace Sharon'
>>> name.isalpha()
False
>>> name
'Grace Sharon'
>>> 'ace' in name
True
>>> url = 'www.hpe.com'
>>> url.startswith('http')
False
>>> s5 = 'Jack 98'
>>> s5.replace(' ', '-')
'Jack-98'
>>> s5.replace(' ','')
'Jack98'
>>> a = 'This is a text dated 11/9/1999 15:30 addressed to Mr. Jack Daniels'
>>> s
'enterprise'
>>> a
'This is a text dated 11/9/1999 15:30 addressed to Mr. Jack Daniels'
>>> len(a)
66
>>> import re
>>> pattern = r'/d/d\/d/d\/d/d'
>>> re.find(pattern, a)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    re.find(pattern, a)
AttributeError: module 're' has no attribute 'find'
>>> re.search(pattern, a)
>>> pattern = r'\d\d\\\d\d\\\d\d'
>>> m = re.find(pattern, a)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    m = re.find(pattern, a)
AttributeError: module 're' has no attribute 'find'
>>> m = re.findall(pattern, a)
>>> m
[]
>>> m = re.findall(r'[0-9][0-9]:[0-9][0-9]', a)
>>> m
['15:30']
>>> m = re.findall(r'\d\d:\d\d', a)
>>> m
['15:30']
>>> m = re.finditer(r'\d\d:\d\d', a)
>>> m.group()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    m.group()
AttributeError: 'callable_iterator' object has no attribute 'group'
>>> m
<callable_iterator object at 0x000002F162C4E630>
>>> m.span()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    m.span()
AttributeError: 'callable_iterator' object has no attribute 'span'
>>> m.span()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    m.span()
AttributeError: 'callable_iterator' object has no attribute 'span'
>>> s.group(1)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    s.group(1)
AttributeError: 'str' object has no attribute 'group'
>>> m.group(1)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    m.group(1)
AttributeError: 'callable_iterator' object has no attribute 'group'
>>> m = re.finditer(r'(\d\d):(\d\d)', a)
>>> m
<callable_iterator object at 0x000002F162C334A8>
>>> m.group()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    m.group()
AttributeError: 'callable_iterator' object has no attribute 'group'
>>> m.group(1)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    m.group(1)
AttributeError: 'callable_iterator' object has no attribute 'group'
>>> #############################################################
>>> s
'enterprise'
>>> 'r' in s
True
>>> s.index('r')
4
>>> s.count('r')
2
>>> s.find('r')
4
>>> s.find('z')
-1
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.index('y')
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    s.index('y')
ValueError: substring not found
>>> s.find('y')
-1
>>> #################################################
>>> ipaddr = '192:168:1:10'
>>> ipaddr.replace(':', '.')
'192.168.1.10'
>>> L = ipaddr.split(':')
>>> L
['192', '168', '1', '10']
>>> '-'.join(L)
'192-168-1-10'
>>> 
