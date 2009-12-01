# Exp2Syn. To see how it is plotted

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from numpy import exp

t = np.linspace(0,100, num=1000)

tau1 = 9
tau2 = 10
weight = 1

def exp2syn(t, tau1, tau2, weight):
   
   g = weight * (exp (-t/tau2) - exp(-t/tau1))
   return g
   
g = exp2syn(t, tau1, tau2, weight)   
plt.plot(t, g, label="conductance")
plt.savefig('exp2syn.png')
plt.show()

