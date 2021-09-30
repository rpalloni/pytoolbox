import datetime
from dataclasses import dataclass
from typing import List, Optional

order_json = {
    'item_id': '123',                   # str
    'dt_created': '2018-09-30 12:20',
    'page_visited': [1, 2, '3'],        # mix
    'price': 17.22
}

# https://docs.python.org/3/library/dataclasses.html#module-dataclasses
# This module provides a decorator and functions for automatically adding generated special methods
# such as __init__() and __repr__() to user-defined classes (see also data_class.py)

@dataclass
class Order:
    item_id: int
    dt_created: Optional[datetime.datetime]
    page_visited: List[int]
    price: float

    def __post_init__(self):
        # controls here
        pass


def main() -> None:
    o = Order(**order_json)
    print(o)


if __name__ == "__main__":
    main()

# data silently accepted despite class attribute definition
# Order(item_id='123', dt_created='2018-09-30 12:20', page_visited=[1, 2, '3'], price=17.22)
