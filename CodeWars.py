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
    fat = (weight / (height ** 2))
    
    if fat <= 18.5:
        return "Underweight"
    elif fat <= 25.0:
        return "Normal"
    elif fat <= 30.0:
        return "Overweight"
    else:
        return "Obese"
