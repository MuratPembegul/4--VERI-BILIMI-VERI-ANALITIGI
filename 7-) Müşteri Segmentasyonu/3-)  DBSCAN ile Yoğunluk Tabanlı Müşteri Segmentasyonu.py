from sklearn.cluster import DBSCAN

# DBSCAN modeli
dbscan = DBSCAN(eps=1, min_samples=2)
data['DBSCAN_Segment'] = dbscan.fit_predict(data_scaled)

print(data)
