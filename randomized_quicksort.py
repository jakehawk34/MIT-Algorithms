import random

def randomized_qsort(A, end=None):
    if not A: return A # empty sequence case
    if end == None: end = len(A) - 1 # set to last index
    pivot = A[random.randint(0, end)] # random pivot

    less = randomized_qsort([x for x in A if x < pivot]) # values less than pivot
    greater = randomized_qsort([x for x in A if x > pivot]) # values greater than pivot
    return less + [x for x in A if x == pivot] + greater # list of less than pivot, equal to pivot, greater than pivot

A = [6, 10, 13, 5, 8, 3, 2, 11]
B = [1, 2, 4, 5, 6, 7, 8, 9, 10]

print(randomized_qsort(A, 0))
print(randomized_qsort(B, 0))