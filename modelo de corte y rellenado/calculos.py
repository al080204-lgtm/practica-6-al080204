import numpy as np


def calcular_volumenes(x, terreno, rasante):
d = [t - r for t, r in zip(terreno, rasante)]
vol_corte = 0
vol_relleno = 0
tabla = []


for i in range(len(x) - 1):
L = x[i+1] - x[i]
d1, d2 = d[i], d[i+1]


if d1 >= 0 and d2 >= 0:
A = L * (d1 + d2) / 2
vol_corte += A
tabla.append((i, "Corte", A))


elif d1 <= 0 and d2 <= 0:
A = L * (abs(d1) + abs(d2)) / 2
vol_relleno += A
tabla.append((i, "Relleno", A))


else:
t = abs(d1) / (abs(d1) + abs(d2))
L1 = t * L
L2 = (1 - t) * L


if d1 > 0:
A1 = L1 * (d1 + 0) / 2
A2 = L2 * (0 + abs(d2)) / 2
vol_corte += A1
vol_relleno += A2
else:
A1 = L1 * (abs(d1) + 0) / 2
A2 = L2 * (0 + d2) / 2
vol_relleno += A1
vol_corte += A2


tabla.append((i, "Transición", A1 + A2))


return vol_corte, vol_relleno, tabla
```python
def calcular_corte_relleno(elevaciones, rasante):
total_corte = 0
total_relleno = 0
detalles = []


for i in range(len(elevaciones)):
terreno = elevaciones[i][0]
diseno = rasante[i]


diferencia = terreno - diseno


if diferencia > 0:
corte = diferencia
relleno = 0
total_corte += corte
else:
corte = 0
relleno = abs(diferencia)
total_relleno += relleno


detalles.append((i, terreno, diseno, corte, relleno))


return total_corte, total_relleno, detalles