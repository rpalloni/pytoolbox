# https://realpython.com/python-enumerate/
names = ['Bob', 'Alice', 'Guido']
for index, value in enumerate(names):
    print(f'{index}: {value}')


names = ['Bob', 'Alice', 'Guido']
for index, value in enumerate(names, 1):
    print(f'{index}: {value}')


# implemented as a Python iterator
# generates its output elements lazily
# and one by one when they’re requested

names = ['Bob', 'Alice', 'Guido']
enumerate(names)

list(enumerate(names))


from enum import Enum
from enum import auto

class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

c = Colour.RED
print(c)
print(c.name)
print(c.value)
print(c is Colour.RED)
print(c is Colour.BLUE)

for name, member in Colour.__members__.items():
    print(name, member)

class Colour(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


c = Colour.RED
print(c.value)

# extend enum with methods
class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    def __str__(self):
        return self.name

    def colorize(self):
        return f"Let's paint everything in {self.name.lower()}"

c = Colour.RED
print(c)
print(c.colorize())


class Cards(Enum):
    clubs = 1
    diamonds = 2
    hearts = 3
    spades = 4

Cards = Enum('Cards', ['clubs', 'diamonds', 'hearts', 'spades'])


Color = Enum('Color', ['red', 'green', 'blue'])
Shape = Enum('Shape', ['circle', 'triangle', 'square', 'hexagon'])
def has_vertices(shape):
 	return shape != Shape.circle

has_vertices(Color.green)

# kinds of enum: IntEnum, IntFlag, Flag
from enum import IntEnum
from enum import IntFlag
from enum import Flag

class Colour(IntEnum):
    RED = 1
    GREEN = 2
    BLUE = 3

r = Colour.RED
b = Colour.GREEN
print(r < b)


class Permission(IntFlag):
    R = 4 # read
    W = 2 # write
    X = 1 # execute


RW = Permission.R | Permission.W
print(RW)
print(Permission.R + Permission.W)
print(Permission.R in RW)


class Colour(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    WHITE = RED | GREEN | BLUE


print(Colour.WHITE.name, Colour.WHITE.value)


# use enum to add more meaning to code

from http.client import HTTPResponse

def evaluate_response(response: HTTPResponse) -> str:
    if response.code() == 404:
        return "Not Found"
    elif response.code() == 502:
        return "???"
    elif response.code() == 400:
        return "???"
    else:
        return "Unknown Status Code"

# clear code
from enum import IntEnum

class HTTPCode(IntEnum):
    BAD_REQUEST = 400
    NOT_FOUND = 404
    BAD_GATEWAY = 502

def evaluate_response(response: HTTPResponse) -> str:
    if response.code() == HTTPCode.NOT_FOUND:
        return "Not Found"
    elif response.code() == HTTPCode.BAD_GATEWAY:
        return "???"
    elif response.code() == HTTPCode.BAD_REQUEST:
        return "???"
    else:
        return "Unknown Status Code"
