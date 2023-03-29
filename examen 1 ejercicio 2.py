import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Definir una función para ajustar la función gaussiana con diferentes valores iniciales
def gaussian(x, amp, cen, wid):
    return amp * np.exp(-(x - cen) ** 2 / wid)

def fit_gaussian(xdata, p0):
    try:
        popt, pcov = curve_fit(gaussian, xdata, np.zeros_like(xdata) + 1, p0=p0)
    except:
        popt = [0, 0, 0]
    return popt

# Lee el archivo Excel desde la carpeta de descargas
df = pd.read_excel(r"C:\Users\feroc\OneDrive\Documents\examen-1-programacion\excel\excel.xlsx")

# Extraer las columnas B y C como arreglos NumPy
xdata_b = np.array(df['estatura'])
xdata_c = np.array(df['talla'])

# Calcula la media y la desviación estándar de la columna B
mean_b = np.mean(df['estatura'])
std_b = np.std(df['estatura'])

# Calcula la media y la desviación estándar de la columna C
mean_c = np.mean(df['talla'])
std_c = np.std(df['talla'])

# Imprime los resultados
print('Media de estatura:', mean_b)
print('Desviación estándar de estatura:', std_b)
print('Media de talla:', mean_c)
print('Desviación estándar de talla:', std_c)


# Definir valores iniciales para los parámetros de ajuste
p0_range = np.linspace(0.1, 10, 100)
p0_b = [1, mean_b, std_b/2]
p0_c = [1, mean_c, std_c/2]
for p in p0_range:
    p0_b[0] = p
    p0_c[0] = p
    popt_b = fit_gaussian(xdata_b, p0_b)
    popt_c = fit_gaussian(xdata_c, p0_c)
    if popt_b[0] != 0 and popt_c[0] != 0:
        break

# Ajustar las funciones gaussianas a los datos
#popt_b, pcov_b = curve_fit(gaussian, xdata_b, np.zeros_like(xdata_b) + 1, p0=p0_b)
#popt_c, pcov_c = curve_fit(gaussian, xdata_c, np.zeros_like(xdata_c) + 1, p0=p0_c)

# Generar datos para graficar las funciones gaussianas
x_plot_b = np.linspace(np.min(xdata_b), np.max(xdata_b), 100)
y_plot_b = gaussian(x_plot_b, *popt_b)
x_plot_c = np.linspace(np.min(xdata_c), np.max(xdata_c), 100)
y_plot_c = gaussian(x_plot_c, *popt_c)

# Graficar los datos y las funciones gaussianas ajustadas
#plt.plot(xdata_b, np.zeros_like(xdata_b), 'bo', label='Columna B')
plt.plot(x_plot_b, y_plot_b, 'b--', label='Ajuste gaussiano de la columna B')
#plt.plot(xdata_c, np.zeros_like(xdata_c), 'ro', label='Columna C')
plt.plot(x_plot_c, y_plot_c, 'r--', label='Ajuste gaussiano de la columna C')
plt.legend()
plt.show()