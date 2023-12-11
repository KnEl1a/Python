import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter  # Importa FuncFormatter

# Lee los datos desde el archivo CSV
archivo = 'DatosPunto10.csv'
datos = pd.read_csv(archivo, usecols=['Anos','Exportaciones','Importaciones','Balanza']) 
df = pd.DataFrame(datos, columns=['Anos','Exportaciones','Importaciones','Balanza']) # no reconoce la ñ y lo que son las tildes de nuestro 

# Definir una función para formatear los valores del eje x (en este caso, para eliminar los puntos flotantes)
def format_years(x, pos):
    return int(x)

def format_y_plain(x, pos):
    return f'{x/1000000000:.0f}'  # Mostrar el número completo sin notación científica

# Crea el gráfico de barras
plt.bar(df['Anos'], df['Exportaciones'], width=1/5, label = "Exportaciones")
plt.bar(df['Anos'] + 0.2, df['Importaciones'], width=1/5, label = "Importaciones")
plt.bar(df['Anos'] + 0.4, df['Balanza'], width=1/5, label = "Balanza")

#activar leyenda
plt.legend()

#etiquetas en los ejes
plt.xlabel("Años") #etiqueta en eje x
plt.ylabel("Total FOB US$ [Mil Millones]")#etiqueta en eje y

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

#plt.title("Segun la FAO(1961-2019): Área cosechada, rendimiento y producción en China del Arroz")
plt.show()
