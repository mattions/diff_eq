# Exp2Syn. To see how it is plotted

from pylab import *
import numpy

t = numpy.arange(0,100,0.1)

tau1 = 9
tau2 = 10
weight = 1

def exp2syn(t, tau1, tau2, weight):
   
   g = weight * (exp (-t/tau2) - exp(-t/tau1))
   return g
   
g = exp2syn(t, tau1, tau2, weight)   
plot(t, g, label="conductance")

voltage = numpy.arange(-120, 31, 1)
e = -65


i = numpy.zeros(len(voltage))

i = (voltage - e)

#figure()
#plot(voltage,i, label="intensity")

show()

