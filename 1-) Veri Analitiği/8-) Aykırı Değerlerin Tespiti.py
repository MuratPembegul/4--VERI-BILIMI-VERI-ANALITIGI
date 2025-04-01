# Yaş değişkeni için aykırı değerlerin tespiti
sns.boxplot(x=data['Age'])
plt.title('Yaş Aykırı Değerleri')
plt.show()

# Aykırı değerleri kaldırma
q1 = data['Age'].quantile(0.25)
q3 = data['Age'].quantile(0.75)
iqr = q3 - q1
data = data[(data['Age'] >= (q1 - 1.5 * iqr)) & (data['Age'] <= (q3 + 1.5 * iqr))]
