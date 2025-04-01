# Cinsiyet gibi kategorik verileri sayısal verilere dönüştürme
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# Gemi sınıfı (Pclass) gibi kategorik verilerle aynı işlemi yapalım
data['Pclass'] = data['Pclass'].astype('category')
