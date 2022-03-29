import datetime
from typing import List

from dateutil.parser import parse

order_json = {
    'item_id': '123',                   # try 'xyz'
    'dt_created': '2018-09-30 12:20',
    'page_visited': [1, 2, '3'],        # mix
    'price': 17.22
}


class Order:

    def __init__(self, item_id: int, dt_created: datetime.datetime, page_visited: List[int], price: float):

        try:
            self.item_id = int(item_id)
        except ValueError:
            raise Exception('item_id not valid, must be int.')

        try:
            self.dt_created = parse(dt_created)
        except:
            raise Exception('dt_created not valid, must be datetime.')

        try:
            self.price = float(price)
        except ValueError:
            raise Exception('price not valid, must be float.')

        try:
            self.page_visited = [int(p) for p in page_visited]
        except:
            raise Exception('page_visited not valid, must be an iterable of int.')

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return isinstance(other, Order) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return isinstance(other, Order) and self.__dict__ == other.__dict__


def main() -> None:
    o = Order(**order_json)
    print(o)


if __name__ == '__main__':
    main()

# {'item_id': 123, 'dt_created': datetime.datetime(2018, 9, 30, 12, 20), 'price': 17.22, 'page_visited': [1, 2, 3]}
