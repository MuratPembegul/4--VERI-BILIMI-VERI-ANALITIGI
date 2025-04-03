from scipy import stats

# İki grup için örnek veriler
grup1 = [20, 22, 19, 24, 23, 21]
grup2 = [17, 18, 20, 16, 22, 19]

# Bağımsız iki örneklem t-testi
t_istatistik, p_degeri = stats.ttest_ind(grup1, grup2)

print(f"T-Test İstatistiği: {t_istatistik:.4f}")
print(f"P-Değeri: {p_degeri:.4f}")
