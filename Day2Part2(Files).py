#read = Gathers the document and presents it as a string, when using when you use an index it grabs the letter
#readlines = shows every character in the document, when using an index it grabs a line



# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total 
# number of characters in the file and save to the variable num.

  with open('travel_plans.txt', 'r')as myfile:
    num = len(myfile.read())
    
    
    
    

# We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
# Find the total number of words in the file and assign this value to the variable num_words.

with open('emotion_words.txt', 'r')as myfile:
    num_words = (myfile.read())
    num_words = num_words.split( )
    num_words = len(num_words)
    




# Assign to the variable num_lines the number of lines in the file school_prompt.txt.

with open('school_prompt.txt', 'r')as myfile:
    num_lines = len(myfile.readlines())
    




# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

with open('school_prompt.txt', 'r')as fp:
    beginning_chars = fp.read(30)               <---------- 30 indicates the number of bytes that are taken into account under the variable "beginning_chars"
  
  
  
  
  
# Using the file school_prompt.txt, assign the third word of every line to a list called three

with open('school_prompt.txt', 'r')as fp:
    third_word = (word[2] for word in (line.split( ) for line in fp))       <--------- Uses the second index (third word) as indicated by the [2]
    three = list(third_word)                                                           and uses local variables like "word" and"line" in the for loops
    
    
    

                                                            or




three = []                              <---------- make an empty list called three

with open('school_prompt.txt', 'r')as fp:
lines = fp.readlines()                  
for i in  lines.split():
  three.append(i.split()[2])            <--------- append the 2nd index (third element) to the list called three using the split on spaces
  
  




# Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

with open('school_prompt.txt', 'r')as fp:
    words = fp.read().split()
    
    for i in words: 
       if 'p' in i:
        p_words.append(i)
        
        
        
# Copy one file to another

with open('originalfile.txt', 'r')as fp0:
  contents = fp0.read()        <-------- # can be readlines but the write must be writelines
  
with open('newfile.txt', 'w')as fp1:
          fp1.write(contents)
        
