import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

veri = np.random.rand(10, 10)
sns.heatmap(veri, cmap='coolwarm', annot=True)
plt.title("Isı Haritası")
plt.show()
