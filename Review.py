myIP = 192.168.28.50
myIP.split('.') # <------- splits ip on the .
if int(myIP.split('.')[-1] <= 62:
       print("This IP falls within that range"


#Dictionaries
myDict = {'PVT':'E-1'}
myDict['PVT']
'E1'
myDict['PFC'] = 'E-2'
myDict = {'VT':'E-1', 'PFC':'E-2'}
for i in myDict
  print(myDict[i])
E1
E2

for i in myDict:
   print(myDict(i))
PVT
PFC
             

             
#format
first = 'aaron'
middle = 'andrew'
last = 'anderson'
domain = 'cornetto'             
'{}.{}.{}@{}.com.format(first, middle[0], last, domain)             
             

# SLICING: list vs range

# LIST
mylist = ['195' '168' '28' '50']
myOctets[0:3]
['195' '168' '28']
[:-1] <--------- # start at the beginning of the list and stop at the end of the list
             
# RANGE
list(range(0,10))
[0,1,2,3,4,5,6,7,8,9]
 

# FILEIO
with open('myfile.txt, 'r') as fp:
  print(read*([:3])

      
# Copy from one file to another
infile = 'myfile.txt
outfile = 'outfile.txt'
with open(infile, 'r') as fp0:
  lines0 = fp0.readlines()
with open(outfile, 'w')as fp:
  fp.writelines(lines0)
        
        OR
        
with open(infile, 'r') as fp0:
    with open(outfile, 'w')as fp:
        fp.writelines(fp0.readlines()[2]) <-----# readlines puts the text in a list and the index of 2 grabs the second index of that list
        
        
