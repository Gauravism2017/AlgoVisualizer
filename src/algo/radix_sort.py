
import time
from src.plots.bar import AnimatePlot
from src.plots.qt import Plot2D
from numba import jit, void, int_, double
import matplotlib.pyplot as plt
from pyqtgraph.Qt import QtCore, QtGui

f = open('inp', 'r')
inp = f.read()
array = list(map(int, inp.split(',')))

plot = AnimatePlot("Radix Sort")
for i in range(5):
    plot.update(array, 0, 0)

_len = len(array)
plot._len = _len


def count_sort(place):
    output = [0] * _len
    count = [0] * 10
    for i in range(_len):
        index = int(array[i]/place)
        count[index%10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = _len - 1
    while i >= 0:
        index = int(array[i] / place)
        output[count[index%10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(_len): 
        array[i] = output[i] 
    # print(array)
    plot.update(array, 0, 0)
# 
    
def radixSort():
    max_element = max(array)
    place = 1
    while(int(max_element/ place)):
        # print(max_element)
        count_sort(place)
        place *= 10

radixSort()
for i in range(5):
    plot.update(array, 0, 0)
plot.CreateVideo()
#print(array)