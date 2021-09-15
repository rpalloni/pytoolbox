import time

### Bubble Sort Algorithm
def bubble_sort(array):
    n = len(array)

    for i in range(n):

        all_sorted = True # flag to terminate if nothing left to sort

        # Look at each item of the list one by one,
        # comparing it with its adjacent value.
        # After each iteration, the portion of the array to sort shrinks
        # because the remaining items have already been sorted.

        for j in range(n - i - 1):

            if array[j] > array[j + 1]:

                # If the item is greater than its adjacent, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # As long as sorting happens, 'all_sorted' is set to False
                # so the algorithm doesn't stop
                all_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and algorithm can terminate
        if all_sorted:
            break

    return array

a = [8, 2, 6, 5, 4]

start_time = time.time()
bubble_sort(a)
time.time() - start_time


### Insertion Sort Algorithm
def insertion_sort(array):

    # Loop from the second element of the array until the last element
    for i in range(1, len(array)):

        # Element to be positioned
        item = array[i]

        # Initialize the position variable
        j = i - 1

        # Run through the list of items (the left subarray)
        # and find the correct position of the item.
        # Do this only if item is smaller than its adjacent values.
        while j >= 0 and array[j] > item:

            # Shift the value one position to the left
            # and reposition j to point to the next element
            array[j + 1] = array[j]

            j = j - 1
            print(j)

        # When you finish shifting the elements, you can position
        # item in its correct location

        array[j + 1] = item

    return array

a = [8, 2, 6, 5, 4]

# range(1, len(a))

start_time = time.time()
insertion_sort(a)
time.time() - start_time


### Merge Sort Algorithm (2 steps)
def merge(left, right):

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):

        # sort the elements in the result array comparing 
        # pairs of values in the two arrays

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # when end of either array is reached,remaining elements
        # are added from the other array to the result and break

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):

    if len(array) < 2:
        return array

    midpoint = len(array) // 2 # len(a) => 5 // 2 => 2

    # splitting recursively  the input into two equal halves,
    # sorting each half and merging them together into the final result

    left=merge_sort(array[:midpoint])
    right=merge_sort(array[midpoint:])

    return merge(left, right)


a = [8, 2, 6, 5, 4]

start_time = time.time()
merge_sort(a)
time.time() - start_time


# Quick Sort Algorithm
from random import randint

def quick_sort(array):

    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # select pivot element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # assign elements to each list
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # combine lists
    return quick_sort(low) + same + quick_sort(high)

a = [8, 2, 6, 5, 4]

start_time = time.time()
quick_sort(a)
time.time() - start_time
