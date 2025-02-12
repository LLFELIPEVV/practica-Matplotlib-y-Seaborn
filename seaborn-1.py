import seaborn as sns
import matplotlib.pyplot as plt
# import pandas as pd
import numpy as np

# Configuracion inicial
sns.set_theme(style="whitegrid")  # Estilo con cuadricula
sns.set_palette("husl")  # Paleta de colores

# Cargando datos
# Seaborn funciona muy bien con DataFrames de Pandas.
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

# Grafico de dispersion (scatter plot)
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="time")
plt.show()

# Grafico de lineas (line plot)
# Para series temporales o tendencias.
sns.lineplot(x="total_bill", y="tip", data=tips, hue="time")
plt.show()

# Histograma (histogram)
# Para distribuciones de una variable.
# kde = kernel density estimation. kde=True añade una curva de densidad
sns.histplot(tips["total_bill"], kde=True)
plt.show()

# Grafico de barras (bar plot)
# Para comparar categorias.
sns.barplot(x="day", y="total_bill", data=tips, hue="sex")
plt.show()

# Bloxpot
# Para ver distribuciones y outliners.
sns.boxplot(x="day", y="total_bill", data=tips, hue="sex")
plt.show()

# Heatmap (mapa de calor)
# Para matrices de correlacion o datos tabulares.
numeric_tips = tips.select_dtypes(include=[np.number])
corr = numeric_tips.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

# Grafico avanzados
# Pairplot
# Para visualizar relaciones entre múltiples variables.
sns.pairplot(iris, hue="species")
plt.show()

# FacetGrid
# Para crear múltiples gráficos basados en categorías.
g = sns.FacetGrid(tips, col="time", row="sex")
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()

# Distribucion conjunta (jointplot)
# Para ver la relación y distribuciones de dos variables.
sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
plt.show()

# Grafico de violin (violinplto)
# Combina boxplot y distribución.
sns.violinplot(x="day", y="total_bill", data=tips, hue="sex")
plt.show()

# Documentacion oficial
# Aplica el tema por defecto.
sns.set_theme()

# Carga un Dataset de ejemplo
tips = sns.load_dataset("tips")

# Crea la visualizacion
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size"
)

plt.show()

# La función relplot()se llama así porque está diseñada para visualizar muchas relaciones estadísticas diferentes
dots = sns.load_dataset("dots")
sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate", col="align",
    hue="choice", size="coherence", style="choice",
    facet_kws=dict(sharex=False)
)

plt.show()

# Estimacion estadistica
# Muchas funciones de Seaborn realizarán automáticamente la estimación estadística necesaria para responder a estas preguntas.
fmri = sns.load_dataset("fmri")
sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", col="region",
    hue="event", style="event",
)

plt.show()

# Es posible mejorar un diagrama de dispersión al incluir un modelo de regresión lineal (y su incertidumbre) utilizando lmplot().
sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")

plt.show()

# La función Seaborn displot()admite varios enfoques para visualizar distribuciones.
sns.displot(data=tips, x="total_bill", col="time", kde=True)

plt.show()

# Seaborn también intenta promover técnicas potentes pero menos conocidas, como calcular y trazar la función de distribución acumulativa empírica de los datos.
sns.displot(data=tips, kind="ecdf", x="total_bill",
            col="time", hue="smoker", rug=True)

plt.show()

# Se puede acceder a los gráficos especializados orientados a la visualización de datos categóricos a traves de catplot().
sns.catplot(data=tips, kind="swarm", x="day", y="total_bill", hue="smoker")

plt.show()

# Como alternativa, puede utilizar la estimación de densidad del kernel para representar la distribución subyacente de la que se extraen los puntos.
sns.catplot(data=tips, kind="violin", x="day", y="total_bill", hue="smoker",
            split=True)

plt.show()
