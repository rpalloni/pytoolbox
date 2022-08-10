# decorators allows to temporary extend and modify the behavior of a callable (function, method, class)
# often are generic functionality wrapped around a function (e.g. timing, logging, access control, etc)

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
def star_decorator(f):
    def wrapper(*args, **kwargs):
        print('*'*10 + 'START' + '*'*10)
        f(*args, **kwargs)
        print('*'*10 + 'END' + '*'*10)
    return wrapper

@star_decorator
def calc_square(n):
    print(n * n)

calc_square(3)
