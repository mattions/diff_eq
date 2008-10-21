# alpha function
from pylab import *
import numpy
from matplotlib import rc


rc('text', usetex=True)    # Activating Tex. Used in the plot title
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})


t = numpy.arange(0, 1000, 0.1)
t0 = 10
taus = numpy.arange(100, 1000, 100)

g_syns = []
for tau in taus:
   g_syn = (t - t0)/tau * exp(- (t-t0)/tau)
   #plot(t, g_syn)
   g_syns.append(g_syn)

for g_syn in g_syns:
  plot(t, g_syn)
  
title(r"Alpha Function: g_{syn} = \frac{(t-t_0)}{\tau} exp(\frac{t-t_o}{\tau})", fontsize=16)
  
show()
