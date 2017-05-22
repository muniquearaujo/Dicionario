#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt 
import numpy as np
import math

T={"Mercúrio":0.241,"Vênus":0.615,"Terra":1,"Marte":1.88,"Júpiter":11.86,"Saturno":29.5, "Urano":84.0, "Plutão":248.0}
R={"Mercúrio":0.387,"Vênus":0.723,"Terra":1,"Marte":1.523,"Júpiter":5.202,"Saturno":9.539, "Urano":19.18, "Plutão":39.44}

periodo=[t**2 for t in T.values()]
distancia=[d**3 for d in R.values()]

ax=plt.gca()
plt.xscale('log')
plt.yscale('log')
ax.autoscale()
plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'$r^3$(UA)')
plt.ylabel('$T^2$ (anos)')

plt.title(r'Periodo $\times$ Distancia', fontsize=12)
plt.grid()
plt.plot(periodo,distancia, '-c')
plt.savefig("kepler.pdf", dpi=96)
plt.show()
