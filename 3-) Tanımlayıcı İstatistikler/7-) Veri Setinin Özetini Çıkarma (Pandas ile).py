import pandas as pd

veri = {'Yaş': [22, 25, 30, 35, 40, 45, 50, 55, 60, 65]}

df = pd.DataFrame(veri)
print(df.describe())  # Pandas ile hızlı özetleme
