# Zaman serisi veri seti yükleme
data_time = pd.read_csv('timeseries_data.csv', parse_dates=['Date'], index_col='Date')

# Zaman serisi verisinin görselleştirilmesi
data_time['Value'].plot(figsize=(10, 6))
plt.title('Zaman Serisi Verisi')
plt.show()

# Rolling mean hesaplama (3 günlük hareketli ortalama)
data_time['Rolling Mean'] = data_time['Value'].rolling(window=3).mean()
data_time[['Value', 'Rolling Mean']].plot(figsize=(10, 6))
plt.title('Zaman Serisi ve Hareketli Ortalama')
plt.show()
