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
