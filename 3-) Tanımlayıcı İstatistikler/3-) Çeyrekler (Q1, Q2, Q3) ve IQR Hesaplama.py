import numpy as np

veri = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

q1 = np.percentile(veri, 25)
q2 = np.percentile(veri, 50)  # Medyan
q3 = np.percentile(veri, 75)
iqr = q3 - q1  # IQR (Interquartile Range)

print(f"1. Çeyrek (Q1): {q1}")
print(f"Medyan (Q2): {q2}")
print(f"3. Çeyrek (Q3): {q3}")
print(f"IQR: {iqr}")
