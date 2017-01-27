# quick sort faster

from random import randint

def quickSortRand(L):
    if len(L) < 2:
        return L
    else:
        pivot = L[randint(0, len(L)-1)]
        lesser = [i for i in L if i <= pivot and i != pivot]
        greater = [i for i in L if i > pivot and i != pivot]
        return quickSortRand(lesser) + [pivot] + quickSortRand(greater)
        
L = [2, 3, 1, 4, 5, 0]
print(quickSortRand(L))

L = [10, 2, 6, 9, 3, 1, 4, 8, 7, 5, 0]
print(quickSortRand(L))