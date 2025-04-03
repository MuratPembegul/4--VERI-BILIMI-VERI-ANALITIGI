import pandas as pd
import matplotlib.pyplot as plt

# Zaman serisi verisini oku
df = pd.read_csv("zaman_serisi.csv", parse_dates=["Tarih"], index_col="Tarih")

# Zaman serisini çiz
plt.figure(figsize=(10,5))
plt.plot(df, label="Zaman Serisi Verisi")
plt.xlabel("Tarih")
plt.ylabel("Değer")
plt.title("Zaman Serisi Grafiği")
plt.legend()
plt.show()
