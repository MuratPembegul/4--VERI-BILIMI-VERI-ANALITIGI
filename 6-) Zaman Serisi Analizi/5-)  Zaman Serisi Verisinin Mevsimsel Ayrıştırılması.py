from statsmodels.tsa.seasonal import seasonal_decompose

decomposition = seasonal_decompose(df["Değer"], model="additive", period=12)

# Grafikleri çiz
plt.figure(figsize=(10,8))
plt.subplot(411)
plt.plot(df["Değer"], label="Orijinal")
plt.legend()

plt.subplot(412)
plt.plot(decomposition.trend, label="Trend")
plt.legend()

plt.subplot(413)
plt.plot(decomposition.seasonal, label="Mevsimsellik")
plt.legend()

plt.subplot(414)
plt.plot(decomposition.resid, label="Rastgele Bileşen")
plt.legend()

plt.show()
