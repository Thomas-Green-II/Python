!/usr/bin/env python3

def q1(floatstr):
    '''
    TLO: 112-SCRPY002, LSA 3,4
    Given the floatstr, which is a comma separated string of
    floats, return a list with each of the floats in the 
    argument as elements in the list.
    '''
    return [float(i) for i in(floatstr.split(','))]

                    # or

    newList = []
    for i in floatstr.split(',')
        newList.append(float(i))

    return newList

                    # or

    return list(map(float, floatstr.split(',')))  # <-----map takes two arguments, the one on the left is a function and the one on the right is the iterable object. The function then applies itself using list(map( to everything in that iterable object.

def q2(*args):
    '''
    TLO: 112-SCRPY006, LSA 3
    TLO: 112-SCRPY007, LSA 4
    Given the variable length argument list, return the average
    of all the arguments as a float
    '''
    return sum(args)/len(args)

def q3(lst,n):
    '''
    TLO: 112-SCRPY004, LSA 3
    Given a list (lst) and a number of items (n), return a new 
    list containing the last n entries in lst.
    '''
    x = lst[-n::]  # <------- [start:stop:step]
    return x

def q4(strng):
    '''
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY006, LSA 3
    Given an input string, return a list containing the ordinal numbers of 
    each character in the string in the order found in the input string.
    '''
    x = []
    for i in strng:
        x.append(ord(i))

    return x

                #or
                                                                                                                                   1,15          Top
return [ord(i) for i in strng]

                #or

    return list(map(ord,strng)

def q5(strng):
    '''
    TLO: 112-SCRPY002, LSA 1,3
    TLO: 112-SCRPY004, LSA 2
    Given an input string, return a tuple with each element in the tuple
    containing a single word from the input string in order.
    '''
    strng = strng.split(" ")
    return tuple(strng)



def q6(catalog, order):
    '''
    TLO: 112-SCRPY007, LSA 2
    Given a dictionary (catalog) whose keys are product names and values are product
    prices per unit and a list of tuples (order) of product names and quantities,
    compute and return the total value of the order.

    Example catalog:
    {
        'AMD Ryzen 5 5600X': 289.99,
        'Intel Core i9-9900K': 363.50,
        'AMD Ryzen 9 5900X': 569.99
    }

    Example order:
    [
        ('AMD Ryzen 5 5600X', 5), 
        ('Intel Core i9-9900K', 3)
    ]

    Example result:
    2540.45 

    How the above result was computed:
    (289.99 * 5) + (363.50 * 3)
    '''
    total = 0
    for product, quantity in order:
        total += catalog[product] * quantity
    return total

                # or

    return sum(catalog[product]*quantity for product,quantity in order)

                                                                                                                                   109,0-1       43%
def q7(filename):
    '''
    TLO: 112-SCRPY005, LSA 1
    Given a filename, open the file and return the length of the first line 
    in the file excluding the line terminator.
    '''

    with open(filename, "r")as fp:
        length = len(readlines()[0])-1)
    return length



def q8(filename,lst):
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY005, LSA 1
    Given a filename and a list, write each entry from the list to the file
    on separate lines until a case-insensitive entry of "stop" is found in 
    the list. If "stop" is not found in the list, write the entire list to 
    the file on separate lines.
    '''
    with open(filename, 'w')as fp:
        for i in lst:
            if i.lower() == 'stop':
                break
            fp.write(f'{i}\n') # f is the shorthand for .format
            # fp.write('{}\n'.format(i))



def q9(miltime):
    '''
    TLO: 112-SCRPY003, LSA 1
    Given the military time in the argument miltime, return a string 
    containing the greeting of the day.
    0300-1159 "Good Morning"
    1200-1559 "Good Afternoon"
    1600-2059 "Good Evening"
    2100-0259 "Good Night"
    '''
    if miltime >= 300 and miltime <= 1159:
        return "Good Morning"
    elif miltime >= 1200 and miltime <= 1559:
        return "Good Afternoon"
    elif miltime >= 1600 and miltime <= 2059:
        return "Good Evening"
    else:
        return "Good Night"

def q10(numlist):
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1
    Given the argument numlist as a list of numbers, return True if all 
    numbers in the list are NOT negative. If any numbers in the list are
    negative, return False.
    '''
    for i in numlist:
        if i < 0:
            return False
        else:
            return True

        #or

    return all(map(lambda x: x >=0,numlist)
                                                                                                                                
