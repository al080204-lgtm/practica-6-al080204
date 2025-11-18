import matplotlib.pyplot as plt


def graficar(elevaciones, rasante):
estaciones = list(range(len(elevaciones)))
terreno = [fila[0] for fila in elevaciones]


plt.plot(estaciones, terreno, label="Terreno")
plt.plot(estaciones, rasante, label="Rasante", linestyle="--")
plt.title("Perfil Longitudinal")
plt.xlabel("Estaciones")
plt.ylabel("Elevación (m)")
plt.legend()
plt.grid(True)
plt.show()