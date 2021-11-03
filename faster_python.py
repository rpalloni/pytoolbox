import time
import random

n = 1000000
rng = range(1, n)
nr = [random.randint(0, 9) for i in rng]

# faster algorithms

start = time.time()
sum = 0
for x in range(1, n+1):
    sum += x
print(sum)
print(time.time() - start)

start = time.time()
print(n*(1+n)/2)
print(time.time() - start)


# faster python (code structures)

### 0 - create list/dict
start = time.time()
l1 = list() # dict()
print(time.time() - start)

start = time.time()
l2 = [] # {}
print(time.time() - start)

### 1 - count elements in list
start = time.time()
how_many = 0
for element in rng:
  how_many += 1
print(how_many)
print(time.time() - start)

start = time.time()
print(len(rng))
print(time.time() - start)

### 2 - filter a list
start = time.time()
output = []
for element in rng:
  if element % 2:
    output.append(element)
print(time.time() - start)

start = time.time()
list(filter(lambda x: x % 2, rng))
print(time.time() - start)

start = time.time()
[item for item in rng if item % 2]
print(time.time() - start)

### 3 - item in list
def check_number(number):
    for item in rng:
        if item == number:
            return True
    return False

start = time.time()
check_number(125)
print(time.time() - start)

start = time.time()
check_number(99999) # speed depends on item position => no constant lookup time
print(time.time() - start)

# use set for constant lookup time
MILLION_SET = set(rng)

start = time.time()
125 in MILLION_SET
print(time.time() - start)

start = time.time()
99999 in MILLION_SET
print(time.time() - start)

### 4 - remove duplicates
start = time.time()
unique = []
for item in nr:
    if item not in unique:
        unique.append(item)
print(time.time() - start)

start = time.time()
set(nr) # set conversion removes duplicates
print(time.time() - start)

### 5 - list sorting
start = time.time()
sorted(nr)
print(time.time() - start)

start = time.time()
nr.sort()
print(time.time() - start)

### 6 - apply function
def square(number):
    return number**2

start = time.time()
squares = [square(i) for i in rng] # call function i times
print(time.time() - start)

def squares():
    return [i**2 for i in rng] # call once

start = time.time()
squares()
print(time.time() - start)

### 7 - function vs lambda
def greet(name):
    return f'Hello {name}'

start = time.time()
greet('John')
print(time.time() - start)

lgreet = lambda name: f'Hello {name}'

start = time.time()
lgreet('John')
print(time.time() - start)

### 8 - check truthy
variable = True

start = time.time()
if variable == True:
    print('hello')
print(time.time() - start)

start = time.time()
if variable is True:
    print('hello')
print(time.time() - start)

start = time.time()
if variable:
    print('hello')
print(time.time() - start)

# falsy (False, None, zero, empty string, empty list)
start = time.time()
if len(nr) == 0:
    print('hello')
print(time.time() - start)

start = time.time()
if nr == []:
    print('hello')
print(time.time() - start)

start = time.time()
if not nr:
    print('hello')
print(time.time() - start)
