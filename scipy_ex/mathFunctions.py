# This file contains several math functions that are useful

import numpy
from matplotlib import rc
from pylab import *

def hill(x,K,n):
   """
   return the result of an hill function
   defined as y = x^n / ( K^n + x^n )
   Parameters:
      x
         point where to calculate the function
      K
         Activation coefficient -- govern the change of the function
      n
         Hill coefficient -- govern the stepness of the Hill function
         
   """
   y = pow(x, n) / (pow(K, n) + pow(x, n))

   print "Activation coefficient (K) %d\tStepness coefficient (n) %d" %(K,n)
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

def plotHills():
   figure()
   K = 5
   n=2 
   plot(x,hill(x,K,n))
   if texOn:
      title_str = r"Hill like equation: $ y = \frac{x^{n}}{K^{n} + x^{n}}$. $n="
      title_str += "%.1f$" %n   
      title_str += r" $K="
      title_str += "%.1f$" %K
      title(title_str, fontsize=16)


   figure()
   nList = [1, 1.5, 2, 2.5, 3, 4]
   K = 5

   for n in nList:

      plot(x,hill(x,K,n), label=r"$n$ = " + str(n))

      if texOn:
        title_str = r"Hill like equation: $ y = \frac{x^{n}}{K^{n} + x^{n}}$. $n="
        title_str += "variable$"   
        title_str += r" $K="
        title_str += "%.1f$" %K
        title(title_str, fontsize=16)
   legend()
      
   KList = [0,1,10,50,90, 100, 1000, 2000]
   n = 3

   figure()
   for K in KList:

      plot(x,hill(x,K,n), label=r"$K$ = " + str(K))
      
      if texOn:
        title_str = r"Hill like equation: $ y = \frac{x^{n}}{K^{n} + x^{n}}$. $n="
        title_str += "%.1f$" %n   
        title_str += r" $K="
        title_str += "variable$"
        title(title_str, fontsize=16)
        
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
    texOn = True
    rc('text', usetex=texOn)    # Activating Tex. Used in the plot title
    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    x = numpy.linspace(0,1)
    plotHills()
    plotMich()

show()
