# decorators allows to temporary extend and modify the behavior of a callable (function, method, class)
# often are generic functionality wrapped around a function (e.g. timing, logging, access control, etc)

# decorator: container function
# wrapped: input function to decorate
# wrapper: closure decorating the input

import time

# timing decorator
def time_wrapper(wrapped):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = wrapped(*args, **kwargs)
        end = time.time()
        print(wrapped.__name__ + " took " + str((end-start)*1000) + " mil sec")
        return result
    return wrapper

@time_wrapper
def calc_square(numbers): # wrapped
    result = []
    for number in numbers:
        result.append(number*number)
    return 'Squared!'

@time_wrapper
def calc_cube(numbers): # wrapped
    result = []
    for number in numbers:
        result.append(number*number*number)
    return 'Cubed!'

array = range(1, 100000)
calc_square(array)
calc_cube(array)


# logging decorator
def star_decorator(wrapped):
    def wrapper(*args, **kwargs):
        print('*'*10 + 'START' + '*'*10)
        wrapped(*args, **kwargs)
        print('*'*10 + 'END' + '*'*10)
    return wrapper

@star_decorator
def calc_square(n):
    print(n * n)

calc_square(3)


def trace(wrapped):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {wrapped.__name__}() with {args}, {kwargs}')
        original_result = wrapped(*args, **kwargs)
        print(f'TRACE: {wrapped.__name__}() returned {original_result!r}')
        return original_result
    return wrapper

@trace
def write(name, text):
    return f'{name}: {text}'

write('Foo', 'Hello World')


# editor
def uppercase(wrapped):
    def wrapper():
        original_result = wrapped()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'Hello!'

greet()


# multiple decoration and order
def strong(f):
    def wrapper():
        return '<strong>' + f() + '</strong>'
    return wrapper

def emphasis(f):
    def wrapper():
        return '<em>' + f() + '</em>'
    return wrapper

@strong
@emphasis
def html_greet():
    return 'Hello!'

html_greet()
