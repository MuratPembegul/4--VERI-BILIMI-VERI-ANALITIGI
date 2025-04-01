# Örnek finansal veri seti
finance_data = pd.DataFrame({
    'Kategori': ['Market', 'Fatura', 'Ulaşım', 'Eğlence', 'Yemek'],
    'Harcama': [750, 1200, 500, 300, 900]
})

# Pasta Grafiği ile Harcama Dağılımı
plt.figure(figsize=(7, 7))
plt.pie(finance_data['Harcama'], labels=finance_data['Kategori'], autopct='%1.1f%%', startangle=140)
plt.title("Harcama Dağılımı")
plt.show()
