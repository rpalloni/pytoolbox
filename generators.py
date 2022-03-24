'''
Generator functions are a special kind of function that return a lazy iterator.
Iterator is an object that you can loop over like a list.
However, unlike lists, lazy iterators do not store their contents in memory.
-> List: fast but heavy
-> Genrators: slow but light
'''

import sys
import time

numbers = range(0, 10000, 1)

# list comprehension
start_time = time.time()
lc = [n*n for n in numbers if n % 2 == 1] # list comprehension
time.time() - start_time

lc # lc produces a list object => created AND iterated at once
type(lc)
print(sys.getsizeof(lc)) # bytes

# generator comprehension
start_time = time.time()
ge = (n*n for n in numbers if n % 2 == 1)
time.time() - start_time

ge # ge produces a generator object => created AND iterated at each iteration (lazy approach)
type(ge)
print(sys.getsizeof(ge)) # bytes

for i in ge:
    print(i)
for i in ge:
    print(i) # ge exausted during first iteration and no more available


'''
yield statement suspends function execution and returns the yielded value to the caller.
In contrast, return stops function execution completely.
When a function is suspended, the state of that function is saved.
This includes any variable bindings local to the generator,
the instruction pointer, the internal stack, and any exception handling.
next() resume function execution where it was yielded
'''

def cmap(funcs, arr):
    for f in funcs:
        output = list(map(f, arr))
        arr = output
        # return output
        yield output # generator

funcs = [lambda x: x*x, lambda x: x+x]
arr = [1, 2, 3, 4]

result = cmap(funcs, arr)
#result
next(result)
next(result)
