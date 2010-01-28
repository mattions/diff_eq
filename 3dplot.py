import numpy as np
import enthought.mayavi.mlab as mlab


"""Test surf on regularly spaced co-ordinates like MayaVi."""
def f(x, y):

    return np.sin(x+y) + np.sin(2*x - y) + np.cos(3*x+4*y)

def f2(x, y):
    
    return pow(x,1/3) * y - np.sin(x* pow(y,2))

def f3(x, y):
    return pow(x,-3) * y
    
def f4(x, y):
    return np.sin(x* pow(y,2))
    
    
x, y = np.mgrid[0.:3:0.1, -2.:2:0.1]

#s = mlab.surf(x, y, f)

#mlab.figure()

s2 = mlab.surf(x, y, f2)

#mlab.figure()

#s3 = mlab.surf(x, y, f3)

#mlab.figure()

#s4 = mlab.surf(x, y, f4)
