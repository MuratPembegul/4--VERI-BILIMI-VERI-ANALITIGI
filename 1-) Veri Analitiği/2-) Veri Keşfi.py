import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Veri Keşfi (EDA)
df = sns.load_dataset("titanic")
print(df.head())
print(df.info())
print(df.describe())

# 2. Veri Temizleme (Eksik Veriler)
print(df.isnull().sum())
df.fillna(df.median(), inplace=True)

# 3. Özet İstatistikler
print("Yaş Ortalaması:", df["age"].mean())
print("Medyan Ücret:", df["fare"].median())

# 4. Veri Görselleştirme
plt.figure(figsize=(8, 5))
sns.histplot(df["age"], bins=30, kde=True)
plt.title("Yaş Dağılımı")
plt.show()

# 5. Eksik Veri Analizi
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Eksik Veri Haritası")
plt.show()

# 6. Aykırı Değer Analizi
plt.figure(figsize=(6, 4))
sns.boxplot(x=df["fare"])
plt.title("Ücret Aykırı Değerler")
plt.show()

# 7. Korelasyon Analizi
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Korelasyon Matrisi")
plt.show()

# 8. Özellik Mühendisliği (Yeni Özellik Ekleme)
df["family_size"] = df["sibsp"] + df["parch"] + 1
print(df[["sibsp", "parch", "family_size"].head()])

# 9. Zaman Serisi Analizi (Eğer tarih varsa)
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    df.resample("M").mean().plot()
    plt.title("Aylık Ortalama Değerler")
    plt.show()

# 10. Makine Öğrenmesi İçin Veri Hazırlama
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df.dropna(inplace=True)  # Eksik verileri at
X = df.drop(["survived"], axis=1)
y = df["survived"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Veri analitiği işlemleri tamamlandı!")
