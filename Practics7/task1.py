import numpy as np
import math
import matplotlib.pyplot as plt
def func(x1):
    x1 = float(x1)
    b = math.log((1/(math.e**(math.sin(x1)) + 1))/(5/4+1/x1**15), (1+x1**2))
    return(b)
print('f(1) =', func(1))
print('f(10) =',func(10))
print('f(1000) =',func(1000))




