from statsmodels.tsa.stattools import adfuller

test_result = adfuller(df["Değer"])
print("ADF Test İstatistiği:", test_result[0])
print("p-değeri:", test_result[1])
if test_result[1] < 0.05:
    print("Zaman serisi durağandır (H0 reddedildi).")
else:
    print("Zaman serisi durağan değildir (H0 kabul edildi).")
