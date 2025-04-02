import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

plt.plot(x, y, marker='o', linestyle='-', color='b', label="Çizgi Grafiği")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.title("Basit Çizgi Grafiği")
plt.legend()
plt.grid(True)
plt.show()
