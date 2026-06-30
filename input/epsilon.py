import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np
plt.rcParams["figure.dpi"]=150
plt.rcParams["figure.facecolor"]="white"

data_r = np.loadtxt('./epsr_mos2bulk.dat')
data_i = np.loadtxt('./epsi_mos2bulk.dat')
energy_r, epsilon_r = data_r[:, 0], data_r[:, 1]
energy_i, epsilon_i = data_i[:, 0], data_i[:, 1]

plt.plot(energy_r, epsilon_r, lw=1, label="$\\epsilon_1$")
plt.plot(energy_i, epsilon_i, lw=1, label="$\\epsilon_2$")
plt.xlim(0, 15)
plt.xlabel("Energy (eV)", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel("$\\epsilon_1~/~\\epsilon_2$", fontsize=16 )
plt.legend(frameon=False, fontsize=16)
plt.tight_layout()
plt.savefig("./espilonbulk.png")
