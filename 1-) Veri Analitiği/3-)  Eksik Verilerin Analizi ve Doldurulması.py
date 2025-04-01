import pandas as pd
import numpy as np

# Örnek veri setini yükleyelim
data = pd.read_csv('titanic.csv')

# Eksik verileri kontrol et
missing_data = data.isnull().sum()
print(missing_data)

# Eksik verileri medyan ile doldurma
data['Age'].fillna(data['Age'].median(), inplace=True)

# Eksik verilerden sonra son durumu kontrol et
print(data.isnull().sum())
