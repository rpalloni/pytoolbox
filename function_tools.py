# cached_property()
# transform a method of a class into a property whose value is computed once and then cached as a normal attribute
# similar to the built-in @property decorator, with the addition of caching
from functools import cached_property

class DataSet:
    def __init__(self, sequence_of_numbers):
        self._data = sequence_of_numbers

    @cached_property
    def stdev(self):
        return statistics.stdev(self._data)

    @cached_property
    def variance(self):
        return statistics.variance(self._data)


# lru_cache()
# Least-Recently-Used Cache
# I/O bound functions that are periodically called with the same arguments
from functools import lru_cache
import requests

@lru_cache(maxsize=32)
def get_pep(number: int) -> str:
    resource = f"http://www.python.org/dev/peps/pep-{number:04d}/"
    print(resource)
    try:
        with requests.get(resource) as s:
            return s.text
    except requests.HTTPError:
        return "Not Found"


list_of_peps = [8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991]

for n in list_of_peps:
    pep = get_pep(n)
    print(n, len(pep))

print(get_pep.cache_info())


# total_ordering()
# implement all comparison methods without declaration in class
from functools import total_ordering

@total_ordering
class Pythonista:
    firstname: str
    lastname: str

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pythonista):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))

    def __lt__(self, other: object):
        if not isinstance(other, Pythonista):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))

guido = Pythonista("Guido", "van Rossum")
brett = Pythonista("Brett", "Cannon")
print(guido > brett)


# partial()
# avoid full reimplementation for minimum changes
import math
from functools import partial

def euclidean_distance(point1: [int, int], point2: [int, int]) -> float:
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

euclidean_distance((2,2),(4,4))

zero_euclid = partial(euclidean_distance, (0, 0)) # origin distance
point = (1, 1)
print(zero_euclid(point))


# partialmethod()
# define methods without reimplementation
from functools import partialmethod

class Cell(object):
    def __init__(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)

    set_alive = partialmethod(set_state, True) # avoid def set_alive:
    set_dead = partialmethod(set_state, False) # avoid # def set_dead:

c = Cell()
c.set_alive()
print(c.alive)


# reduce()
from functools import reduce

def sum_many(*args):
    s = 0
    for i in args:
        s += i
    return s

iterable = [1, 2, 3, 4, 5]
sum_many(iterable) # error

result = reduce(sum_many, iterable)
print(result)


# singledispatch()
# transforms a function into a single-dispatch generic function
# a generic function is a function composed of multiple functions
# implementing the same operation for different types
from functools import singledispatch

@singledispatch
def mul(a, b):
    if type(a) is not type(b):
        return NotImplemented
    return a * b

@mul.register
def strtype(a: str, b: str):
    return a + b

print(mul(1, 2))
print(mul(1.5, 2.5))
print(mul("1", "2"))
print(mul(1, 1.0))


# singledispatchmethod()
# transforms methods
from functools import singledispatchmethod

class Negator:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate!!")

    @neg.register
    def neg_int(self, arg: int):
        return -arg

    @neg.register
    def neg_bool(self, arg: bool):
        return not arg


neg = Negator()
print(neg.neg(5))
print(neg.neg(True))
print(neg.neg("Hello"))

# update_wrapper()
# wraps()
# add decoration to wrapper to apply it to function

def show_args(f):
    '''docs decorator'''
    def wrapper(*args, **kwargs):
        print(f"Calling function {f.__name__} with {args} and {kwargs}")
        return f(*args, **kwargs)
    return wrapper

@show_args
def add(a: int, b: int) -> int:
    '''Add two numbers a and b and return the result'''
    return a + b

print(add(5, 1))
print(add.__doc__)
print(add.__name__)


def show_args(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f"Calling function {f.__name__} with {args} and {kwargs}")
        return f(*args, **kwargs)
    return wrapper

def add(a: int, b: int) -> int:
    '''Add two numbers a and b and return the result'''
    return a + b

print(add(5, 1))
print(add.__doc__)
print(add.__name__)