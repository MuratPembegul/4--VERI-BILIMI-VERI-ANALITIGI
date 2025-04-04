from sklearn.decomposition import PCA

# PCA ile boyut azaltma
pca = PCA(n_components=2)
pca_data = pca.fit_transform(data_scaled)

# K-Means tekrar uygulanıyor
kmeans_pca = KMeans(n_clusters=3, random_state=42)
clusters_pca = kmeans_pca.fit_predict(pca_data)

plt.scatter(pca_data[:, 0], pca_data[:, 1], c=clusters_pca, cmap='coolwarm')
plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.title("PCA ile Müşteri Segmentasyonu")
plt.show()
