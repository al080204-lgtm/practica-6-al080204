from src.calculos import calcular_corte_relleno


def test_basico():
elev = [[10], [12], [8]]
ras = [9, 11, 10]
corte, relleno, _ = calcular_corte_relleno(elev, ras)
assert corte == 2
assert relleno == 2


print("Pruebas ejecutadas correctamente.")