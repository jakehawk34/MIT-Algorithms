''' Find an element in a sorted array where A is the array and x is the target value we are searching for.
Worst case running time is big-theta( log n )
'''

def binary_search(A, x):
    L = 0 # left index
    R = len(A) - 1 # right index

    while L <= R: # Make sure the left and right indices do not cross 
        m = (L + R) // 2 # Middle element index
        if x > A[m]: # Target value is greater than middle value; move left index to one greater than the middle
            L = m + 1
        elif x < A[m]: # Target value is less than middle value; move right index to one less than the middle
            R = m - 1
        else:
            return m # Return m when the left and right index are the same

    return "Value not in array" # Unsuccsessful search

print(binary_search([2, 5, 7, 8, 9, 12, 15],  12))
print(binary_search(sorted([3, 1, 2]), 2))
