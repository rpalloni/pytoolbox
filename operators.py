# unpacking operator
a = [8, 2, 6, 5, 4]
[*range(len(a))]

arr1 = range(10)
print(arr1)
[*arr1]

arr2 = range(0, 10, 2)
[*arr2]

arr2 = range(10, 0, -1)
print(*arr2)

# slice [index] and range slice [start:stop:step] operators
arr3 = [1, 2, 3, 4, 5, 6]
arr3[2] # index starts at 0
arr3[-1] # last
arr3[1:3] # take items 2-3, upper bound noninclusive
arr3[0:-1] # take all but the last
arr3[::2]
arr3[::-1]

# modulus: reminder of division
arr = [1, 2, 3, 4, 5]
list(filter(lambda x: x % 2 == 0, arr))

# floor division (no decimals)
x = 13
y = 3
print(x//y)

print(x/y)
print(x % y) # reminder
res, rem = divmod(x, y)
print(f'result:{res}, reminder:{rem}')

# pop: get and remove
arr4 = [5, 3, 6, 2, 10]
arr4.pop(2) # get element by index
arr4        # removed in arr

# enumerate
for index, i in enumerate('pippo'):
    print(index, i)

names = ['Bob', 'Alice', 'Guido']
for index, value in enumerate(names):
    print(f'{index}: {value}')

names = ['Bob', 'Alice', 'Guido']
for index, value in enumerate(names, 1):
    print(f'{index}: {value}')

list(enumerate(names))

# reverse and sorted
arr5 = [1, 2, 3, 4, 5]
list(reversed(arr5))

arr6 = [7, 4, 2, 9, 5]
sorted(arr6)

words = ['banana', 'pie', 'Washington', 'book']
sorted(words, key=len)
