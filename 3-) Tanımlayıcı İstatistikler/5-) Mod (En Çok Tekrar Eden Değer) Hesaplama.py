from scipy import stats

veri = [3, 3, 3, 7, 7, 8, 9, 10, 10, 10, 10]

mod = stats.mode(veri)
print(f"Mod: {mod.mode[0]} (Frekans: {mod.count[0]})")
