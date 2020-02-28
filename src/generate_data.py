import os
import sys
import random
import numpy as np
from scipy.sparse import rand
from src.config import SAVE_LOCATION

def generate(kind='list', **kwargs):
    f = open('input.txt', 'w')
    std = sys.stdout
    sys.stdout = f
    n = kwargs.get('size')
    if(kind=='list'):
        li = [random.getrandbits(32) for i in range(n)]
        li = str(li)[1:-1]
        print(li)
    # generate a matrix:
    if(kind == 'matrix'):
        li = [[random.getrandbits(8) for i in range(n)] for i in range(n)]
        li =  rand(n, n, density=(0.6*10)/n).todense()*5
        li = li.astype(int)
        li = str(li).replace('[', ' ').replace(']', '')
        print(n)
        print(li)
        print(0)
    sys.stdout = std
    f.close()
    