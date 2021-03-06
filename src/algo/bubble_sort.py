import sys
import time
from src.plots.bar import AnimatePlot
import matplotlib.pyplot as plt

from src.generate_data import generate



generate(kind='list', size = 200)

f = open('input.txt', 'r')

generate(kind='list', size = 20)

f = open('input.txt', 'r')
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
    # # print(plot.toJSON())
    # sys.stdout = temp
    # f.close()
    plot.CreateVideo()
    print(plot.array)
    
    print("time taken in creating video {}".format(time.time() - t))

print(__name__)

if __name__ == 'src.algo.bubble_sort':
    main()


######################################################################################################
# ################################### FOR PYQTGRAPH RENDERING ############################################    # 
    # p = Plot2D(plot.array)
   
    # i = 0
    # length = len(plot.array)
    # def update():
    #     global p, i
    #     p.trace("sin",p.array[i%length])
    #     i += 1

    # timer = QtCore.QTimer()
    # timer.timeout.connect(update)
    # timer.start(50)

    # p.start()

