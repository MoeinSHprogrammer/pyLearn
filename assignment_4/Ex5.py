
import random
import array
import numpy as np

n = 10
x = np.random.choice(10, 10, replace=True)
x = array.array("i", x)

print("orginal:",x)

print("reverse:",set(x))