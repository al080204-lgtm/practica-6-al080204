import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from src.datos_prueba import estaciones, terreno, rasante_ejemplo
from src.calculos import calcular_volumenes
from src.graficas import graficar_perfil


# GUI


def iniciar_interfaz():
def ejecutar():
try:
ras_in = entrada_rasante.get()
ras = [float(x) for x in ras_in.split(",")]
vol_corte, vol_relleno, tabla = calcular_volumenes(estaciones, terreno, ras)


salida = "RESULTADOS
"
salida += f"Volumen corte: {vol_corte:.2f} m³
"
salida += f"Volumen relleno: {vol_relleno:.2f} m³


"
salida += "Tabla:
"
for fila in tabla:
salida += str(fila) + "
"


texto.config(state="normal")
texto.delete("1.0", tk.END)
texto.insert(tk.END, salida)
texto.config(state="disabled")
except:
messagebox.showerror("Error", "Rasante inválida.")


def graficar():
ras_in = entrada_rasante.get()
ras = [float(x) for x in ras_in.split(",")]
graficar_perfil(estaciones, terreno, ras)


ventana = tk.Tk()
ventana.title("Corte y Relleno - Carreteras")


tk.Label(ventana, text="Rasante (coma separada)").pack()
entrada_rasante = tk.Entry(ventana, width=60)
entrada_rasante.pack(pady=5)
entrada_rasante.insert(0, ",".join([str(x) for x in rasante_ejemplo]))


tk.Button(ventana, text="Calcular", command=ejecutar).pack(pady=5)
tk.Button(ventana, text="Graficar", command=graficar).pack(pady=5)


texto = tk.Text(ventana, width=80, height=20)
texto.pack(pady=10)
texto.config(state="disabled")


ventana.mainloop()


if __name__ == "__main__":
iniciar_interfaz()