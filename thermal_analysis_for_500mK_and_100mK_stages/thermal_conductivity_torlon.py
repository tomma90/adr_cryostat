import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cnt

# Thermal conductivity for Torlon 4203 from: https://ui.adsabs.harvard.edu/abs/1999Cryo...39..481V/abstract

def thermal_conductivity(a, b, T):
	
	k = a * T**(b)
	
	return k
	
def torlon_4203(T):
	
	a = 6.e-3 # Wm-1K-1
	b = 2.18
	
	k_torlon = thermal_conductivity(a, b, T)
	
	return k_torlon
