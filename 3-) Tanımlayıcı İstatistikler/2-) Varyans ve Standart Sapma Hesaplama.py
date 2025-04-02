import numpy as np

veri = [5, 10, 15, 20, 25, 30]

varyans = np.var(veri, ddof=1)  # Örnek varyans
std_sapma = np.std(veri, ddof=1)  # Örnek standart sapma

print(f"Varyans: {varyans}")
print(f"Standart Sapma: {std_sapma}")
