import pylab as p
import numpy
from scipy import integrate
from matplotlib import rc
rc('text', usetex=True)

## definy some global variable here

#Potassium

g_k=36.0 # maximal potassium conductance (in mS/cm^2)
e_k=-77.0 # potassium reversal potential (in mV)

#Sodium
g_na=120.0 # maximal sodium conductance (in mS/cm^2)
e_na=-50.0 # sodium reversal potential (in mV)

#Leakage
g_l=0.3 # maximal leakage conductance (in mS/cm^2)
e_l=-54.4 # leakage reversal potential (in mV)

# Conductance
c = 1
I = -50

def alpha(v,gate):
   """
   forward rate of the Hudgkin-Huxley potassium gate
   """
   if gate=='n':
      v_centered = v + 55
      return 0.01 * v_centered / (1 - p.exp(-v_centered/10.))
   elif gate=='m':
      return 0.1 * (v + 40) / (1 - p.exp( -(v + 40)/10))
   elif gate=='h':
      return 0.07 * p.exp( - (v + 65) / 20)
      
      
def beta(v, gate):
   """
   backward rate of the Hudgkin-Huxley potassium gate
   """
   if gate=='n':
      return 0.125 * p.exp( (v+65)/-80. )
   elif gate=='m':
      return 4 * p.exp(-(v+65) / 18)
   elif gate=='h':
      return 1 / (1 + p.exp( -(v+35) / 10 ))

def tau(v, gate):
   """
   effective time constant of the Hudgkin-Huxley potassium gate

   as obtained from the channel openeing and closing rates
   """
   a = alpha(v, gate)
   b = beta(v, gate)
   return 1./(a+b)
   
def gate_stationary(v, gate):
   """
   stationary state of the Hudgkin-Huxley potassium gate's
   activation function depending on voltage
   """
   a = alpha(v,gate)
   b = beta(v,gate)
   return a/(a+b)



def hh_ode(x, t):
   """
   ODE for the Hodgkin-Huxley potassium component

   x: array of the form [voltage, activation n, activation m, activation h]
   t: time
   g_k: maximal potassium conductance (in mS/cm^2)
   e_k: potassium reversal potential (in mV)
   """
   v = x[0]
   n = x[1]
   m = x[2]
   h = x[3]
   dvdt = (I - (g_k * n**4 * (v - e_k) + g_na * m**3 * h * (v - e_na) + g_l * (v -e_l) ))/c
#   dvdt = (I - (g_k * n**4 * (v - e_k) ))/c
#   dvdt = g_k * n**4 * (e_k - v)
   dndt = alpha(v, 'n') * (1-n) - beta(v,'n') * n
   dmdt = alpha(v, 'm') * (1-m) - beta(v,'m') * m
   dhdt = alpha(v, 'h') * (1-h) - beta(v,'h') * h
   return p.array([dvdt, dndt, dmdt, dhdt])

def hh_potassium_current(x):
   """
   the Hodgkin-Huxley potassium current

   x: array of the form [voltage, activation n, activation m, activation h]
   """
   v = x[:,0]
   n = x[:,1]
   return g_k * n**4 * (v - e_k)
   
def hh_sodium_current(x):
   """
   the Hodgkin-Huxley sodium current

   x: array of the form [voltage, activation n, activation m, activation h]
   """
   
   v = x[:,0]
   m = x[:,2]
   h = x[:,3]
   return  g_na * m**3 * h * (v - e_na)
   
# first, plot n(v) and tau(v)

v = p.arange(-150., 150., 0.1)
p.plot(v, gate_stationary(v, 'n'), label="n activation function")
p.plot(v, gate_stationary(v, 'm'), label="m activation function")
p.plot(v, gate_stationary(v, 'h'), label="h activation function")
#p.plot(v, 0.1*tau(v, 'n'), label="n time constant [10 ms]")
#p.plot(v, 0.1*tau(v, 'm'), label="m time constant [10 ms]")
#p.plot(v, 0.1*tau(v, 'h'), label="h time constant [10 ms]")
p.legend(loc='best')
p.xlabel('voltage [mV]')
p.title('Hodgkin-Huxley gate variable channel')

p.axis([-150, 150, -0.1, 1.1])
#p.show()
p.savefig('hh_potassiumactivation.png')

# next, plot the voltage and potassium current
# in response to an initial condition away from
# equilibrium (but no other stimulation)

# initial condition

n_0 = 0.317
m_0 = 0.052
h_0 = 0.596


x_0 = p.array([-65., n_0, m_0, h_0]) # [voltage, activation]

# time resolution and duration
dt = 0.01
t_before_stim  = p.arange(0,30,dt)
t_after_stim = p.arange(30,100,dt)

# trajectory x(t) (format: [t,[voltage, activation]])
x_t_0 = integrate.odeint(hh_ode, x_0, t_before_stim, full_output=0, mxstep=10000)
x_1 = x_t_0[-1] # Taking the last point
x_1[0] = -50.0 # Given the stimulus
x_t_1 = integrate.odeint(hh_ode, x_1, t_after_stim, full_output=0, mxstep=10000)

# Join them together
x_t = numpy.append(x_t_0, x_t_1, axis=0) # The voltage
t = numpy.append(t_before_stim, t_after_stim)


print(x_t)

# plot the results
p.figure(2)
p.subplot(3,1,1)
p.plot(t, x_t[:,0])
p.ylabel('voltage [mV]')
p.title('Hodgkin-Huxley ', size=16)

p.subplot(3,1,2)
p.plot(t, hh_potassium_current(x_t))
p.ylabel(r"K current $\[\mu \rm{A/cm}^2\]$")
#p.xlabel('time [ms]', size=15)

p.subplot(3,1,3)
p.plot(t, hh_sodium_current(x_t))
p.ylabel(r"Na current $\[\mu \rm{A/cm}^2\]$")
p.xlabel('time [ms]', size=15)

p.show()
p.savefig('hh_current.png')

