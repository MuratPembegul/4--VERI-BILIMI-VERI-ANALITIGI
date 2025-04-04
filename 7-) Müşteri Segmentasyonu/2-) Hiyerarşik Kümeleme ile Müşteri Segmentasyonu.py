from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# Hiyerarşik kümeleme modeli
linked = linkage(data_scaled, method='ward')

plt.figure(figsize=(8, 5))
dendrogram(linked)
plt.title("Hiyerarşik Kümeleme Dendrogramı")
plt.show()

# Kümeleme işlemi
hc = AgglomerativeClustering(n_clusters=3)
data['Hiyerarşik_Segment'] = hc.fit_predict(data_scaled)

print(data)
