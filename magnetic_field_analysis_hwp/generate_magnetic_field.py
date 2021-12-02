import numpy as np                                                               
import matplotlib.pyplot as plt                                                  
import define_magnet as dm

x = np.linspace(0., 1., 10000)
B = dm.B_ring(1.1e4, 12e-3, 68.5e-3, 58.5e-3, x)

plt.figure()
plt.plot(x, B)

plt.show()
