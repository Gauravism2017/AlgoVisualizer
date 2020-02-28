import os
import sys
import random
import numpy as np
from scipy.sparse import rand
from src.config import SAVE_LOCATION
#   ceate a list
# f = open('inp', 'w')
# std = sys.stdout
# sys.stdout = f
#   ceate a list
# li = [random.getrandbits(32) for i in range(20)]
# li = str(li)[1:-1]
# generate a matrix:
f = open('input.txt', 'w')
std = sys.stdout
sys.stdout = f
li = [random.randint(0, 100) for i in range(100)]
li = str(li)[1:-1]
n = 30
# li = [[random.getrandbits(8) for i in range(n)] for i in range(n)]
li =  rand(n, n, density=(0.6*10)/n).todense()*5
li = li.astype(int)
li = str(li).replace('[', ' ').replace(']', '')
print(n)
print(li)
print(0)
sys.stdout = std
f.close()
    