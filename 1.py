import numpy as np
import matplotlib.pyplot as plt

x = np.array([15, 20, 25, 30, 35, 40, 45, 50])
y = np.array([73.1, 72.62, 72.7, 72.8, 72.1, 71.6, 71.7, 71.5])

plt.figure()


plt.plot(x, y, 'o-', color="#c64328", markerfacecolor='white', markersize=10, linewidth=3, label = "Citeseer")
plt.tick_params(axis='both', labelsize=20)  

plt.xlim(10, 55)
plt.ylim(71, 73.5)

plt.legend(fontsize=20, loc='best')       

plt.grid(True)

plt.savefig('k_1.svg', format='svg', bbox_inches='tight')
