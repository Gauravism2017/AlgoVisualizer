import os
import sys
import random
import numpy as np
from src.config import SAVE_LOCATION

f = open('inp', 'w')
std = sys.stdout
sys.stdout = f
li = [random.getrandbits(256) for i in range(20)]
li = str(li)[1:-1]
print(li)
sys.stdout = std
f.close()
    