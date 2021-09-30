import datetime
from typing import List

order_json = {
    'item_id': '123',                   # str
    'dt_created': '2018-09-30 12:20',
    'page_visited': [1, 2, '3'],        # mix
    'price': 17.22
}


class Order:

    def __init__(self, item_id: int, dt_created: datetime.datetime,
                 page_visited: List[int], price: float):
        self.item_id = item_id
        self.dt_created = dt_created
        self.page_visited = page_visited
        self.price = price

    def __str__(self):
        return str(self.__dict__)


def main() -> None:
    o = Order(**order_json)
    print(o)


if __name__ == "__main__":
    main()

# {'item_id': '123', 'dt_created': '2018-09-30 12:20', 'page_visited': [1, 2, '3'], 'price': 17.22}
