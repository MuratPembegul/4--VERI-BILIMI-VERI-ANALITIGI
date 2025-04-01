# Örnek alışveriş verisi
ecommerce_data = pd.DataFrame({
    'Ürün': ['Telefon', 'Laptop', 'Kamera', 'Saat', 'Kulaklık'],
    'Fiyat': [10000, 25000, 8000, 4000, 2000],
    'Adet': [1, 2, 1, 3, 5]
})

# Toplam harcamayı hesaplayalım
ecommerce_data["Toplam Harcama"] = ecommerce_data['Fiyat'] * ecommerce_data['Adet']

# En çok harcanan ürünler
sns.barplot(x=ecommerce_data['Ürün'], y=ecommerce_data['Toplam Harcama'])
plt.title("Ürün Bazında Toplam Harcama")
plt.show()
