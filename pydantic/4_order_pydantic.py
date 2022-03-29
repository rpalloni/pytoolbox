import datetime
from typing import List, Optional

from pydantic import BaseModel

order_json = {
    'item_id': '123',                   # str
    'dt_created': '2018-09-30 12:20',
    'page_visited': [1, 2, '3'],        # mix
    'price': 17.22
}


class Order(BaseModel):
    item_id: int
    dt_created: Optional[datetime.datetime]
    page_visited: List[int] = []
    price: float


def main() -> None:
    o = Order(**order_json)
    print(o)


if __name__ == '__main__':
    main()

# data types solved according to class attributes types
# item_id=123 dt_created=datetime.datetime(2018, 9, 30, 12, 20) page_visited=[1, 2, 3] price=17.22
