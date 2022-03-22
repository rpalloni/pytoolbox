# any number of positional arguments
# *args packs the positional arguments into a tuple
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

l1 = [1, 2, 3, 4, 5]
sum_many(*l1) # unpacking

# any number of keyword argument
# **kwargs packs the keyword arguments into a dictionary
def profile(**kwargs):
    '''print profile with any number of attributes'''
    for key, value in kwargs.items():
        print(key, ":", value)

profile(firt_name='John', last_name='Doe', age=25, job='tester')

# args and kwargs
def cheeseshop(kind, *arguments, **keywords):
    print("-> Do you have any", kind, "?")
    print("-> I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("<->" * 10)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger")

cheeseshop("Limburger",
           "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# nested functions
def outer(x, y):
    def inner(a, b):
        return (a + b)
    print(inner(x, y))

outer(3, 6)

def external(x):
    y = 20

    def internal():
        print(x + y)
    internal()

external(5)


# closure
def add(x, y):
    # do_add is a closure
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add


def generate_power(number):
    def nth_power(power):
        return number ** power
    return nth_power

raise_two = generate_power(2) # generate_power returns a function
raise_three = generate_power(3)

raise_two(2)

# function as parameter of another function
def sum_num(a, b):
    print(a + b)

def handler(f, x, y):
    f(x, y)

handler(sum_num, 4, 5)
