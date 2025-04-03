import scipy.stats as stats

# Üç grup için örnek veriler
grup1 = [20, 22, 19, 24, 23, 21]
grup2 = [17, 18, 20, 16, 22, 19]
grup3 = [25, 27, 26, 28, 29, 30]

# ANOVA testi
f_istatistik, p_degeri = stats.f_oneway(grup1, grup2, grup3)

print(f"ANOVA Test İstatistiği: {f_istatistik:.4f}")
print(f"P-Değeri: {p_degeri:.4f}")
