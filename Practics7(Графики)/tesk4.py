import numpy as np
import pylab
from matplotlib import mlab
import math

xlist = mlab.frange (-2*np.pi, 2*np.pi, 0.01)

pylab.ion()
for a in range (0,50,1):
        ylist = [np.sin (x + a/10) for x in xlist]
        zlist = [np.cos(2*x) for x in xlist]
        pylab.clf()
        pylab.plot ( ylist, zlist)
        pylab.draw()

pylab.close()
               
