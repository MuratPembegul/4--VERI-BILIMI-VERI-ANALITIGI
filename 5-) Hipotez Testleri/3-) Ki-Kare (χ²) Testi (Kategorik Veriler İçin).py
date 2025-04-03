import scipy.stats as stats
import numpy as np

# Gözlenen ve beklenen değerler
gozlenen = np.array([[50, 30], [20, 40]])  # Örnek tablo (İki kategorili)
ki_kare, p_degeri, _, _ = stats.chi2_contingency(gozlenen)

print(f"Ki-Kare Test İstatistiği: {ki_kare:.4f}")
print(f"P-Değeri: {p_degeri:.4f}")
