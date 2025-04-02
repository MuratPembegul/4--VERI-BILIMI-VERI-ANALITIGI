import numpy as np
import matplotlib.pyplot as plt

veri = np.random.normal(50, 15, 1000)  # Ortalama 50, Standart Sapma 15, 1000 veri noktası
plt.hist(veri, bins=20, color='g', edgecolor='black', alpha=0.7)
plt.xlabel("Değerler")
plt.ylabel("Frekans")
plt.title("Histogram Grafiği")
plt.show()
