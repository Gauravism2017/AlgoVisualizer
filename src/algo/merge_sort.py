import time
from src.plots.bar import AnimatePlot
from src.plots.qt import Plot2D
from numba import jit, void, int_, double
import matplotlib.pyplot as plt
from pyqtgraph.Qt import QtCore, QtGui

f = open('inp', 'r')
inp = f.read()
array = list(map(int, inp.split(',')))

plot = AnimatePlot("merge Sort")
plot.update(array, 0, 0)
_len = len(array)
plot._len = _len

def merge(start, mid, end):
    j = start
    next = end + 1
    _mid = mid
    print("start {} end {}".format(start, end))
    p = start
    q = mid + 1
    temp = []
    k = 0
    for i in range(start, end + 1):
        k += 1
        if(p > mid):
            temp.append(array[q])
            q += 1
        elif(q > end):
            temp.append(array[p])
            p += 1
        elif(array[p] < array[q]):
            temp.append(array[p])
            p += 1
        else:
            temp.append(array[q])
            q += 1

    #print(temp)
    for i in range(0, k):
        array[start] = temp[i]
        start += 1   

    plot.update(array, j, plot.k[-1] + 1, next=next, mid=_mid) 



def mergesort(start = 0, end = _len - 1):
    if(start < end):
        mid = start + int((end - start) / 2)
        mergesort(start, mid)
        mergesort(mid + 1, end)
        merge(start, mid, end)

mergesort()
#print(array)
for i in range(5):
    plot.update(array, 0, 0)
        
# print(plot.j)
# print('\n')
# print(plot.next)
plot.CreateVideo()
