import matplotlib.pyplot as plt

etiketler = ["Elma", "Armut", "Muz", "Üzüm"]
degerler = [30, 15, 45, 10]

plt.pie(degerler, labels=etiketler, autopct='%1.1f%%', colors=['red', 'yellow', 'green', 'purple'])
plt.title("Pasta Grafiği")
plt.show()
