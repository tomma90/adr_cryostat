import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cnt
from scipy.integrate import quad

# Vespel SP1 from 3K to 500mK
# 4 bars:
# lenght 110 mm
# outer radius 5 mm
# inner radius 4 mm
n3K_500mK = 4 
l3K_500mK = 110.e-3
r_out3K_500mK = 5.e-3
r_in3K_500mK = 4.e-3

# Single bar 3K-500mK cross-section
A3K_500mK = np.pi * r_out3K_500mK * r_out3K_500mK - np.pi * r_in3K_500mK * r_in3K_500mK

# Vespel SP22 from 500K to 100mK
# 8 bars:
# lenght 96 mm
# outer radius 3 mm
n500mK_100mK = 8
l500mK_100mK = 96.e-3
r_out500mK_100mK = 3.e-3

# Single bar 500mK-100mK cross-section
A500mK_100mK = np.pi * r_out500mK_100mK * r_out500mK_100mK

# Cooling capacity (see https://arxiv.org/abs/1911.11902)
# 500 mK
J_cooling_500mK = 1.2 #J
# 100 mK
J_cooling_100mK = 120.e-3 #J

P3K_500mK = quad(vespel_sp_22, 0.5, 3.0)[0] * A3K_500mK / l3K_500mK
P3K_500mK_total = P3K_500mK * n3K_500mK

P500mK_100mK = quad(vespel_sp_22, 0.1, 0.5)[0] * A500mK_100mK / l500mK_100mK
P500mK_100mK_total = P500mK_100mK * n500mK_100mK
