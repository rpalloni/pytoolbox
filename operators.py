# unpacking operator
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
