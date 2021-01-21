import time
import random

def insertion_sort(A, n):

    for i in range(1, n):
        key = A[i] # Start at second element in array
        j = i - 1
        while j >= 0 and A[j] > key: # Compare all of the elements to the left of the key
            A[j + 1] = A[j] # If a number is greater than the key, move it to the right one
            j -= 1 # Check the number to the left
        A[j + 1] = key # Once you have sorted the first key, move the new key to the right by one
    return A # Return the sorted array

A = [random.randint(0, 40) for _ in range(1000)]

t0 = time.perf_counter()
insertion_sort(A, len(A))
t1 = time.perf_counter()
print(f'Inserion sort time : {t1 - t0}')