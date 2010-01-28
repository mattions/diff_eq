import numpy as np
import enthought.mayavi.mlab as mlab

def f(x, y):

    return x + y*y

x, y = np.mgrid[1:3:0.1, -2.:2.:0.01]
s = mlab.surf(x, y, f)
