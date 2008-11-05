#!/usr/bin/env python

# Simulation D'alcantara with pysces

import pysces
#mod = pysces.model('/home/mattions/Work/model/diff_eq/Fernandez/BIOMD0000000152.xml')
mod = pysces.model('/home/mattions/Work/model/diff_eq/Dalcantara_model/dAlcantara2003.xml')
mod.doLoad()
mod.doSimPlot(end=600.00)