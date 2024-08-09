# Sort And search
A brief description of your project, explaining its purpose and functionality.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation
to install this project run this project locally 
1.Clone the repository:
Open terminal and run clone repository:
git clone https://github.com/your-username/sort-and-search.git
2.navigate to the project directory:
cd sort-and-search
3.No external dependencies are required for this project. you can run the python script directly: 
python sort_and_search.py


## Usage
This project includes three main functionalities: Linear Search, Insertion Sort, and Binary Search.

Linear Search
Linear Search is a basic search algorithm that checks each element in the list one by one until it finds the target element.
example:
# Searching algorithm: Linear Search
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
# output 
Index of 9 using linear search: 10

Binary Search
Binary Search is a more efficient search algorithm that works on sorted arrays by repeatedly dividing the search interval in half.
example:
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
# output
Index of 9 using binary search: 8

Insertion Sort
Insertion Sort is a simple sorting algorithm that builds the sorted array one element at a time.
example:
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
# output
Output:
Sorted array using insertion sort: [-40, -3, -1, 1, 2, 4, 5, 7, 9, 16, 18, 27, 35, 100]
   
Efficiency
Binary Search is efficient for large datasets where the array is sorted. It reduces the time complexity to O(log n) compared to Linear Search's O(n). In real-world scenarios, such as looking up words in a dictionary or finding a contact in a sorted phone book, Binary Search is highly efficient and saves considerable time.


## Credits
This project was developed by Siyabonga.