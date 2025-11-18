from interfaz.gui import iniciar_interfaz


if __name__ == "__main__":
iniciar_interfaz()
```python
from datos import elevaciones
from calculos import calcular_corte_relleno
from graficas import graficar


print("Modelo de Corte y Relleno")
rasante = list(map(float, input("Ingrese la rasante separada por comas: ").split(",")))


corte, relleno, detalles = calcular_corte_relleno(elevaciones, rasante)
print("Total de corte:", corte)
print("Total de relleno:", relleno)