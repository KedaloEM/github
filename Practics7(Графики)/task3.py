import numpy as np
import matplotlib.pyplot as plt
import math
x=np.arange(-10,10.01,0.01)
def func(x):
    b=np.log((x**2+1)*np.e**(-abs(x)/10) , 1 + np.tan(1/(1+np.sin(x)**2)))
    return(b)
plt.plot(x , func(x))
plt.show()
