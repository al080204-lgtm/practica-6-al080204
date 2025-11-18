# practica-6-al080204
# Modelo de Corte y Relleno para Carreteras


## 🎯 Objetivo
Este proyecto tiene como objetivo modelar el cálculo de **volúmenes de corte y relleno** a lo largo de un perfil longitudinal de carretera, utilizando Python y una interfaz gráfica desarrollada con Tkinter.


Los estudiantes serán capaces de:
- Comprender el proceso de modelado de un problema real de Ingeniería Civil.
- Utilizar listas y matrices para representar datos topográficos.
- Crear funciones modulares para analizar, diseñar y probar soluciones.
- Graficar perfiles longitudinales del terreno y la rasante.
- Integrar una GUI para facilitar el uso del modelo.


---


## 📚 Marco Teórico
En un proyecto de construcción de carreteras, es necesario comparar el perfil del **terreno natural** con la **rasante de diseño**. Esta comparación permite obtener los volúmenes aproximados de:


- **Corte:** Cuando el terreno está por encima de la rasante.
- **Relleno:** Cuando el terreno está por debajo de la rasante.


El cálculo básico por estación es:


\[
\Delta h = Elevación_{terreno} - Elevación_{rasante}
\]


- Si \( \Delta h > 0 \), existe **corte**.
- Si \( \Delta h < 0 \), existe **relleno**.


Los valores por estación se suman para obtener los volúmenes totales.


---


## 🧱 Código organizado
El proyecto se divide en módulos:


### `src/datos.py`
Almacena la matriz de elevaciones.


### `src/calculos.py`
Realiza el cálculo de corte y relleno.


### `src/graficas.py`
Genera el perfil longitudinal.


### `src/main.py`
Ejecuta el modelo en consola.


### `interfaz/gui.py`
Interfaz gráfica completa con cálculo y gráficas.

