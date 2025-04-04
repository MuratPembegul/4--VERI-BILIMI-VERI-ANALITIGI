# Yaş dağılımı (Histogram)
plt.figure(figsize=(8, 6))
sns.histplot(data['Age'], bins=30, kde=True)
plt.title('Yaş Dağılımı')
plt.show()

# Sınıf dağılımı (Bar plot)
plt.figure(figsize=(8, 6))
sns.countplot(x='Pclass', data=data)
plt.title('Sınıf Dağılımı')
plt.show()

# Yaş ve Fiyatın ilişkisinin görselleştirilmesi (Boxplot)
plt.figure(figsize=(8, 6))
sns.boxplot(x='Pclass', y='Age', data=data)
plt.title('Yaş ve Sınıf İlişkisi')
plt.show()
