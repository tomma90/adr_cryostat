import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cnt

mu0 = cnt.mu_0

# Magnetic field of a magnetic ring at distance x
# Br = remanence magnetization of the ring (Gauss)
# h = ring thickness (m)
# ro = outer radius (m)
# ri = inner radius (m)
# x = distance (m)

def B_ring(Br, h, ro, ri, x):
  
	A = (D+x)/np.sqrt(Ro*Ro+(D+x)*(D+x))
	B = x/np.sqrt(Ro*Ro+x*x)
	C = (D+x)/np.sqrt(Ri*Ri+(D+x)*(D+x))
	D = x/np.sqrt(Ri*Ri+x*x)
	
  return Br/2.*(A-B-C+D)
