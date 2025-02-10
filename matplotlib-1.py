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

# Marcadores
# Se puede utilizar la notacion de cadena de acceso directo para especificar los marcadores.
# Se pueden usar los siguientes marcadores:
# 'o' - Círculo
# '*' - Estrella
# '.' - Punto
# ',' - Punto pequeño
# 'x' - X
# '+' - Cruz
# 'P' - Plus
# 's' - Cuadrado
# 'D' - Diamante
# 'p' - Pentágono
# 'X' - X rotado
# 'h' - Hexágono 1
# 'H' - Hexágono 2
# 'v' - Triángulo hacia abajo
# '^' - Triángulo hacia arriba
# '<' - Triángulo hacia la izquierda
# '>' - Triángulo hacia la derecha
# '1' - Triángulo hacia arriba y hacia la derecha
# '2' - Triángulo hacia arriba y hacia la izquierda
# '3' - Triángulo hacia abajo y hacia la derecha
# '4' - Triángulo hacia abajo y hacia la izquierda
# '|' - Línea vertical hacia arriba
# '_' - Línea horizontal hacia la izquierda
print()
print("Marcadores")

# Marcando cada punto con un circulo
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o')
plt.show()

# Marcando cada punto con una estrella
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='*')
plt.show()

# Cadenas de formato fmt
# Se escribe con la sintaxis marker|line|color
# Se puede especificar los colores de los marcadores y de las lineas.
# Se puede usar cualquier combinacion de caracteres para especificar el color.
# Se puede usar un solo caracter para especificar el color.
# Se puede usar un solo caracter para especificar el color de las lineas.
# Marcando cada punto con un circulo
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()

# Tamaño del marcador
# Se puede usar el parametro markersize o la version mas corta ms para establecer el tamaño de los marcadores
# Estableciendo el tamaño de los marcadores a 20
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', ms=20)
plt.show()

# Color del marcador
# Se puede usar el parametro markeredgecolor o la version mas corta mec para establecer el color de los marcadores.
# Se pueden usar colores hexadecimales.
# Estableciendo el color del borde de los marcadores a rojo
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', mec='r')
plt.show()

# Se puede usar el parametro markerfacecolor o la version mas corta mfc para establecer el color de los marcadores
# Estableciendo el color de los marcadores a rojo
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', mfc='r')
plt.show()

# Linea de Matplotlib
print()
print("Linea de Matplotlib")

# Estilo de linea
# Se puede usar el parametro linestyle o la version mas corta ls para cambiar el estilo de la linea.
# Utilizando una linea de puntos.
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle='dotted')
plt.show()

# Utilizando una linea discontinua
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle='dashed')
plt.show()

# Sintaxis mas corta
# linestyle se puede escribir ls.
# dotted se puede escribir :.
# dashed se puede escribir --.
# Usando la sintaxis mas corta para trazar una linea de puntos
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls=':')
plt.show()

# Color de linea
# Se puede utilizar el argumento color o la version mas corta c para establecer el color de la linea.
# Estableciendo el color de la linea en rojo
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color='r')
plt.show()

# Ancho de linea
# Se puede usar el parametro linewidth o la version mas corta lw para cambiar el ancho de la linea.
# Estableciendo el ancho de la linea a 20.5
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth='20.5')
plt.show()

# Lineas Multiples
# Se pueden trazar varias lineas agregando multiples pares de argumentos x y en la funcion plot().
# Dibujando 2 lineas
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

# Etiquetas y titulos de Matplotlib
print()
print("Etiquetas y titulos de Matplotlib")

# Creando etiquetas para un grafico
# Se puede usar la funcion xlabel() y ylabel() para establecer etiquetas para los ejes x y y.
# Añadiendo etiquetas a los ejes x e y
x = np.array([80, 85, 90, 95, 100])
y = np.array([240, 250, 260, 270, 280])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

# Creando un titulo para un grafico
# Se puede usar la funcion title() para establecer un titulo para el grafico.
# Añadiendo un titulo al grafico
x = np.array([80, 85, 90, 95, 100])
y = np.array([240, 250, 260, 270, 280])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

# Establecer propiedades de fuente para titulos y etiquetas
# Se puede usar el parametro fontdict para establecer propiedades de fuente para el titulo y las etiquetas.
# Estableciendo propiedades de fuente para titulos y etiquetas
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

plt.title("Sports Watch Data", fontdict=font1)
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)

plt.plot(x, y)

plt.show()

# Posicionar el titulo
# Se puede usar el parametro loc para posicionar el titulo.
# Estableciendo el titulo en la izquierda
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc='left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()

# Cuadricula Matplotlib
# Se puede usar la funcion grid() para establecer cuadricula en el grafico.
print()
print("Cuadricula Matplotlib")

# Añadiendo lineas de cuadricula al grafico
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.grid()

plt.show()

# Especificar que lineas de cuadricula se van a mostrar
# Se puede utilizar el parametro axis para especificar que lineas de cuadricula mostrar.
# Mostrando las lineas de cuadricula solo para el eje x.
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.grid(axis='x')

plt.show()

# Mostrandos las lineas de cuadricula solo para el eje y.
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.grid(axis='y')

plt.show()

# Establecer propiedades de linea para la cuadricula
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.grid(color='green', linestyle='--', linewidth=0.5)

plt.show()

# Subtrama de Matplotlib
print()
print("Subtrama de Matplotlib")

# Mostrar graficos multiples
# Con la funcion subplot() se pueden dibujar multiples graficos en una figura.
# Plot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)

# Plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)

plt.show()

# Funcion subplot()
# La Funcion subplot() toma 3 argumentos que describen el diseño de la figura.
# El diseño esta organizado en filas y columnas, que estan representadas por el primer y segundo argumento.
# El tercer argumento representa el indice de la figura.
# Dibujando dos graficos en vertical
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)  # (filas, columnas, orden)
plt.plot(x, y)

# Plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x, y)

plt.show()

# Dibujando 6 graficos
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x, y)

plt.show()

# Titulo
# Se puede agregar un titulo a cada subtrama con la funcion title().
# Agregando un titulo a cada subtrama
# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("SALES")

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("INCOME")

plt.show()

# Super titulo
# Se puede agregar un titulo general a la figura con la funcion suptitle().
# Agregando un titulo general a la figura
# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("SALES")

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()
