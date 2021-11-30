import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cnt

# Thermal conductivity for Vespel from: https://arxiv.org/abs/0806.1921v1 

def thermal_conductivity(a, b, g, n, T):
	
	k = a * T**(b + g * T**n)
	
	return k
	
def vespel_sp_1(T):
	
	a = 2.23e-3 # Wm-1K-1
	b = 1.92
	g = -0.819
	n = 0.0589
	
	k_sp_1 = thermal_conductivity(a, b, g, n, T)
	
	return k_sp_1
	
def vespel_sp_22(T):
	
	a = 1.44e-3 # Wm-1K-1
	b = 2.11
	g = -0.521
	n = -0.0163
	
	k_sp_22 = thermal_conductivity(a, b, g, n, T)
	
	return k_sp_22
