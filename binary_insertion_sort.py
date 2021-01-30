def binary_search(arr, val, low, high):
        #Distinguish whether to insert before or after the low boundary
        if high == low:
            if arr[low] > val:
                return low
            else:
                return low + 1
        
        if low > high:
            return low
        
        mid = (high + low) // 2
        if val > arr[mid]:
            return binary_search(arr, val, mid + 1, high)
        elif val < arr[mid]:
            return binary_search(arr, val, low, mid - 1)
        else:
            return mid

def insertion_sort(arr):

    for i in range(1, len(arr)):
        val = arr[i] 
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr


print(insertion_sort([1, 3, 4, 9, 5, 6, 7, 0]))