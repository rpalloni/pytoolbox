# any number of positional arguments
def sum_many(*args):
    '''sum any number of numbers'''
    s = 0
    for i in args:
        s += i
    print("sum is", s)

print(sum_many.__doc__) # docs strings
print(sum_many.__name__)

sum_many(1, 2, 3)
sum_many(1, 2, 3, 4, 5, 7, 8, 9, 10)

# any number of keyword argument
def profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)