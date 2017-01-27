from random import randint
from time import time
from quick_sort_rand import quickSortRand
from quick_sort import quickSort
from quick_sort_mid import quickSortMid
import matplotlib.pyplot as plt
import numpy

randomTimes = []
firstElementTimes = []
midElementTimes = []

for i in range(1000):
    L = [randint(0, 100) for i in range(1000)]
    
    # run the random pivot quick sorter
    t = time()
    quickSortRand(L)
    randomTimes.append(time() - t)
    
    # run the first element quick sorter
    t = time()
    quickSort(L)
    firstElementTimes.append(time() - t)
    
    # run the mid element quick sorter
    t = time()
    quickSortMid(L)
    midElementTimes.append(time() - t)
    
    
plt.title("Sort Time Histogram")
plt.xlabel("Sort Time")
plt.ylabel("Run Count")

bins = numpy.linspace(0, 0.02, 100)

plt.hist(randomTimes, bins, alpha=0.5, label='Random Pivot')
plt.hist(midElementTimes, bins, alpha=0.5, label='Middle Element Pivot')
plt.hist(firstElementTimes, bins, alpha=0.5, label='First Element Pivot')
plt.legend(loc='upper right')

plt.show()