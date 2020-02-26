import sys
import time
from src.plots.bar import AnimatePlot
from src.plots.qt import Plot2D
from numba import jit, void, int_, double
import matplotlib.pyplot as plt
from pyqtgraph.Qt import QtCore, QtGui

f = open('inp', 'r')
inp = f.read()
array = list(map(int, inp.split(',')))

plot = AnimatePlot("bubble_Sort")
plot.update(array, 0, 0)
_len = len(array)
plot._len = _len
#@jit(nopython=False, parallel=True)
def main():
    k = 1
    t = time.time()
    
    for i in range(_len - 1):
        for j in range(_len - i - 1):
            if(array[j] > array[j + 1]):
                plot.update(array, j, k, next=j+1)
                # plot._plot()
                # _plot(array, j, k)
                array[j], array[j + 1] = array[j + 1], array[j]
                k += 1

    for i in range(5):
        plot.update(array, j, k, next=j+1)
    print("time taken in sorting and Storing is {}".format(time.time() - t))
    t = time.time()
    # f = open('data.json','w')
    # temp = sys.stdout
    # sys.stdout = f
    # print(plot.toJSON())
    # sys.stdout = temp
    # f.close()
    #plot.CreateVideo()
    #print(plot.array)
    
    print("time taken in creating video {}".format(time.time() - t))

print(__name__)

if __name__ == 'src.algo.bubble_sort':
    main()
    p = Plot2D(plot.array)
   
    i = 0
    length = len(plot.array)
    def update():
        global p, i
        p.trace("sin",p.array[i%length])
        i += 1

    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(50)

    p.start()