import pylab as p

# step sizes
dts = (1.0, 0.5, 0.1, 0.05)

def approximate_x(dt=0.1):
   # time
   t = p.arange(0, 5+dt, dt)
   # initialize trajectory
   x = p.zeros(p.size(t), dtype='float')
   # set initial condition
   x[0] = 1.

   for i in range(p.size(t)-1):
      x[i+1] = x[i] - x[i]*dt

   return t, x

# analytical solution
t_real = p.arange(0,5,0.01)
x_real = p.exp(-t_real)

for dt in dts:
   label = "stepsize = %s" % dt
   t, x = approximate_x(dt)
   p.plot(t, x, label=label)
   p.plot(t,x, 'k,')

p.plot(t_real, x_real, label="real solution")
p.legend()
p.title(r"$\frac{dx}{dt} = - x$ initial condition $x_0 = 1$", size=16)
p.xlabel('time', size=15)
p.axis([0,5,0,1])
p.savefig('euler1.png')
p.show()


