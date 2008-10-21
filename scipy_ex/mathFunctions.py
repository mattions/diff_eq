# This file contains several math functions that are useful

import numpy
from matplotlib import rc
from pylab import *

def hill(x,theta,n):
   """
   return the result of an hill function
   defined as y = x^n / ( theta^n + x^n )
   Parameters:
      x
         point where to calculate the function
      theta
         Activation coefficient -- govern the change of the function
      n
         Hill coefficient -- govern the stepness of the Hill function
         
   """
   y = pow(x, n) / (pow(theta, n) + pow(x, n))

   print "Activation coefficient (theta) %d\tStepness coefficient (n) %d" %(theta,n)
   return y
   
def michaelisMenten(x, vMax, Km):
   """
   Return the result of a Michaelis Menten Kinetik
   defined as y =  Vmax * x / (Km + x)
   :Parameters:
      x
         Concentration of the specie
      vMax
         velocity Maxima of the reaction
      Km
         Constant of the reaction
   """   
   y = vMax *( x / (Km + x))
   return y
   
   
texOn = True
rc('text', usetex=texOn)    # Activating Tex. Used in the plot title
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})


x = numpy.arange(0,10,0.1)

def plotHills():
   figure()

   plot(x,hill(x,5,4))
   if texOn:
      title(r"Hill's equation: $ y = \frac{x^{n}}{\theta^{n} + x^{n}}$. $n=4$  $\theta=5$", fontsize=16)


   figure()
   nList = [0,1,4,5,9]
   theta = 5

   for n in nList:

      plot(x,hill(x,theta,n), label=r"$n$ = " + str(n))

      if texOn:
         title(r"Hill's equation: $ y = \frac{x^{n}}{\theta^{n} + x^{n}}$. $n$ Variable. $\theta$=" + str(theta), fontsize=16)
   legend()
      
   thetaList = [0,1,4,5,9]
   n = 4

   figure()
   for theta in thetaList:

      plot(x,hill(x,theta,n), label=r"$\theta$ = " + str(theta))
      
      if texOn:
         title(r"Hill's equation: $ y = \frac{x^n}{\theta^n + x^n}$. $\theta$ Variable. $n$=" + str(n), fontsize=16)
   legend() #drawing the legend


######### 
# Michaelis Menten

def plotMich():
   figure()
   vMax = 10
   Km = 70
   s = numpy.arange(0,4000,0.1)
   plot(s,michaelisMenten(s,vMax,Km))
   if texOn:
      title(r"Michaelis Menten equation: $\frac{d[P]}{dt} = V_{max} \frac{ [x]}{K_m + [x]}$", fontsize=16)


if __name__ == "__main__":
   plotHills()
   plotMich()

show()
