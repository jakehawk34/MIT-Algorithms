import time
import random

def merge_sort(A, n):
    if n > 1: #If array is longer than 1
        m = len(A) // 2 #middle index
        L = A[:m] #temporary left subarray
        R = A[m:] #temporary right subarray

        merge_sort(L, len(L)) #recursive calls for the left and right halves
        merge_sort(R, len(R))

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]: #If the left elemement is less than the right, add it to the sorted array
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j] #If the right element is less than the left, add it to the sorted array
                j += 1
            k += 1
        #check for any element left over
        while i < len(L): 
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

    return A


A = [random.randint(0, 40) for _ in range(1000)]

t0 = time.perf_counter()
merge_sort(A, len(A))
t1 = time.perf_counter()
print(f'Merge sort time : {t1 - t0}')

