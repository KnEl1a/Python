import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter  # Importa FuncFormatter

# Lee los datos desde el archivo CSV
archivo = 'PreciosInternacionalesCSV(chart 4).txt'
datos = pd.read_csv(archivo, usecols=['Anio','Soja','Maiz','Trigo','Arroz']) 
df = pd.DataFrame(datos, columns=['Anio','Soja','Maiz','Trigo','Arroz']) # no reconoce la ñ por lo que en lugar de "Año" va ...

# Definir una función para formatear los valores del eje x (en este caso, para eliminar los puntos flotantes)
def format_years(x, pos):
    return int(x)

def format_y_plain(x, pos):
    return f'{x/1:.0f}'  # Mostrar el número completo sin notación científica

# Crea el gráfico de barras
#plt.plot(df['Ano'], df['URY'], marker='*', label = "Uruguay",  linestyle='--')
#plt.plot(df['Ano'], df['BRA'], marker='+', label = "Brasil")

plt.plot(df['Anio'], df['Soja'], marker='*', label = "Soja", color = "green")
plt.plot(df['Anio'], df['Maiz'], marker='+', label = "Maiz", color = "purple")
plt.plot(df['Anio'], df['Trigo'], marker='.', label = "Trigo", color = "brown")
plt.plot(df['Anio'], df['Arroz'], marker='>', label = "Arroz", color = "black")

#activar leyenda
plt.legend()

#etiquetas en los ejes
plt.xlabel("Años") #etiqueta en eje x
plt.ylabel("Precios en dolares por tonelada")#etiqueta en eje y

# Configura el formateador personalizado para el eje x
formatter = FuncFormatter(format_years)
plt.gca().xaxis.set_major_formatter(formatter)

# Establece los límites del eje y para mostrar solo los primeros 3 números
# Configura el formateador personalizado para el eje y sin notación científica
y_formatter = FuncFormatter(format_y_plain)
plt.gca().yaxis.set_major_formatter(y_formatter)


plt.xticks(np.arange(2000, 2020, 1))
#plt.yticks(np.arange(210000, 2020, 3))

#activar cuadricula 
#plt.grid()

#activar marcas menores 
plt.minorticks_on()
#plt.title("Mercosur4 - Evolución de las exportaciones del Arroz a China") #titulo
plt.grid(True, which='major', axis='both', color='black', linestyle='--', linewidth=0.5, alpha=0.3)
plt.show()


