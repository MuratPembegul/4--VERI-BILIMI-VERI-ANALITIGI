import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Örnek veri
data = pd.DataFrame({
    'Gelir': [15000, 18000, 30000, 50000, 70000, 100000, 120000, 300000],
    'Harcama': [2000, 2500, 4000, 10000, 20000, 25000, 30000, 50000]
})

# Veriyi ölçeklendirme
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# K-Means modeli
kmeans = KMeans(n_clusters=3, random_state=42)
data['Segment'] = kmeans.fit_predict(data_scaled)

# Sonuçları görselleştirme
plt.scatter(data['Gelir'], data['Harcama'], c=data['Segment'], cmap='viridis')
plt.xlabel("Gelir")
plt.ylabel("Harcama")
plt.title("K-Means ile Müşteri Segmentasyonu")
plt.show()
