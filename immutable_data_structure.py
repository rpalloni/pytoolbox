# named tuple
from collections import namedtuple

# Create a namedtuple type, Point
Point = namedtuple("Point", "x y")
issubclass(Point, tuple)

# Instantiate the new type
point = Point(2, 4)
point

# Dot notation to access coordinates
point.x
point.y

# Indexing to access coordinates
point[0]
point[1]

# Convert to dict
point._asdict()

# Error: Named tuples are immutable!
point.x = 100



#| Name            | Field      | Born | Nobel Prize? |
#|-----------------|------------|------|--------------|
#| Ada Lovelace    | math       | 1815 | no           |
#| Emmy Noether    | math       | 1882 | no           |
#| Marie Curie     | math       | 1867 | yes          |
#| Tu Youyou       | physics    | 1930 | yes          |
#| Vera Rubin      | chemistry  | 1928 | no           |
#| Sally Ride      | physics    | 1951 | no           |

# list of dict objects
scientists = [
    {'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
    {'name': 'Emy Noether', 'field': 'math', 'born': 1882, 'nobel': False},
    {'name': 'Marie Curie', 'field': 'math', 'born': 1867, 'nobel': True},
    {'name': 'Tu Youyou', 'field': 'physics', 'born': 1930, 'nobel': True},
    {'name': 'Vera Rubin', 'field': 'chemistry', 'born': 1928, 'nobel': False},
    {'name': 'Sally Ride', 'field': 'physics', 'born': 1951, 'nobel': False}
]

scientists[0]['name'] = 'Ed Lovelance' # mutable
scientists

# mutable data structure disadvantages
# 1 - code repetition (boilerplate keys)
# 2 - in multithread parallel processing, risk of data structure change while many threads access it (absence of resource lock)

# immutable data structure: record
import collections
from pprint import pprint
ScientistRecordBuilder = collections.namedtuple('ScientistRecordBuilder', ['name','field','born','nobel'])
print(ScientistRecordBuilder)

ada = ScientistRecordBuilder(name='Ada Lovelace', field= 'math', born=1815, nobel=False)
ada.name
ada.field

ada.name = 'Ed Lovelace' # immutable

emy = ScientistRecordBuilder(name='Emy Noether', field= 'math', born=1882, nobel=False)
marie = ScientistRecordBuilder(name='Marie Curie', field= 'math', born=1867, nobel=True)
tu = ScientistRecordBuilder(name='Tu Youyou', field= 'physics', born=1930, nobel=True)
vera = ScientistRecordBuilder(name='Vera Rubin', field= 'chemistry', born=1928, nobel=False)
sally = ScientistRecordBuilder(name='Sally Ride', field= 'physics', born=1928, nobel=False)

scientists = [ada,emy,marie,tu,vera,sally] # immutable datastructures (tuple) added to mutable datastructure (list)
pprint(scientists)

scientists[0].name = 'Ed Lovelace' # record is immutable

del scientists[0] # list is mutable
pprint(scientists)

# solid datastructure: fully immutable
scientists = (ada,emy,marie,tu,vera,sally) # immutable datastructures (tuple) added to immutable datastructure (tuple)
pprint(scientists)
del scientists[0] # immutable

# list of nested dict
scientists = [
    {'name':'Ada Lovelace', 'field':'math', 'born':1815, 'nobel':False, 'affiliation':{'university':'Cambridge','country':'UK'}},
    {'name':'Emy Noether', 'field':'math', 'born':1882, 'nobel':False, 'affiliation':{'university':'Erlangen','country':'DE'}},
    {'name':'Marie Curie', 'field':'math', 'born':1867, 'nobel':True, 'affiliation':{'university':'Sorbonne','country':'FR'}},
    {'name':'Tu Youyou', 'field':'physics', 'born':1930, 'nobel':True, 'affiliation':{'university':'Ningbo','country':'PRC'}},
    {'name':'Vera Rubin', 'field':'chemistry', 'born':1928, 'nobel':False, 'affiliation':{'university':'Princeton','country':'USA'}},
    {'name':'Sally Ride', 'field':'physics', 'born':1951, 'nobel':False, 'affiliation':{'university':'Stanford','country':'USA'}}
]
scientists

[scientist['name'] for scientist in scientists]
[scientist['affiliation']['university'] for scientist in scientists]

list(map(lambda x: x['affiliation']['university'], [scientist for scientist in scientists]))

