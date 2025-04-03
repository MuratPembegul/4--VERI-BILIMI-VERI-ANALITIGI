from statsmodels.tsa.arima.model import ARIMA

# Modeli tanımla ve eğit
model = ARIMA(df["Değer"], order=(2,1,2))  # (p,d,q) parametreleri
model_fit = model.fit()

# Tahmin yap
future_steps = 10
forecast = model_fit.forecast(steps=future_steps)
print("Gelecek Tahminleri:\n", forecast)
