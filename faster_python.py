import time

# faster algorithms
sum = 0
for x in range(1,100+1):
    sum += x
print(sum)

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
  
