import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='blue', alpha=0.5, edgecolors='black')
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.title("Dağılım Grafiği")
plt.show()
