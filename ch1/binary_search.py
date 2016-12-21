# Implementation of Binary Search

def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid
        else:
            low = mid + 1
    return None
    
testList = [1, 3, 5, 7, 9]

print binarySearch(testList, 10)
