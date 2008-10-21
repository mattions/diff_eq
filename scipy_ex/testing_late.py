import pylab as p
from scipy import integrate
from matplotlib import rc
rc('text', usetex=True)

x = p.arange(0,15)
p.plot(x, p.exp(x))
p.title(r'function: $y = e^{x}$')
p.show()
