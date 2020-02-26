import os
import sys
import random
from src.config import SAVE_LOCATION

f = open('inp', 'w')
std = sys.stdout
sys.stdout = f
li = [random.randint(0, 100) for i in range(100)]
li = str(li)[1:-1]
print(li)
sys.stdout = std
f.close()
    