# Örnek sağlık verisi
fitness_data = pd.DataFrame({
    'Gün': ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar'],
    'Adım Sayısı': [8000, 7500, 9200, 11000, 5000, 3000, 12000],
    'Kalori': [350, 320, 400, 500, 220, 150, 600]
})

# Adım sayısı grafiği
sns.lineplot(x=fitness_data['Gün'], y=fitness_data['Adım Sayısı'], marker='o', label='Adım Sayısı')
sns.lineplot(x=fitness_data['Gün'], y=fitness_data['Kalori'], marker='s', label='Kalori')
plt.title("Günlük Adım Sayısı ve Kalori Yakımı")
plt.show()
