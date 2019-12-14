Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'My name is {} and age is {}'.format('Purushotham', 36)
'My name is Purushotham and age is 36'
>>> 'My name is {} and age is {}'.format('Vijay', 26)
'My name is Vijay and age is 26'
>>> 'My name is {0} and age is {1}'.format('Vijay', 26)
'My name is Vijay and age is 26'
>>> 'My name is {1} and age is {0}'.format('Vijay', 26)
'My name is 26 and age is Vijay'
>>> 'My name is {0:10} and age is {1:5}'.format('Vijay', 26)
'My name is Vijay      and age is    26'
>>> 'My name is {0:>10} and age is {1:<5}'.format('Vijay', 26)
'My name is      Vijay and age is 26   '
>>> 'My name is {0:^10} and age is {1:^5}'.format('Vijay', 26)
'My name is   Vijay    and age is  26  '
>>> 'My name is {name:^10} and age is {age:^5}'.format(name='Vijay', age=26)
'My name is   Vijay    and age is  26  '
>>> template = 'My name is {name:^10} and age is {age:^5}'
>>> template.format('Ravi', 25)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    template.format('Ravi', 25)
KeyError: 'name'
>>> template.format(name='Ravi', age=25)
'My name is    Ravi    and age is  25  '
>>> template.format(name='Jay', age=35)
'My name is    Jay     and age is  35  '
>>> 
