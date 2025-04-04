from sklearn.linear_model import LinearRegression

# Örnek veri: Alan, oda sayısı ve ev fiyatı
data = pd.DataFrame({
    'Alan': [50, 60, 80, 100, 120, 150],
    'Oda Sayısı': [1, 2, 2, 3, 3, 4],
    'Fiyat': [200000, 250000, 300000, 350000, 400000, 500000]
})

X = data[['Alan', 'Oda Sayısı']]
y = data['Fiyat']

# Model eğitme
model = LinearRegression()
model.fit(X, y)

# Yeni bir ev fiyatı tahmini
y_pred = model.predict([[90, 2]])  # 90 m², 2 odalı ev fiyatı tahmini
print(f"90m², 2 odalı ev tahmini fiyatı: {y_pred[0]:,.2f} TL")
