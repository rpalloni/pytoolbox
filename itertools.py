# compress: filter sequences (iterable) with boolean True (selector)
from itertools import compress

dates = ['2020-01-01','2020-02-04','2020-02-01','2020-01-24','2020-01-08','2020-02-10','2020-02-15','2020-02-11',]
counts = [1, 4, 3, 8, 0, 7, 9, 2]

bools = [n > 3 for n in counts]
print(list(compress(dates, bools)))

# accumulate: accumulate results of some (binary) function
from itertools import accumulate
import operator

data = [3, 4, 1, 3, 5, 6, 9, 0, 1]
list(accumulate(data, max))

list(accumulate(range(1, 11), operator.mul))

# cycle: takes iterable and creates infinite cycle from it
from itertools import cycle

players = ['John', 'Ben', 'Martin', 'Peter']

next_player = cycle(players).__next__
next_player()
next_player()

# tee: creates multiple iterators from one
from itertools import tee

def pairwise(iterable):
    '''s -> (s0, s1), (s1, s2), (s2, s3), ...'''
    a, b = tee(iterable, 2)
    next(b, None)
    return zip(a, b)

# divide: split iterable into number of sub-iterables
from more_itertools import divide
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

[list(l) for l in divide(3, data)]

# partition: divide our iterable using a predicate
from more_itertools import partition

files = ['foo.jpg','bar.exe','baz.gif','text.txt','data.bin',]

ALLOWED_EXTENSIONS = ('jpg','jpeg','gif','bmp','png')
is_allowed = lambda x: x.split('.')[1] in ALLOWED_EXTENSIONS

allowed, forbidden = partition(is_allowed, files)
list(allowed)
list(forbidden)

# consecutive_groups: find consecutive numbers, dates, letters, booleans or any other orderable objects
import datetime
import more_itertools

dates = [datetime.datetime(2020, 1, 15),datetime.datetime(2020, 1, 16),datetime.datetime(2020, 1, 17),datetime.datetime(2020, 2, 1),datetime.datetime(2020, 2, 2),datetime.datetime(2020, 2, 4)]

ordinal_dates = []
for d in dates:
    ordinal_dates.append(d.toordinal())

groups = [list(map(datetime.datetime.fromordinal, group)) for group in more_itertools.consecutive_groups(ordinal_dates)]
groups

# side_effect: generate side effect (logs) while iterating
import more_itertools
num_events = 0
events = ['click', 'scroll', 'zoom']

def _increment_num_events(_):
    global num_events
    num_events += 1

# Iterator that will be consumed
event_iterator = more_itertools.side_effect(_increment_num_events, events)

more_itertools.consume(event_iterator)

print(num_events)

# collapse: flatten multiple levels of nesting
import more_itertools
import os
list(more_itertools.collapse(list(os.walk('/local/dir/path')))) # flat list of dir and file

tree = [40, [25, [10, 3, 17], [32, 30, 38]], [78, 50, 93]]
list(more_itertools.collapse(tree))

# split_at: split iterable into lists based on predicate (similar to split with delimiter for string)
import more_itertools

lines = [
    'erhgedrgh',
    'erhgedrghed',
    'esdrhesdresr',
    'ktguygkyuk',
    '-------------',
    'srdthsrdt',
    'waefawef',
    'ryjrtyfj',
    '-------------',
    'edthedt',
    'awefawe',
]

list(more_itertools.split_at(lines, lambda x: '-------------' in x))

# bucket: split iterable into multiple buckets based on some condition
import more_itertools

class Circle: pass
class Cube: pass
class Triangle: pass

shapes = [Circle(), Cube(), Circle(), Circle(), Cube(), Triangle(), Triangle()]
s = more_itertools.bucket(shapes, key=lambda x: type(x)) # group using a key based on type

list(s[Cube])

list(s[Circle])

# map_reduce
from more_itertools import map_reduce
data = 'This sentence has words of various lengths in it, both short ones and long ones'.split()
data

keyfunc = lambda x: len(x)
result = map_reduce(data, keyfunc) # map
result

valuefunc = lambda x: 1
result = map_reduce(data, keyfunc, valuefunc) # transform
result

reducefunc = sum
result = map_reduce(data, keyfunc, valuefunc, reducefunc) # reduce
result

# sort_together: sort data by columns
'''
      Name     |    Address    | Year of Birth |   Income
----------------------------------------------------------------
John           |               |  1994         |   45000
Ben            |               |  1985         |   93000
Andy           |               |  2000         |   56000
Mary           |               |  1998         |   73000
'''

from more_itertools import sort_together
cols = [
    ('John', 'Ben', 'Andy', 'Mary'),
    ('1994', '1985', '2000', '1998'),
    ('45000', '93000', '56000', '73000')
]

sort_together(cols, key_list=(1, 2))

# seekable: allow to go back and forward through iterator even when it is consumed
from more_itertools import seekable

data = "This is example sentence for seeking back and forth".split()

it = seekable(data)
for word in it:
    ... # consume the full iterable

next(it) # StopIteration
it.seek(3)
next(it)


# filter_except: filter items based on exception to the selection function
from more_itertools import filter_except

data = ['1.5', '6', 'not-important', '11', '1.23E-7', 'remove-me', '25', 'trash']
list(map(float, filter_except(float, data, TypeError, ValueError))) # select float as they won't throw exception

# unique_to_each: mutually exclude elements
from more_itertools import unique_to_each
graph = {
    'A': {'B', 'E'},
    'B': {'A', 'C'},
    'C': {'B'},
    'D': {'E'},
    'E': {'A', 'D'}
}

unique_to_each({'B', 'E'}, {'A', 'C'}, {'B'}, {'E'}, {'A', 'D'})

# numeric_range: iterate over range of some non-integer values (float, date, etc)
from more_itertools import numeric_range
import datetime
from decimal import Decimal

list(numeric_range(Decimal('1.7'), Decimal('3.5'), Decimal('0.3')))

start = datetime.datetime(2020, 2, 10)
stop = datetime.datetime(2020, 2, 15)
step = datetime.timedelta(days=2)
list(numeric_range(start, stop, step))


# make_decorator
from more_itertools import make_decorator
from more_itertools import map_except

mapper_except = make_decorator(map_except, result_index=1) # create decorator(applied function, consumed function)

@mapper_except(float, ValueError, TypeError)
def read_file(f): # consumed function
    with open(f,'r') as file:
        contents = [line.strip('') for line in file]
        # contents = file.readlines()
    print(contents)
    return contents

list(read_file('iterfile.txt'))
