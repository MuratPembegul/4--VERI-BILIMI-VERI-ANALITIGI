import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Örnek veri: Çalışma saati ve gelir ilişkisi
data = pd.DataFrame({
    'Çalışma Saati': [20, 25, 30, 35, 40, 45, 50, 55, 60],
    'Gelir': [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]
})

X = data[['Çalışma Saati']]
y = data['Gelir']

# Modeli eğitme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Gelir tahmini
y_pred = model.predict(X_test)

# Sonuçları görselleştirme
plt.scatter(data['Çalışma Saati'], data['Gelir'], color='blue', label="Gerçek Veriler")
plt.plot(X_test, y_pred, color='red', linewidth=2, label="Tahmin Edilen Çizgi")
plt.xlabel("Çalışma Saati")
plt.ylabel("Gelir")
plt.title("Basit Doğrusal Regresyon ile Gelir Tahmini")
plt.legend()
plt.show()
