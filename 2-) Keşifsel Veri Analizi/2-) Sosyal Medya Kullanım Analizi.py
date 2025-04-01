import numpy as np

# Sosyal medya kullanım verileri (Dakika cinsinden)
social_data = pd.DataFrame({
    'Kullanıcı': ['Ali', 'Ayşe', 'Mehmet', 'Zeynep', 'Hasan', 'Fatma'],
    'Instagram': [120, 80, 45, 200, 130, 75],
    'Twitter': [30, 50, 40, 60, 20, 15],
    'Facebook': [60, 30, 20, 90, 55, 25],
    'TikTok': [90, 120, 30, 150, 110, 70]
})

# Kullanıcı başına toplam sosyal medya süresi
social_data["Toplam Süre"] = social_data[['Instagram', 'Twitter', 'Facebook', 'TikTok']].sum(axis=1)

# Görselleştirme
sns.barplot(x=social_data['Kullanıcı'], y=social_data['Toplam Süre'])
plt.title("Kullanıcı Başına Toplam Sosyal Medya Kullanımı (Dakika)")
plt.show()
