#!/usr/bin/env python

from pylab import *
import scipy


def analisys(x,f):
   plot(x, f(x))
   plot(x, f.deriv()(x))
   grid()
   print "function: \n%s\n\nderiv: \n%s\n\nroots: %s" \
   %(f,f.deriv(),f.deriv().r)


x=r_[-2:2:0.1]


# First figure
f = scipy.poly1d([1,0,0,0])
figure()
analisys(x,f)
title("x^3, der=x^2, x=0 unstable point because always positive")
plot([0],[0], 'wo')

# Second one
f1 = scipy.poly1d([-1,0,0,0])
figure()
analisys(x,f1)
title("x^-3, der=x^-2, x=0 stable point because always negative")
plot([0],[0], 'ko')

#Third one
f2 = scipy.poly1d([1,0,0])
figure()
analisys(x,f2)
title("x^2, der=x, x=0 half-stable point because derivate change sign")
plot([0],[0], 'o', c='0.7')




show()



