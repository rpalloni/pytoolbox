import time

# faster algorithms
sum = 0
for x in range(1,100+1):
    sum += x
print(sum)

s = sum(range(1,100+1))
print(s)

print(100*(1+100)/2)

# faster python (banning for loops)

#1 count elements in list
how_many = 0
for element in ONE_MILLION_ELEMENTS:
  how_many += 1
print(how_many)

print(len(ONE_MILLION_ELEMENTS))

#2 filter a list
output = []
for element in MILLION_NUMBERS:
  if element % 2:
    output.append(element)
    
list(filter(lambda x: x % 2, MILLION_NUMBERS))

[item for item in MILLION_NUMBERS if item % 2]
  
#3 item in list
def check_number(number):
    for item in MILLION_NUMBERS:
        if item == number:
            return True
        return False
'''    
speed depends on item position => no constant lookup time
100 in MILLION_NUMBERS
100000 in MILLION_NUMBERS 
'''

MILLION_SET = set(MILLION_NUMBERS) # set has constant lookup time
100 in MILLION_SET
100000 in MILLION_SET

#4 remove duplicates
unique = []
for item in MILLION_ELEMENTS:
    if item not in unique:
        unique.append(item)
       
set(MILLION_ELEMENTS) # set conversion removes duplicates

#5 list sorting
sorted(MILLION_RANDOM_NUMBERS)

MILLION_RANDOM_NUMBERS.sort()

#6 apply function
def square(number):
    return number**2
squares = [square(i) for i in range(1000)] # call function i times

def squares():
    return [i**2 for i in range(1000)] # call once

#7 check truty
variable = True
if variable == True:
    print('Hello')
    
if variable is True:
    print('Hello')
    
if variable:
    print('Hello')
