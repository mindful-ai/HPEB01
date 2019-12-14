Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> D
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    D
NameError: name 'D' is not defined
>>> import shelve
>>> p = shelve.open('data.db')
>>> D = p['mydata']
>>> D
{'name': 'Vijay', 'place': 'Vijaynagar', 'company': 'HPE', 'country': 'INDIA'}
>>> p.close()
>>> 
