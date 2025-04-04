from sklearn.ensemble import RandomForestRegressor

# Model oluşturma
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Yeni bir veri tahmini
y_pred_rf = model.predict([[90, 2]])  # 90 m², 2 odalı ev tahmini
print(f"90m², 2 odalı ev Random Forest tahmini fiyatı: {y_pred_rf[0]:,.2f} TL")
