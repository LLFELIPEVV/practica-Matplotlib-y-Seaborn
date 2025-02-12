import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
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


