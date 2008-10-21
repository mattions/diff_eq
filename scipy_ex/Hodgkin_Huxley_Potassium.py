import pylab as p
from scipy import integrate
from matplotlib import rc
rc('text', usetex=True)

def alpha_n(v):
   """
   forward rate of the Hudgkin-Huxley potassium gate
   """
   v_centered = v + 55
   return 0.01 * v_centered / (1 - p.exp(-v_centered/10.))

def beta_n(v):
   """
   backward rate of the Hudgkin-Huxley potassium gate
   """
   return 0.125 * p.exp( (v+65)/-80. )

def tau_n(v):
   """
   effective time constant of the Hudgkin-Huxley potassium gate

   as obtained from the channel openeing and closing rates
   """
   a = alpha_n(v)
   b = beta_n(v)
   return 1./(a+b)

def n_stationary(v):
   """
   stationary state of the Hudgkin-Huxley potassium gate's
   activation function depending on voltage
   """
   a = alpha_n(v)
   b = beta_n(v)
   return a/(a+b)

def hh_potassium_ode(x, t, g_k=36., e_k=-77.):
   """
   ODE for the Hodgkin-Huxley potassium component

   x: array of the form [voltage, activation]
   t: time
   g_k: maximal potassium conductance (in mS/cm^2)
   e_k: potassium reversal potential (in mV)
   """
   v = x[0]
   n = x[1]
   dvdt = g_k * n**4 * (e_k - v)
   dndt = alpha_n(v) * (1-n) - beta_n(v) * n
   return p.array([dvdt, dndt])

def hh_potassium_current(x, g_k=36., e_k=-77.):
   """
   the Hodgkin-Huxley potassium current

   x: array of the form [time, [voltage, activation]]
   g_k: maximal potassium conductance (in mS/cm^2)
   e_k: potassium reversal potential (in mV)
   """
   v = x[:,0]
   n = x[:,1]
   return g_k * n**4 * (v - e_k)

# first, plot n(v) and tau(v)

v = p.arange(-150., 150., 0.1)
p.plot(v, n_stationary(v), label="activation function")
p.plot(v, 0.1*tau_n(v), label="time constant [10 ms]")
p.legend(loc='best')
p.xlabel('voltage [mV]')
p.title('Hodgkin-Huxley potassium channel')

p.axis([-150, 150, -0.1, 1.1])
#p.show()
p.savefig('hh_potassiumactivation.png')

# next, plot the voltage and potassium current
# in response to an initial condition away from
# equilibrium (but no other stimulation)

# initial condition
n_0 = 0.317
x_0 = p.array([-50., 0.317]) # [voltage, activation]

# time resolution and duration
dt = 0.1
t  = p.arange(0,30,dt)

# trajectory x(t) (format: [t,[voltage, activation]])
x_t = integrate.odeint(hh_potassium_ode, x_0, t)

# plot the results
p.figure(2)
p.subplot(2,1,1)
p.plot(t, x_t[:,0])
p.ylabel('voltage [mV]')
p.title('Hodgkin-Huxley (potassium channels only)', size=18)

p.subplot(2,1,2)
p.plot(t, hh_potassium_current(x_t))
p.ylabel(r"potassium current $\[\mu \rm{A/cm}^2\]$")
p.xlabel('time [ms]', size=15)
p.show()
p.savefig('hh_potassiumcurrent.png')

