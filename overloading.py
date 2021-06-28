# how the same built-in operator or function shows different behavior for objects of different classes
1 + 2
'Code' + 'Python'
3 * 2
'Python' * 3

# dunder (double under) methods:
# len() >> __len__()
# str() >> __str__()
# + >> __add__()
# [] >> __getitem__()
# ...

a = 'Code Python'
b = ['Code', 'Python']
len(a)
a.__len__()
b[0]
b.__getitem__(0)
dir(a) # full list of methods and dunders for a string

# By default, most of the built-ins and operators will not work with objects of classes
class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

order = Order(['banana', 'apple', 'mango'], 'Emma')
len(order) # error!

# You must override the corresponding special methods in the class definition:

############################ __len__() ##############################
class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart) # instead of defining a get_cart_len()

order = Order(['banana', 'apple', 'mango'], 'Mark')
len(order)
order.__len__()

############################ __str__() ##############################
class Vector:
    def __init__(self, x_coor, y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor

    def __str__(self):
        return f'{self.x_coor}x:{self.y_coor}y'

vector = Vector(3, 4)
str(vector)
vector.__str__()

############################ __repr__() ##############################
class Vector:
    def __init__(self, x_coor, y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor

    def __repr__(self):
        return f'Vector({self.x_coor}, {self.y_coor})'

vector = Vector(3, 4)
repr(vector)

v = eval(repr(vector))
v.x_coor
v.y_coor

############################ __bool__() ##############################
class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __bool__(self):
        return len(self.cart) > 0

order1 = Order(['banana', 'apple', 'mango'], 'Mark')
order2 = Order([], 'Daniel')

bool(order1)
bool(order2)

for order in [order1, order2]:
    if order:
        print(f"{order.customer}'s order is processing...") # Truthy
    else:
        print(f"Empty order for customer {order.customer}") # Falsey

######################## + __add__() ##############################
a = 'Code'
a + 'Python'
a
a = a + 'Python' # add requires explicit assignment
a

class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __add__(self, other):
        new_cart = self.cart.copy()
        new_cart.append(other)
        return Order(new_cart, self.customer)

order = Order(['banana', 'apple'], 'Mark')
(order + 'orange').cart
order.cart # no addition
order.customer

order = order + 'orange' # explicit assignment
order.cart

######################## += __iadd__() ##############################
class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __iadd__(self, other): # __isub__(), __imul__(), __idiv__()
        self.cart.append(other)
        return self

order = Order(['banana', 'apple'], 'John')
order += 'mango'
order.cart


######################## [] __getitem__() ##############################
class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __getitem__(self, key): # key: integer | string | slice obj
        return self.cart[key]

order = Order(['banana', 'apple', 'orange', 'mango'], 'Joe')
order[0]
order[-1]
order[2:]
