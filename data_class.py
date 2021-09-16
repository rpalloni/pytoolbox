### Compare data_classes and regular_classes

from dataclasses import dataclass

@dataclass
class DataClassCard:
    # attribute: type = default_value
    rank: str = 'A'
    suit: str

    # default implementation for init, repr and comparison
    # __init__()
    # __repr__()
    # __eq__()

queen_of_hearts = DataClassCard('Q', 'Hearts')
queen_of_hearts.rank
queen_of_hearts
queen_of_hearts == DataClassCard('Q', 'Hearts') # true


class RegularClassCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        # boilerplating...

queen_of_hearts = RegularClassCard('Q', 'Hearts')
queen_of_hearts.rank
queen_of_hearts
queen_of_hearts == RegularClassCard('Q', 'Hearts') # false ?!?!?


class RegularClassCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    # to be added for representation and comparison
    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')
    
    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)

queen_of_hearts = RegularClassCard('Q', 'Hearts')
queen_of_hearts.rank
queen_of_hearts
queen_of_hearts == RegularClassCard('Q', 'Hearts') # true


### NamedTuple as alternative to DataClass
from collections import namedtuple

NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])

queen_of_hearts = NamedTupleCard('Q', 'Hearts')
queen_of_hearts.rank
queen_of_hearts
queen_of_hearts == NamedTupleCard('Q', 'Hearts')

# tuple lacks of type awareness
NamedTuplePerson = namedtuple('Person', ['firstname', 'lastname'])
queen_of_hearts == NamedTuplePerson('Q', 'Hearts') # true ??!?!

# tuple is immutable
queen_of_hearts.rank = 'A' # cannot set attribute


### DataClasses stuff

# dynamic typing: type not enforced!
@dataclass
class GeoPosition:
    name: str
    lon: float = 0.0
    lat: float = 0.0

GeoPosition('Oslo', 10.8, 59.9)
GeoPosition('New York', 'test', 120) # no error

# data structures as attributes
from typing import List

@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'

@dataclass
class Deck:
    cards: List[PlayingCard]

queen_of_hearts = PlayingCard('Q', 'Hearts')
ace_of_spades = PlayingCard('A', 'Spades')
two_cards_deck = Deck([queen_of_hearts, ace_of_spades])



