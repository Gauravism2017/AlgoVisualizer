import time
from src.plots.bar import AnimatePlot
from src.plots.qt import Plot2D
from numba import jit, void, int_, double
import matplotlib.pyplot as plt
from pyqtgraph.Qt import QtCore, QtGui
from src.generate_data import generate

generate(kind='list', size = 20)

f = open('input.txt', 'r')
inp = f.read()
array = list(map(int, inp.split(',')))

plot = AnimatePlot("Heap Sort")
for i in range(5):
    plot.update(array, 0, 0)

_len = len(array)
plot._len = _len

def heapify(i, _len):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if(left < _len and array[left] > array[largest]):
        largest = left
    if(right < _len and array[right] > array[largest]):
        largest = right
    if(largest != i):
        array[i], array[largest] = array[largest], array[i]
        plot.update(array, i, 0, next=largest)
        heapify(largest, _len)

def heapsort():
    for i in range(int(_len / 2) - 1, -1, -1):
        heapify(i, _len)
    for i in range(_len-1, -1, -1):
        array[0], array[i] = array[i], array[0]
        plot.update(array, 0, 0, next=i)
        heapify(0, i)


heapsort()
for i in range(5):
    plot.update(array, 0, 0)
# print(array)
plot.CreateVideo()
