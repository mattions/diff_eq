import pylab as p

def alpha(v, v_half=30, s=10, phi=.8):
   """
   forward rate

   v_half: voltage where half of the channels are open
   s: "effective temperature"/thermal energy
   phi: transition  rate constant
   """
   return phi * p.exp( (v - v_half)/s )

def beta(v, v_half=30, s=10, phi=.8):
   """
   backward rate

   v_half: voltage where half of the channels are open
   s: "effective temperature"
   phi: transition  rate constant
   """
   return phi * p.exp( -(v - v_half)/s )

def tau(v, v_half=30, s=10, phi=.8):
   """
   effective time constant

   as obtained from the channel openeing and closing rates
   """
   a = alpha(v, v_half, s, phi)
   b = beta(v, v_half, s, phi)
   return 1./(a+b)

def n_stationary(v, v_half=30, s=10, phi=.8):
   """
   stationary state of the channel's activation function
   depending on voltage (and channel properties)
   """
   a = alpha(v, v_half, s, phi)
   b = beta(v, v_half, s, phi)
   return a/(a+b)

# now plot n_v and tau_v

v = p.arange(-100., 100., 0.1)
p.plot(v, n_stationary(v), label="activation function")
p.plot(v, tau(v), label="time constant [inverse phi]")
p.legend(loc='upper left')
p.title('Gate Model', size=20)
p.xlabel('voltage [mV]', size=15)

p.axis([-100, 100, -0.1, 1.1])
p.show()
p.savefig('gate_model.png')

