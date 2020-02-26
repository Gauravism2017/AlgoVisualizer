
import time
from src.plots.bar import Plot
#array = list(map(int, input().split()))




##  READ INPUT
f = open('inp', 'r')
inp = f.read()
array = list(map(int, inp.split(',')))

plot = Plot(array, 0, 0, "bubble_Sort")
plot._plot(1, 0)

k = 1
_len = len(array)

for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while(j >= 0 and array[j] > key):
        plot.update(array, j, k, next=j+1)
        plot._plot()
        array[j + 1], array[j] = array[j], array[j + 1]
        #print(array)
        j -= 1
        k += 1
        
    array[j + 1] = key
plot.update(array, j, k, next=j+1)
plot._plot(0, 1)