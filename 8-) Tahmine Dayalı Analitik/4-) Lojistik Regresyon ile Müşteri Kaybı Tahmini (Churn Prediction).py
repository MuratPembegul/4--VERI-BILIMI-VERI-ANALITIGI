from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Örnek müşteri verisi: Harcama süresi ve abonelik devamlılığı
data = pd.DataFrame({
    'Harcama Süresi (ay)': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Abonelik Devam mı?': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
})

X = data[['Harcama Süresi (ay)']]
y = data['Abonelik Devam mı?']

# Model eğitme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# Tahmin ve doğruluk
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Doğruluğu: {accuracy:.2%}")

# Yeni müşteri tahmini
yeni_musteri = model.predict([[7]])  # 7 ay harcama süresi olan müşteri
print("7 aydır harcama yapan müşteri aboneliği devam ettirir mi?", "Evet" if yeni_musteri[0] == 1 else "Hayır")
