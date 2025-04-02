import numpy as np
import matplotlib.pyplot as plt

veri = [10, 20, 30, 40, 50, 60, 100, 150, 200, 250]  # Aykırı değerler var!

plt.boxplot(veri, patch_artist=True)
plt.title("Kutu Grafiği (Boxplot)")
plt.show()
