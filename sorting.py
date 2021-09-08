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
