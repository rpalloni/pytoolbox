# https://docs.python.org/3/library/functions.html#built-in-functions

# iterate: range() >> enumeration()
numbers = [45, 22, 14, 65, 97, 72]
for i in range(len(numbers)):
    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
        numbers[i] = 'fizzbuzz'
    elif numbers[i] % 3 == 0:
        numbers[i] = 'fizz'
    elif numbers[i] % 5 == 0:
        numbers[i] = 'buzz'

for i, num in enumerate(numbers):
    if num % 3 == 0 and num % 5 == 0:
        numbers[i] = 'fizzbuzz'
    elif num % 3 == 0:
        numbers[i] = 'fizz'
    elif num % 5 == 0:
        numbers[i] = 'buzz'

numbers

# apply: map() and filter() >> list comprehension
numbers = [4, 2, 1, 6, 9, 7]
def square(x):
    return x*x

list(map(square, numbers))
[square(x) for x in numbers]


def filter_is_odd(x):
    return bool(x % 2)

list(filter(filter_is_odd, numbers))
[x for x in numbers if filter_is_odd(x)]

# sort: sort() >> sorted()
sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear'], reverse=True)

animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},
]

sorted(animals, key=lambda animal: animal['age'])

# speed: list[] >> set()
import random
all_words = "all the words in the world".split()
def get_random_word():
    return random.choice(all_words)

def get_unique_words():
    words = []
    for _ in range(1000):
        words.append(get_random_word())
    return set(words)
get_unique_words()

def get_unique_words():
    words = set()
    for _ in range(1000):
        words.add(get_random_word())
    return words
get_unique_words()

# memory saving: list[] >> generators()
# out of memory
sum([i * i for i in range(1, 10000001)])

# only one element exists in memory at a time
sum((i * i for i in range(1, 10000000001)))


# standard library
student_grades = {}
grades = [
     ('elliot', 91),
     ('neelam', 98),
     ('bianca', 81),
     ('elliot', 88),
]

for name, grade in grades:
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)
student_grades

# defaultdict
from collections import defaultdict
student_grades = defaultdict(list)
for name, grade in grades:
    student_grades[name].append(grade)
student_grades

# Counter
from collections import Counter
words = "if there was there was but if there was not there was not".split()
counts = Counter(words)
counts
counts.most_common(2)

# string
import string
string.ascii_letters
string.ascii_uppercase
string.ascii_lowercase
string.digits
string.hexdigits
string.octdigits
string.punctuation
string.printable
string.whitespace

def is_upper(word):
     for letter in word:
         if letter not in string.ascii_uppercase:
             return False
     return True

is_upper('Thanks Geir')
False
is_upper('LOL')
True

import itertools
friends = ['Monique', 'Ashish', 'Devon', 'Bernie']
# list of every possible grouping of input values with two elements
# with permutations, the order of the elements matters
list(itertools.permutations(friends, r=2))

# with combinations, order is irrelevant
list(itertools.combinations(friends, r=2))
