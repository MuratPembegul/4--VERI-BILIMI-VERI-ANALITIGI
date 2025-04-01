import seaborn as sns
import matplotlib.pyplot as plt

# Korelasyon matrisi
correlation_matrix = data.corr()

# Isı haritası ile görselleştirme
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Korelasyon Matrisi')
plt.show()
