# Lambda: Anonymous Functions (unnamed) no def of a function > no name

# lambda <==> def
def add(x, y):
    return x+y
add(2, 3)

# f = lambda argument(s) : expression
def add(x, y): return x + y
add(2, 3)

(lambda x, y: x + y)(2, 3) # Immediately Invoked Function Expression

(lambda x: (x % 2 and 'odd' or 'even'))(3)

arr = [1, 2, 3, 4, 5]
list(filter(lambda x: x % 2 == 0, arr)) # modulus: reminder of division

def full_name(first, last): return f'Full name: {first.title()} {last.title()}'
full_name('roberto', 'palloni')

# https://realpython.com/python-lambda/#map
list(map(lambda x: x*2, [1, 2, 3, 4])) # map(function_object, iterable1, iterable2,...)

list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))

fields = ['name', 'last_name', 'age', 'job']
records = [['John', 'Doe', '45', 'Python Developer'], ['Bob', 'Roi', '25', 'Java Developer']]
list(map(lambda x: dict(zip(fields, x)), records))

# https://realpython.com/python-lambda/#filter
list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])) # filter(function_object, iterable)

fruit = {'apple': 5, 'pear': 3, 'banana': 4, 'pineapple': 1, 'cherry': 20, 'orange': 15, 'watermelon': 10, 'lemon': 25}
s = filter(lambda x: x <= 3, fruit.values())
next(s)
next(s)

dct = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
list(filter(lambda x: x['name'] == 'python', dct))

# https://realpython.com/python-lambda/#reduce
from functools import reduce

reduce(lambda collector, x: f'{collector} | {x}', ['cat', 'dog', 'cow'])

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
reduce(lambda collector, pair: collector + pair[0], pairs, 0)


# data structures examples
portfolio = [
    {'name': 'IBM', 'price': 91.1, 'shares': 50},
    {'name': 'AA', 'price': 32.2, 'shares': 100},
    {'name': 'CAT', 'price': 83.44, 'shares': 150},
    {'name': 'MSFT', 'price': 51.23, 'shares': 200},
    {'name': 'GE', 'price': 40.37, 'shares': 95},
    {'name': 'MSFT', 'price': 65.1, 'shares': 50},
    {'name': 'IBM', 'price': 70.44, 'shares': 100}
]

def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name) # named callback
portfolio

portfolio.sort(key=lambda s: s['name']) # unnamed (lambda) callback
portfolio


dhtdata = [
    {'id': 1, 'time': '2020-10-20 09:30', 'data': {'temperature': '19.00', 'humidity': '61.50', 'hic': '18.56'}},
    {'id': 2, 'time': '2020-10-21 09:30', 'data': {'temperature': '18.00', 'humidity': '60.40', 'hic': '18.53'}},
    {'id': 3, 'time': '2020-10-22 09:30', 'data': {'temperature': '21.00', 'humidity': '61.00', 'hic': '18.65'}}
]

dhtdata[0]['time']
dhtdata[0]['data']['temperature']
[d['time'] for d in dhtdata]
[d['data']['temperature'] for d in dhtdata]
list(map(lambda x: float(x['data']['temperature']), [d for d in dhtdata]))


def fruit_selector(fruit):
    fruits = {
        'apple': 'The fruit is apple',
        'banana': 'The fruit is banana',
        'blueberries': 'The fruit is berries',
        'raspberries': 'The fruit is berries',
        'blue currant': 'The fruit is berries',
        'currant': 'The fruit is berries',
        'default': 'The fruit is unknown'
    }
    return dict(filter(lambda key: fruit in key[0], fruits.items()))

fruit_selector('banana')
fruit_selector('anana')
