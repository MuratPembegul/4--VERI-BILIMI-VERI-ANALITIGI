# Rastgele müşteri verisi
data_clv = pd.DataFrame({
    'Müşteri': ['A', 'B', 'C', 'D', 'E'],
    'Satın Alma Sıklığı': [5, 10, 20, 30, 50],
    'Ortalama Harcama': [100, 200, 150, 300, 400],
    'Sadakat': [1, 2, 3, 4, 5]
})

# CLV Hesaplama = Satın Alma Sıklığı x Ortalama Harcama x Sadakat
data_clv['CLV'] = data_clv['Satın Alma Sıklığı'] * data_clv['Ortalama Harcama'] * data_clv['Sadakat']

# CLV'ye göre segmentleme
data_clv['Segment'] = pd.qcut(data_clv['CLV'], 3, labels=["Düşük", "Orta", "Yüksek"])

print(data_clv)
