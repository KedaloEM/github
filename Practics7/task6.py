__author__ = 'student'

import numpy as np
import matplotlib.pyplot as plt
from math import cos,pi
a = 3
b = 0.5
x = np.arange(-2,4,0.01)
y = np.arange(-2,4,0.01)
def func(x):
    for i in range(len(x)):
        y[i] = sum([cos(pi*x[i]*a**j)*b**j for j in range(100)])
    return(y)
plt.plot(x, func(x))
plt.show()