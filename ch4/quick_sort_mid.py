# quick sort middle element pivot

from random import randint

def quickSortMid(L):
    if len(L) < 2:
        return L
    else:
        pivot = L[len(L) / 2]
        lesser = [i for i in L if i <= pivot and i != pivot]
        greater = [i for i in L if i > pivot and i != pivot]
        return quickSortMid(lesser) + [pivot] + quickSortMid(greater)
        
L = [2, 3, 1, 4, 5, 0]
print(quickSortMid(L))

L = [10, 2, 6, 9, 3, 1, 4, 8, 7, 5, 0]
print(quickSortMid(L))