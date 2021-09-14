# compare data_classes and regular_classes

from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str

queen_of_hearts = DataClassCard('Q', 'Hearts')
queen_of_hearts.rank

queen_of_hearts

queen_of_hearts == DataClassCard('Q', 'Hearts') # true


class RegularClassCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

queen_of_hearts = RegularClassCard('Q', 'Hearts')
queen_of_hearts.rank

queen_of_hearts

queen_of_hearts == RegularClassCard('Q', 'Hearts') # false ?!?!?


class RegularClassCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # required to allow comparison
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
