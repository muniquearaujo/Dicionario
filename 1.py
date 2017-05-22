#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt 
import numpy as np
class Derivada:
	def __init__(self,x,funcao):
		self.x=x
		self.funcao=funcao
		
	def derivada(self):
		if funcao=="seno":
			h=10**(-9)
			return((np.sin(self.x+h)-np.sin(self.x))/h)
		if funcao=="cosseno":
			h=10**(-9)
			return((np.cos(self.x+h)-np.cos(self.x))/h)	
x=input('Informe o ponto\n')
funcao=raw_input('Qual função quer? Seno ou Cosseno?\n')
f1=Derivada(x,funcao)
print "Derivada de x é:", f1.derivada()
		
			
