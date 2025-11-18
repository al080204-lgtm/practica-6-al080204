Proyecto: #practica-6-al020480
# Modelo de Corte y Relleno para Carreteras
🎯 Objetivo

Este apartado describe, de forma clara y estructurada, el propósito del modelo desarrollado para calcular volúmenes de corte y relleno a lo largo del perfil longitudinal de una carretera. El sistema combina procesamiento numérico, estructuras de datos, visualización gráfica y una interfaz amigable, permitiendo comprender y aplicar conceptos fundamentales de la Ingeniería Civil.

Los estudiantes serán capaces de:

Comprender cómo se modela un problema real de movimiento de tierras.

Representar información topográfica usando listas y matrices.

Implementar funciones modulares para análisis, diseño y verificación.

Generar gráficos que comparan el perfil del terreno con la rasante de diseño.

Usar una GUI hecha en Tkinter para interactuar fácilmente con el modelo.

📚 Marco Teórico

En el diseño geométrico de carreteras, se compara el perfil del terreno natural con la rasante de diseño para determinar cuánto material debe excavarse (corte) o rellenarse (terraplenes). Esta comparación se realiza estación por estación a lo largo del eje del proyecto.

La diferencia vertical entre el terreno y la rasante se define como:

Δh = Elevación_terreno – Elevación_rasante

Interpretación:

Δh > 0 → Corte: el terreno está más alto que la rasante, por lo que se debe excavar.

Δh < 0 → Relleno: la rasante está por encima del terreno, por lo que se debe aportar material.

Al calcular esta diferencia en todas las estaciones y aplicar métodos de integración como el método del trapecio, se obtienen las áreas y volúmenes aproximados de corte y relleno. Estos valores son esenciales para estimar costos y planificar la ejecución de obra.
