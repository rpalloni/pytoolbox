# The function takes in iterables as arguments and returns an iterator.
# The iterator generates a series of tuples containing elements from each iterable.
numbers = [1, 2, 3] # iterable
letters = ['a', 'b', 'c'] # iterable
zipped = zip(numbers, letters) # iterator
type(zipped)
list(zipped)

s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
list(zip(s1, s2))

integers = [1, 2, 3]
letters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zipped = zip(integers, letters, floats)  # Three input iterables
list(zipped)

# build dict
fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '32', 'Python Developer']
a_dict = dict(zip(fields, values))
a_dict

values2 = [['John', 'Doe', '32', 'Python Developer'], ['Bob', 'Roi', '25', 'Java Developer']]
dev_dict = [dict(zip(fields, sublist)) for sublist in values2]
dev_dict
list(map(lambda x : dict(zip(fields, x)), values2))

list(zip(range(5), range(100))) # unequal lenght: shortest rule

from itertools import zip_longest
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
list(zipped)

# loop over multiple iterables (list)
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print(f'Letter: {l} - Number: {n}')

# loop over multiple iterables (dict)
dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Fly', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1, '|', k2, '->', v2)

# unzip with unpacking operator *
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
numbers
letters

# zip and sort
letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]
data1 = sorted(zip(letters, numbers)) # sort by letters
data2 = sorted(zip(numbers, letters)) # sort by numbers
data1
data2

# calculation in pairs
total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]
for sales, costs in zip(total_sales, prod_cost):
    profit = sales - costs
    print(f'Total profit: {profit}')
