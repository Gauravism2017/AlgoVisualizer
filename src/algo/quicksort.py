import time
import sys
sys.setrecursionlimit(1500)
import random
from src.plots.bar import AnimatePlot
from src.plots.qt import Plot2D
from numba import jit, void, int_, double
import matplotlib.pyplot as plt
from pyqtgraph.Qt import QtCore, QtGui

f = open('inp', 'r')
inp = f.read()
array = list(map(int, inp.split(',')))

plot = AnimatePlot("Quick Sort")
plot.update(array, 0, 0)
_len = len(array)
plot._len = _len
k = 0

def partition(start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while(low <= high and array[high] >= pivot):
            high -= 1
        while(low <= high and array[low] <= pivot):
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            plot.update(array, low, 0, next=high)
        else:
            break
    array[start], array[high] = array[high], array[start]
    #plot.update(array, start, 0, next=high)
    return high + 1

def random_partion(start, end):
    print(start)
    print(end)
    rand  = start + int(random.random()) % (end - start + 1)
    array[rand], array[start] = array[start], array[rand]
    return partition(start, end)

def quickSort(start = 0, end = _len - 1):
    if(start < end):
        piv_pos = partition(start, end)
        quickSort(start, piv_pos - 1);
        quickSort(piv_pos, end)

quickSort()
for i in range(5):
    plot.update(array, 0, 0)
print(array)
plot.CreateVideo()