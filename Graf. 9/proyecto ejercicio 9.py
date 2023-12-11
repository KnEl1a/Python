import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter  # Importa FuncFormatter

# Lee los datos desde el archivo CSV
#archivo = 'DatosPunto 9.csv' los rehago porque estaban mal, no hay que poner coma lal principio, te los bajas del mercosur y de ahi directamente los organizas con excel, luego de eso los limpias
#archivo = 'Fob exp pto 9.csv'
archivo = 'Var exp pto 9.csv'
#datos = pd.read_csv(archivo, usecols=['Anios','ArgExp','BraExp','ParExp','UrugExp']) 
datos = pd.read_csv(archivo, usecols=['Anios','ArgExpVar','BraExpVar','ParExpVar','UrugExpVar']) 
df = pd.DataFrame(datos, columns=['Anios','ArgExpVar','BraExpVar','ParExpVar','UrugExpVar']) # no reconoce la ñ y lo que son las tildes de nuestro 

# Definir una función para formatear los valores del eje x (en este caso, para eliminar los puntos flotantes)
#def format_years(x, pos):
 #   return int(x)

#def format_y_plain(x, pos):
 #   return f'{x/1000000:.0f}'  # Mostrar el número completo sin notación científica

# Crea el gráfico de barras
#plt.bar(df['Anios'], df['BraExp'], width=1/5, label = "Brasil", color='green')
#plt.bar(df['Anios'] + 0.2, df['ArgExp'], width=1/5, label = "Argentina", color='blue')
#plt.bar(df['Anios'] + 0.4, df['UrugExp'], width=1/5, label = "Uruguay", color='yellow')
#plt.bar(df['Anios'] + 0.4, df['ParExp'], width=1/5, label = "Paraguay", color='red')
plt.plot(df['Anios'], df['BraExpVar'], label = "Brasil", color='green', marker = '*', linestyle = "--")
plt.plot(df['Anios'], df['ArgExpVar'], label = "Argentina", color='blue', marker = '>', linestyle = "-.")
plt.plot(df['Anios'], df['UrugExpVar'],  label = "Uruguay", color='yellow', marker = '.', linestyle = "--")
plt.plot(df['Anios'], df['ParExpVar'], label = "Paraguay", color='red', marker = '<', linestyle = "-")

#activar leyenda
plt.legend()

#etiquetas en los ejes
plt.xlabel("Años") #etiqueta en eje x
#plt.ylabel("Total FOB US$ [Millones]")#etiqueta en eje y
plt.ylabel("Variación de las exportaciones")#etiqueta en eje y

# Configura el formateador personalizado para el eje x
#formatter = FuncFormatter(format_years)
#plt.gca().xaxis.set_major_formatter(formatter)

# Establece los límites del eje y para mostrar solo los primeros 3 números
# Configura el formateador personalizado para el eje y sin notación científica
#y_formatter = FuncFormatter(format_y_plain)
#plt.gca().yaxis.set_major_formatter(y_formatter)



plt.xticks(np.arange(2000, 2020, 1))
#plt.yticks(np.arange(210000, 2020, 3))

#activar cuadricula 
#plt.grid()

#activar marcas menores 
plt.minorticks_on()

#plt.title("Exportaciones de cada miembro del mercosur")
plt.grid(True, which='major', axis='both', color='black', linestyle='--', linewidth=0.5, alpha=0.3)
plt.show()
