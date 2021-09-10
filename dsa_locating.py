### Locate Algorithm

# linear search
def locate_number_linear(array, number):
    # initialize position variable at 0
    position = 0

    # loop over the array if not empty
    while position < len(array):
        # check if element at current position equals the number
        if array[position] == number:
            return position
        else:
            position += 1

            # check end of array
            if position == len(array):
                # number not present
                return -1
    return -1


test = {
    'input': {
        'array': [13, 11, 10, 7, 4, 3, 1, 0],
        'number': 7
    },
    'output': 3
}

locate_number_linear(test['input']['array'], test['input']['number']) == test['output'] # or locate_number_linear(**test['input']) == test['output']


# binary search
def locate_number_binary(array, number):
    # define search space
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_number = array[mid]
        print('start position:', start, ', end position :', end, ', mid position:', mid, ', mid number', mid_number)
        if mid_number == number:
            return mid
        elif mid_number < number:
            end = mid - 1
        elif mid_number > number:
            start = mid + 1
    return -1


test = {
    'input': {
        'array': [13, 11, 10, 7, 4, 3, 1, 0],
        'number': 1
    },
    'output': 6
}

locate_number_binary(test['input']['array'], test['input']['number']) == test['output'] # or locate_number_binary(**test['input']) == test['output']

# efficiency
import time

bigtest = {
    'input': {
        'array': list(range(100000, 0, -1)),
        'number': 2
    },
    'output': 99998
}

start_time = time.time()
locate_number_linear(bigtest['input']['array'], bigtest['input']['number']) == bigtest['output']
time.time() - start_time

start_time = time.time()
locate_number_binary(bigtest['input']['array'], bigtest['input']['number']) == bigtest['output']
time.time() - start_time
