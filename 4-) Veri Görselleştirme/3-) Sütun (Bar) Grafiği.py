import matplotlib.pyplot as plt

kategoriler = ["A", "B", "C", "D", "E"]
degerler = [5, 7, 3, 8, 9]

plt.bar(kategoriler, degerler, color='purple', alpha=0.6)
plt.xlabel("Kategoriler")
plt.ylabel("Değerler")
plt.title("Sütun Grafiği")
plt.show()
