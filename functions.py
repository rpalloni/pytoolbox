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
def outer(x,y):
    def inner(a,b):
        return (a + b)
    print(inner(x,y))

outer(3, 6)

def external(x):
    y = 20
    def internal():
        print(x + y)
    internal()

external(5)