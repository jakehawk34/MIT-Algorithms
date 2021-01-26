def quicksort(A, p, r=None):
    if r == None:
        r = len(A)
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q)
        quicksort(A, q + 1, r)
    return A

# Linear-time partitioning subroutine:
def partition(A, p, q):
    pivot = A[p] # Set pivot at first element of subarray
    i = p
    for j in range(p + 1, q): # If a value in the subarray is greater than the pivot
        if A[j] <= pivot: # increase i by 1 and swap the values at i and j
            i += 1
            A[j], A[i] = A[i], A[j]
    A[p], A[i] = A[i], A[p] # swap the pivot to the value of the array where i ended at
    return i

A = [6, 10, 13, 5, 8, 3, 2, 11]
B = [1, 2, 4, 5, 6, 7, 8, 9, 10]

print(quicksort(A, 0))
print(quicksort(B, 0))

'''
Visualization for partition subroutine:
6 10 13 5 8 3 2 11 -> 6 is the pivot; A[i] = 6, A[j] = 10
A[j] > pivot
6 10 13 5 8 3 2 11 -> A[i] = 6, A[j] = 13
A[j] > pivot
6 10 13 5 8 3 2 11 -> A[i] = 6, A[j] = 5
A[j] <= pivot
6 10 13 5 8 3 2 11 -> i = i + 1, A[i] = 10, A[j] = 5
Swap A[j] and A[i]
6 5 13 10 8 3 2 11 -> A[i] = 5, A[j] = 8
A[j] > pivot
6 5 13 10 8 3 2 11 -> A[i] = 5, A[j] = 3
A[j] <= pivot
6 5 13 10 8 3 2 11 -> i = i + 1, A[i] = 13, A[j] = 3
Swap A[j] and A[i]
6 5 3 10 8 13 2 11 -> A[i] = 3, A[j] = 2
A[j] <= pivot
6 5 3 10 8 13 2 11 -> i = i + 1, A[i] = 10, A[j] = 2
Swap A[j] and A[i]
6 5 3 2 8 13 10 11 -> A[i] = 2, A[j] = 11
A[j] > pivot
6 5 3 2 8 13 10 11 -> Loop of j from start + 1 to end complete, A[i] = 2, pivot = 6
Swap pivot and A[i]
2 5 3 6 8 13 10 11
Return index of pivot -> 3
'''
