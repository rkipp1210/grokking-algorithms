# recursive list counter

def count_list(L):
    if L == []:
        return 0
    else:
        return 1 + count_list(L[:-1])
        
L = [1, 2, 3, 4, 5, 6, 7]
print count_list(L)

L = [1, 2, 3]
print count_list(L)