# type hints: modern python feature

from collections import namedtuple
from typing import Optional, Iterable

# https://docs.python.org/3/library/collections.html#collections.namedtuple
Order = namedtuple('Order', 'item, price')


def get_cost(orders):
    total = 0

    for o in orders:
        total += o.price

    return total


def main() -> None:

    dinner = [Order('Pizza', 20.5), Order('Beer', 9.8), Order('Beer', 9.8)]
    breakfast = [Order('Pancakes', 11.3), Order('Bacon', 4), Order('Coffee', 3.6), Order('Coffee', 3.6)]

    print(f"Dinner cost EUR {get_cost(dinner):,.02f}")

    print(f"Breakfast cost EUR {get_cost(breakfast):,.02f}")

if __name__ == '__main__':
    main()
