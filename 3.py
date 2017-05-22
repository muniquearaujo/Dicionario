#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt 
import numpy as np
import math

class Planeta:
	def __init__(self, nome, massa, x,y):
		self.nome=nome
		self.massa=massa
		self.x=x
		self.y=y
		
	def distancia(self):
		return math.sqrt(self.x**2+self.y**2)
	
	def forca(self):
		G=6.67408*10**(-11)
		ms=1.98892*10**(30)
		return ((G*ms*self.massa)/(self.distancia())**2)
	
	def periodo(self):
		return math.sqrt(self.distancia()**3)

nome=raw_input('Informe o nome do planeta:\n')
massa=input('Informe a massa:\n')
x=input('Informe a posição em x:\n')		
y=input('Informe a posição em y:\n')
p=Planeta(nome, massa, x, y)
print "Distância do Planeta ao Sol", p.distancia()
print "Força de Atração Gravitacional entre o Planeta e o Sol", p.forca()		
print "Período de oscilação do Planeta", p.periodo()		
