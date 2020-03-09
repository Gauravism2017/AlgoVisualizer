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
        li = [random.getrandbits(8) for i in range(n)]
        li = str(li)[1:-1]
        print(li)
    # generate a matrix:
    if(kind == 'matrix'):
        # li = [[random.getrandbits(8) for i in range(n)] for i in range(n)]
        if "density" in kwargs:
            li =  rand(n, n, density=kwargs.get("density")).todense()*5
        else:
            li =  rand(n, n, density=min(((0.6*10)/n), 0.1*n)).todense()*5
        li = li.astype(int)
        print(n)
        np.savetxt(f, X = li, fmt='%d')
        print(0)
        
    sys.stdout = std
    f.close()
    