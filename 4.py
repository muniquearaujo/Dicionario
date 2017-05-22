#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt 
import numpy as np
import math

class Planeta:
	def __init__(self, x,y):
		self.x=x
		self.y=y
		
	def operacao(self, outro):
		return math.sqrt((self.x-outro.x)**2+(self.y-outro.y)**2)
		
print "Planeta 1:"
x1=input('Informe a posição em x:\n')		
y1=input('Informe a posição em y:\n')		
p1=Planeta(x1,y1)

print "Planeta 2:"
x2=input('Informe a posição em x:\n')		
y2=input('Informe a posição em y:\n')		
p2=Planeta(x2,y2)

print "Distancia entre os Planetas", p1.operacao(p2)		
