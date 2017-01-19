# recurisively sum items in an array

def rec_sum(L):
    if L == []:
        return 0
    else:
        return L[0] + rec_sum(L[1:])
        
L = [2, 4, 6]
print(rec_sum(L))