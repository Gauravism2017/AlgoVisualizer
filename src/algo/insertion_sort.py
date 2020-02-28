
import time
from src.plots.bar import AnimatePlot
from src.generate_data import generate

generate(kind='list', size = 20)

f = open('input.txt', 'r')
inp = f.read()
array = list(map(int, inp.split(',')))

plot = AnimatePlot("insertion_sort_Sort")
plot.update(array, 0, 0)
_len = len(array)
plot._len = _len
k =  1

for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while(j >= 0 and array[j] > key):
        plot.update(array, j, k, next=j+1)
        array[j + 1], array[j] = array[j], array[j + 1]
        #print(array)
        j -= 1
        k += 1
        
    array[j + 1] = key
plot.update(array, j, k, next=j+1)
plot.CreateVideo()