# Örnek uyku verisi
sleep_data = pd.DataFrame({
    'Gün': ['Pzt', 'Sal', 'Çrş', 'Prş', 'Cum', 'Cmt', 'Paz'],
    'Uyku Süresi (Saat)': [6, 7, 5, 8, 4, 10, 9],
    'Uyku Kalitesi (1-10)': [6, 7, 5, 8, 4, 9, 9]
})

# Scatter plot ile uyku süresi ve kalitesi arasındaki ilişki
sns.scatterplot(x=sleep_data['Uyku Süresi (Saat)'], y=sleep_data['Uyku Kalitesi (1-10)'])
plt.title("Uyku Süresi ve Uyku Kalitesi İlişkisi")
plt.show()
