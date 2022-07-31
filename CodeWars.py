# sum() <--------- adds the numbers in a list together 
# %2 == 0 <--------- signifies if a number is even
return" ".join(words) <-------- # proper way to join a list with just a space in between each item
new = s.split(" ") <----------- # proper way to use split to set string "s" into a list based on spaces and calling it new
space = "".join(x.split()) <--------- # to get rid of spaces entirely
if (int(sum(arr) % 2)) == 0: <------------ # Given a list of integers, determine whether the sum of its elements is odd or even


# To reverse the order of an input series of numbers
def digitize(n):
    return [int(x) for x in reversed(str(n))]





#The function should return result of numbers after applying the chosen operation.
def basic_op(operator, value1, value2):
    if operator == '+':
        return(value1 + value2)
    elif operator == '-':
        return(value1 - value2)
    elif operator == '*':
        return(value1 * value2)
    elif operator == '/':
        return(value1 / value2)
    else:
        return("Please enter a new operator and numbers")

    
    
    
    
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral 
#perfect square is an integer n such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.    

def find_next_square(sq):
    import math as m
    
    return ((m.sqrt(sq) + 1)**2) if m.sqrt(sq).is_integer() else -1



# Write function bmi that calculates body mass index (bmi = weight / height2).
def bmi(weight, height):
    fat = (weight / (height ** 2))   <------------ #    "**" represents squaring
    
    if fat <= 18.5:
        return "Underweight"
    elif fat <= 25.0:
        return "Normal"
    elif fat <= 30.0:
        return "Overweight"
    else:
        return "Obese"
    
    
    
    
 # Given an array of integers, return a new array with each value doubled
def maps(a):
    b = []
     for item in a:
        b.append((int(item) * 2))
    return b

# Create a function which translates a given DNA string into RNA.
# For example:        "GCAT"  =>  "GCAU"
def dna_to_rna(dna):
    dna = list(dna)
    counter = 0
    for i in dna:
        if i == 'T':
            dna[counter] = 'U'
        counter += 1
    return ''.join(dna)


# Remove the first and last characters in a string
def remove_char(s):
    return s[1 : -1]


# Complete the solution so that it reverses the string passed into it.
def solution(string):
    return ''.join(list(reversed(string)))


# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
def count_sheep(n):
    s = ""
    i = 1
    while i <= n:
        s += str(i)+" sheep..."
        i += 1
    return s

# create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
def filter_list(l):
    new_list =[]
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list

# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers
def sum_mix(arr):
    return sum(int(x) for x in arr)


# You receive an array with your peers' test scores. Now calculate the average and compare your score!
def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them. The output should be two capital letters with a dot separating them.
def abbrevName(name):
    name=name.upper()
    n=name.split()
    return n[0][0]+'.'+n[1][0]

# Return the Smallest number in a list
def findSmallestInt(arr):
    return min(arr)

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1
def square_digits(num):
    lst = list(str(num))
    numbers = []
    for i in lst:
        numbers.append(str(int(i)**2))
    return int("".join(numbers))

# multiply numbers in a list together and return the result of the multiplication
def grow(arr):
    num = 1
    for x in arr:
        num = num * x
    return num

# Given an array of integers, find the one that appears an odd number of times
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
