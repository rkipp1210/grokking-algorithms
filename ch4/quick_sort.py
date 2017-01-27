# quick sort algo

def quickSort(L):
    if len(L) < 2:
        return L
    else:
        pivot = L[0]
        lesser = [i for i in L[1:] if i <= pivot]
        greater = [i for i in L[1:] if i > pivot]
        return quickSort(lesser) + [pivot] + quickSort(greater)
        
L = [2, 3, 1, 4, 5, 0]
print(quickSort(L))

L = [10, 2, 6, 9, 3, 1, 4, 8, 7, 5, 0]
print(quickSort(L))