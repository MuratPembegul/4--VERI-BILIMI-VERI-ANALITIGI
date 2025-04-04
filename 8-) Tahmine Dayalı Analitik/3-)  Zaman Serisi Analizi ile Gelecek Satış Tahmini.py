import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Örnek satış verisi
data = pd.DataFrame({
    'Ay': np.arange(1, 13),
    'Satış': [120, 150, 170, 200, 250, 270, 300, 350, 400, 450, 500, 550]
})

# Zaman serisi modelini oluşturma
model = ExponentialSmoothing(data['Satış'], trend='add', seasonal=None)
fit = model.fit()

# Gelecek 3 ayı tahmin etme
tahmin = fit.forecast(3)
print("Gelecek 3 ay tahmini:", tahmin.values)

# Görselleştirme
plt.plot(data['Ay'], data['Satış'], label="Gerçek Satışlar")
plt.plot(range(13, 16), tahmin, label="Tahmin Edilen Satışlar", linestyle='dashed', color='red')
plt.xlabel("Ay")
plt.ylabel("Satış")
plt.title("Zaman Serisi Analizi ile Satış Tahmini")
plt.legend()
plt.show()
