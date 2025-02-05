import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Matplotlib es una biblioteca de representacion grafica de bajo nivel de Python.
# Comprobando la version de Matplotlib
print(matplotlib.__version__)

# Pyplot es un submodulo de Matplotlib que proporciona una interfaz similar a MATLAB.
# Pyplot contiene la mayoria de las utilidades de Maplotlib.
# Dibujando una linea simple
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

# Trazado de Matplotlib
# La funcion plot() se utiliza para dibujar puntos en un diagrama.
# Por defecto, dibuja una linea de punto a punto.
# La funcion plot() necesita dos arrays, uno para los valores del eje x, y otro para los valores del eje y.
# Dibujando puntos en la posicion (1, 3) y (8, 10)
xpoints = np.array([1, 8])  # Valores en x
ypoints = np.array([3, 10])  # Valores en y

plt.plot(xpoints, ypoints)
plt.show()

# Trazando sin linea
# Para trazar solo los marcadores, se puede usar la notacion de cadena de acceso directo 'o'.
# Dibujando puntos en la posicion (1, 3) y (8, 10)
xpoints = np.array([1, 8])  # Valores en x
ypoints = np.array([3, 10])  # Valores en y

plt.plot(xpoints, ypoints, 'o')
plt.show()

# Puntos multiples
# Se pueden trazar tantos puntos como se desee, la unica condicion es que los arrays de x e y deben tener la misma longitud.
# Dibujando puntos en la posicion (1, 3), (2, 8), (6, 1) y (8, 10)
xpoints = np.array([1, 2, 6, 8])  # Valores en x
ypoints = np.array([3, 8, 1, 10])  # Valores en y

plt.plot(xpoints, ypoints)
plt.show()

# Puntos X predeterminados
# Si no se especifican los puntos en el eje x, se obtendran en una sucesion de 0 a infinito, aumentando en uno.
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()
