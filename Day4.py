import math as m  <-------- # renames the import to m
  print(m.cos(m.pi)) # <-------- # uses the new name and you must put the name before the tool (ie. m.pi)
  
  
  
  def add(*args):    <------- # args is a tuple that is paired with a * to make it a variable length argument
    print(args)
    returm (sum(args))
  
  print(add(5,7))
  
  
  def myCar(**kwargs):
    print("I drive a {} {} [}.fomat(kwargs['year'], kwargs['make'], kwargs['model']))
          
  myCar(year='1981', make = 'Toyota', model 'Tacoma') 
          
          
  
  y = lambda m: n + 100   <--------- # lambda Makes a simple function

          
          
          
  s = {1,5,8,9,8,5,5,5,5,5,5,5}    <-------- # {} represent a set
  s
  {1,5,8,9}                  <------------ #Notice there are no duplicates in the actual set
  5 in s
  True
  10 in s
  False
  s.add (11)
  {4.5.8.9.11}
  s.remove (9)
  {4,5,8,11}
          
          
          
  myDict = {'I':1, 'V':5, 'X':10}
  myDict[I]
  1
  myDict['L'] = 50
  {'I':1, 'V':5, 'X':10, 'L':50}
  myDict['L'] = 'Wrong'
  {'I':1, 'V':5, 'X':10, 'L':'Wrong'}
  for i in myDict:
          print(i)
  I
  V
  X
  L
  for i in myDict
          print (myDict[i])
  1
  5
  10
  Wrong
