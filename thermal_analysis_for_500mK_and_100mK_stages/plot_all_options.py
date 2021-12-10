import numpy as np
import matplotlib.pyplot as plt
import thermal_conductivity_vespel as tcv
import thermal_conductivity_torlon as tct

T = np.linspace(0.01,10., 1000)

k_vsp1 = tcv.vespel_sp_1(T)
k_vsp22 = tcv.vespel_sp_22(T)
k_t4203 = tct.torlon_4203(T) 

plt.figure()
plt.title('Conductivity of Vespel and Torlon 0.01-10 K', fontsize=25)
plt.loglog(T, k_vsp1, label = 'vespel sp1')
plt.loglog(T, k_vsp22, label = 'vespel sp22')
plt.loglog(T, k_t4203, label = 'torlon 4203')
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.xlabel('T [K]', fontsize = 20)
plt.ylabel('k [Wm-1K-1]', fontsize = 20)
plt.legend()
plt.tight_layout()
plt.show()
