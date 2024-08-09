# Searching algorithm: Linear Search

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Given array
arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# Search for the number 9 using linear search
index = linear_search(arr, 9)
print(f"Index of 9 using linear search: {index}")

# Insertion Sort implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Sort the array using insertion sort
sorted_arr = insertion_sort(arr)
print(f"Sorted array using insertion sort: {sorted_arr}")

# Searching algorithm: Binary Search

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Search for the number 9 using binary search on the sorted array
index = binary_search(sorted_arr, 9)
print(f"Index of 9 using binary search: {index}")

# Binary search is efficient for large datasets where the array is sorted.
# It reduces the time complexity to O(log n) compared to linear search's O(n).
# In real-world scenarios, such as looking up words in a dictionary or
# finding a contact in a sorted phone book, binary search is highly efficient
# and saves considerable time.