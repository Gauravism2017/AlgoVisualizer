import time
from src.plots.bar import AnimatePlot

f = open('inp', 'r')
inp = f.read()
array = list(map(int, inp.split(',')))

plot = AnimatePlot("bubble_Sort")
plot.update(array, 0, 0)
_len = len(array)
plot._len = _len


def main():
    t = time.time()
    k = 1
    for i in range(_len - 1):
        minm_idx = i
        for j in range(i + 1, _len):
            if(array[j] < array[minm_idx]):
                minm_idx = j
        plot.update(array, i, k, next=minm_idx)
        array[minm_idx], array[i] = array[i], array[minm_idx]
        k += 1

    for i in range(5):
            plot.update(array, j, k, next=minm_idx)

    print("time taken in sorting and Storing is {}".format(time.time() - t))
    t = time.time()
    plot.CreateVideo()
    print("time taken in creating video {}".format(time.time() - t))

if __name__ == 'src.algo.selection_sort':
    main()