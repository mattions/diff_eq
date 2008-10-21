import pylab as p

def ghk_current(x,cr,c_0=1.0):
   """
   the Goldman-Hodgkin-Katz current equation
   x: the normalized voltage
   cr: the concentration ratio
   c_0: the reference (inside) concentration
   """
   c_in  = c_0
   c_out = cr*c_0
   ex = p.exp(-x)
   return x*(c_in - c_out*ex)/(1. - ex)

# voltage range
x = p.linspace(-3.0,3.0,1000)

# concentration ratios
crs = (0.1, 0.5, 1.0, 2.0, 10)

for cr in crs:
   label = "c_out = %s c_in" % cr
   p.plot(x,ghk_current(x,cr), label=label)

p.axvline(0, linestyle=':', linewidth=2, color='black', label='_nolegend_')
p.axhline(0, linestyle=':', linewidth=2, color='black', label='_nolegend_')
p.grid()

p.title("Goldman-Hodgkin-Katz current equation")
p.xlabel("voltage (normalized)")
p.ylabel("current (normalized)")

p.legend(loc='upper left')

p.axis([-3, 3, -3, 3])
p.show()

p.savefig('ghk_current.eps')
p.savefig('ghk_current.png')
p.savefig('ghk_current.svg')

