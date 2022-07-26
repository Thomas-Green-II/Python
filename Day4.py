import math as m  <-------- # renames the import to m
  print(m.cos(m.pi)) # <-------- # uses the new name and you must put the name before the tool (ie. m.pi)

          
          
#----------------------------------RIPL STUFF FROM SOMEONE SMARTER------------------------------------
'''
￼
￼
Python 3.6.9 () 
[] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> math.sqrt(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
#can see needs to import math

>>> import math
>>> math.sqrt(9)
3.0
>>> math.sqrt(10)
3.1622776601683795
>>> int(math.sqrt(10))
3



>>> #IMPOTRS
-----------------------------------
... import math as m
>>> # math is import, m is 'nickname' for import so you can m.sqrt() instead of math.sqrt()
... #can also imort only certain functions / things from modiles
... from math import cos,pi
>>> #import everything ans use it as a built in function
... from math import *
>>> #can create own imports to do whatever
... #create own import by making a script ( vim ___.py)



... #FUNCTIONS
... -------------------------------
>>> #variable legnth argument is for when unknown ammount of var to function
... def add(*args):
...     print(args)
...     return (sum(args))
... 
>>> #*args is variable length argument
... #args is a tuple here
... 
>>> x = add(2,4,5,5,6,4,2)
(2, 4, 5, 5, 6, 4, 2)
>>> x
28



>>> #keyword arguments
-----------------------------------------------
... #**kwargs is keyword argument
>>> def myCar(**kwargs):
...     print("I drive a {} {} {}".format(kwargs['year'], kwargs['make'], kwargs['model']))
... 
>>> myCar(year='1999', make='Ford', model ='mustang')
I drive a 1999 Ford mustang
>>> #lambda -------------
... def lambdaEX(n):
...     y = lambda n: n + 100
...     print(y(25))
... 



#LAMBDA        #stil dont know that this is
-------------------------------
>>> def incrementor(n):
...     return lambda x: x + n
... 
>>> funTime = incrementor(42)
>>> funTime(10)
52



>>> # SETS 
----------------------------------
... #set is unorganized set of collections
... #list would be organized by index value
... # you cannoy pull things out of a set, all you can do is determine if things are in it
... #cannot have duplicates in set
... s = {1,2,3,4,5,6,7,4,6,8,9,0}
>>> s
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> 10 in s
False
>>> 1 in s
True
>>> s.add(100)
>>> s
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100}
>>> s.remove(100)
>>> s
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s1 = {1,4,6,5,7,8}
>>> s1 = {1,4,6,5,7,8,10,11,23}
>>> s.union(s1)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 23}
>>> s.difference(s1)
{0, 9, 2, 3}
>>> s.intersection(s1)
{1, 4, 5, 6, 7, 8}
>>> myList = [4,4,4,4,2,2,7,4,5,8,9]
>>> myList
[4, 4, 4, 4, 2, 2, 7, 4, 5, 8, 9]
>>> set(myList)
{2, 4, 5, 7, 8, 9}




>>> #DICTONARY
-------------------------------------------------
... #organized by a key
... #uses key value pairs
... #list would use index to otganize and use
... myDict = {'I':1, 'V':5, "x':10}
  File "<stdin>", line 5
    myDict = {'I':1, 'V':5, "x':10}
                                  ^
SyntaxError: EOL while scanning string literal
>>> myDict = {'I':1, 'V':5, 'X':10}
>>> myDict['I']
1
>>> myDict['V']
5
>>> myDict
{'I': 1, 'V': 5, 'X': 10}
>>> myDict['L'] = 50
>>> myDict
{'I': 1, 'V': 5, 'X': 10, 'L': 50}
>>> myDict['L'] = 'Wrong'
>>> myDict
{'I': 1, 'V': 5, 'X': 10, 'L': 'Wrong'}
>>> for i in myDict:
...     print(i)
... 
I
V
X
L
>>> for i in myDict:
...     print(myDict[i])
... 
1
5
10
Wrong
>>> del myDict['L']
>>> myDict
{'I': 1, 'V': 5, 'X': 10}
>>> myStr = 'the quick brown fox junmps over the lazy dog'
>>> #can use DICTONARY to count how many instances of a char ina  string
... 
>>> for i in myStr:
...     if i in myDict:
...             myDict[i] += 1
...     else:
...             myDict[i] = 1
... 
>>> myDict
{'I': 1, 'V': 5, 'X': 10, 't': 2, 'h': 2, 'e': 3, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 2, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}
>>> #this will a letter and then a number for tha number, the numbers are how many times the letter appeared in myStr



... #UNPACKING----------------------------
... 
>>> 
>>> myList
[4, 4, 4, 4, 2, 2, 7, 4, 5, 8, 9]
>>> print (*myList)
4 4 4 4 2 2 7 4 5 8 9
>>> myNum = [4,2,0,5,5,5,1,7,7,5]
>>> print('({}{}{})-{}{}{}-{}{}{}{}'.format(*myNum))
(420)-555-1775
>>> #putting a star in front of list will unpack list, for argument unpacking
... #can do with strings too
... 
>>> print('({}{}{})-{}{}{}-{}{}{}{}'.format(*myStr))
(the)- qu-ick 
>>> #unpacking goes through list and passes index stuff
... 
'''
