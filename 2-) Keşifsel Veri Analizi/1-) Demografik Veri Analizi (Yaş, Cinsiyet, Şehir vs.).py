import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Örnek kişisel veri seti oluşturma
data = pd.DataFrame({
    'Ad': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma', 'Ali', 'Zeynep', 'Hasan', 'Elif'],
    'Yaş': [25, 32, 40, 29, 50, 22, 36, 41],
    'Cinsiyet': ['Erkek', 'Erkek', 'Kadın', 'Kadın', 'Erkek', 'Kadın', 'Erkek', 'Kadın'],
    'Şehir': ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya', 'Konya', 'Adana', 'Eskişehir']
})

# Cinsiyet Dağılımı
sns.countplot(x=data['Cinsiyet'])
plt.title("Cinsiyet Dağılımı")
plt.show()

# Yaş Histogramı
sns.histplot(data['Yaş'], bins=5, kde=True)
plt.title("Yaş Dağılımı")
plt.show()
