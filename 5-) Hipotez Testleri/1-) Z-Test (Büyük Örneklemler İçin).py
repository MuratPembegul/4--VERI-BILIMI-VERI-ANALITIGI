import numpy as np
import statsmodels.api as sm

# Örnek veri
veri = np.array([10, 12, 9, 11, 13, 8, 12, 14, 9, 10])

# Örnek ortalaması ve bilinen popülasyon standart sapması
ortalama = np.mean(veri)
pop_std = 2  # Popülasyonun standart sapması biliniyor varsayımı

# Z-test
z_test = (ortalama - 10) / (pop_std / np.sqrt(len(veri)))  # Hipotez ortalaması: 10
p_degeri = 2 * (1 - sm.stats.norm.cdf(abs(z_test)))  # İki taraflı test

print(f"Z-Test İstatistiği: {z_test:.4f}")
print(f"P-Değeri: {p_degeri:.4f}")
