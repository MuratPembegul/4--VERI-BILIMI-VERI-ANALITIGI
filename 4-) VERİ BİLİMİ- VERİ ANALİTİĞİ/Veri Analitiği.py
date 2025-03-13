# 📌 Gerekli kütüphaneleri içe aktaralım
import pandas as pd  # Veri işleme ve analiz için
import numpy as np   # Sayısal işlemler için
import matplotlib.pyplot as plt  # Grafik çizmek için
import seaborn as sns  # Veri görselleştirme için

# 📌 Örnek bir veri seti oluşturalım
data = {
    "Müşteri_ID": [101, 102, 103, 104, 105],
    "Yaş": [25, 30, 35, np.nan, 45],  # Yaş sütununda eksik değer var
    "Gelir": [3000, 4000, 5000, 6000, 7000],
    "Harcamalar": [2000, np.nan, 3000, 4000, 5000]  # Eksik değer var
}

# 📌 Veriyi bir pandas DataFrame'e çevirelim
df = pd.DataFrame(data)

# 📌 1️⃣ Veri Önizleme
print("📊 Veri Önizleme:")
print(df.head())  # İlk 5 satırı göster

# 📌 2️⃣ Eksik Verileri Doldurma
print("\n🔍 Eksik verileri doldurmadan önce:")
print(df.isnull().sum())  # Hangi sütunda eksik veri var göster

# Eksik verileri ortalama ile dolduralım
df["Yaş"].fillna(df["Yaş"].mean(), inplace=True)
df["Harcamalar"].fillna(df["Harcamalar"].mean(), inplace=True)

print("\n✅ Eksik verileri doldurduktan sonra:")
print(df.isnull().sum())  # Tekrar kontrol edelim

# 📌 3️⃣ Temel İstatistiksel Analizler
print("\n📊 Temel İstatistikler:")
print(df.describe())  # Veri hakkında özet bilgiler

# 📌 4️⃣ Veri Görselleştirme
plt.figure(figsize=(10, 5))

# Yaş dağılım grafiği
plt.subplot(1, 2, 1)
sns.histplot(df["Yaş"], bins=5, kde=True, color="blue")
plt.title("Yaş Dağılımı")

# Gelir vs Harcama ilişkisi
plt.subplot(1, 2, 2)
sns.scatterplot(x=df["Gelir"], y=df["Harcamalar"], color="red")
plt.title("Gelir - Harcama İlişkisi")

# 📌 Grafikleri göster
plt.tight_layout()
plt.show()
