import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 9, 11, 14]

plt.plot(x, y, c="red")
plt.title("Wykres")

plt.savefig("wykres.png")
plt.show()
