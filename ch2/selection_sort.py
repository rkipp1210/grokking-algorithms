# Selection sort algo

def findSmallest(L):
    small = L[0]
    small_ind = 0
    for i in range(1, len(L)):
        if L[i] < small:
            small = L[i]
            small_ind = i
    return small_ind
    
def selectionSort(L):
    sorted = []
    for i in range(len(L)):
        smallest = findSmallest(L)
        sorted.append(L.pop(smallest))
    return sorted

print(selectionSort([5, 3, 2, 10]))