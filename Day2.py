#!/usr/bin/python3

user_input = input("Please enter a number to translate between Farenheit and Celsius: ")
user_input = int(user_input)

Which_one = input("Is this Farenheit or Celsius?")

if Which_one == "Celsius":
    Celsius_Farenheit = ((user_input * 1.8) + 32) 

    print ("Your temperature in Farenheit is {}".format(Celsius_Farenheit))

elif Which_one == "Farenheit":
    Farenheit_Celsius = ((user_input - 32) * 0.5556)   # <------- When doing math do it like this

    print ("Your termperature in Celsius is {}".format(Farenheit_Celsius))
else:
    print ("Please type Farenheit or Celsius")                                              
    
    
NEW SCRIPT (while loops)
    |
    |
    V
#!/bin/bash/python3

count = 0

while count < 10:
    count += 1
    print("the count is: {} ".format(count))
    break
 
NEW SCRIPT
    |
    |
    V
#!/bin/bash/python3

mylist = list(range(20))

newlist= []
for num in mylist:   # <--------- num is a local variable for that loop
  print(num*3)
  newlist.append(num * 3) # <---------- append adds to the end of an existing list
    print(newlist)
    

NEW SCRIPT
    |
    |
    V
 #!/usr/bin/env python3
  
 def guess_number(n):   # <--------- Funtion
     Wrong = True
     while(Wrong):      # <-------- While Loop
         
          game = input("Type a random number between 0 and 100: ")
         game = int(game)
         
          if game > n and game > 100:
             print ("Higher than than 100, please stay inside of the range")
       
         elif game > n:
             print ("Too high Please try again")
         
         elif game < n and game < 0:
             print ("Lower than 0, please stay inside of the range")
            
         elif game < n:
             print ("Too low Please try again")
             
         else:
             print ("WIN")
             Wrong = False   # <---------- Indicator that the while loop stops
  guess_number(23)          # <---------- function call

  NEW SCRIPT
      |
      |
      V

l = list(range(0-256))
counter = 0               
for num in l:
    l[counter] = str(255 - int(x))      # <------------ Counter is used as a local variable to represent the index of the list being altered
    counter += 1           # <-------------- Symbolizes the movement of index position instead of staying still and just replacing the same index.
    
    
    newl = []
        for num in l:
            newl.append = str(255 - int(x))      # <--------- .append appends the string in this line to the end of the empty string mentioned in 94
            return newl

  
NEW SCRIPT
    |
    V 
    
#!/usr/bin/python3

with open('test.txt', 'r')as myfile:
    content = myfile.read(#)    # <------------ read, readline, readlines  =  read the file, read the first line, or read every character of the lines
                                            #    including their symbols. The '#' indicates a possible number of byytes wanted to be read from the file.
    print(content)
        
        
#!/usr/bin/python3
        
with open('test.txt', 'w')as myfile
        myfile.write("My first line") <------ Writes/Overwrites a file
