# alpha function

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from numpy import exp

matplotlib.rc('text', usetex=True)    # Activating Tex. Used in the plot title
matplotlib.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})

t = np.linspace(0, 1000)
t0 = 10
taus = np.arange(100, 1000, 100)

g_syns = []
for tau in taus:
   g_syn = (t - t0)/tau * exp(- (t-t0)/tau)
   #plot(t, g_syn)
   g_syns.append(g_syn)

for g_syn in g_syns:
    plt.plot(t, g_syn)
  
plt.title(r"Alpha Function: g_{syn} = \frac{(t-t_0)}{\tau} exp(\frac{t-t_o}{\tau})", fontsize=16)
plt.savefig('alpha_function.png')
plt.show()
