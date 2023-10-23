import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter  # Importa FuncFormatter

# Lee los datos desde el archivo CSV
archivo = 'datosReorganizadosFaostat_ejercicio_2_Arroz_copy.txt'
datos = pd.read_csv(archivo, usecols=['Ano','AreaCosechada','Produccion','Rendimiento']) 
df = pd.DataFrame(datos, columns=['Ano','AreaCosechada','Produccion','Rendimiento']) # no reconoce la ñ y lo que son las tildes de nuestro 

def millions(x, pos):
    'El número 1 se representa como 1M'
    return f'{x/1e6:.0f}M'

def k(x, pos):
    'El número 1 se representa como 1M'
    return f'{x/1000:.0f}k'

# Crea un gráfico de líneas con tres ejes Y
fig, ax1 = plt.subplots()

# Eje Y 1
ax1.set_xlabel('Años')
ax1.set_ylabel('ha', color='tab:blue')
ax1.plot(df['Ano'], df['AreaCosechada'], color='tab:blue', label='Área Cosechada', marker="<", linestyle = "--")
ax1.tick_params(axis='y', labelcolor='tab:blue')


# Eje Y 2
ax2 = ax1.twinx()
ax2.set_ylabel('toneladas', color='tab:red')
ax2.plot(df['Ano'], df['Produccion'], color='tab:red', label='Producción', marker=">", linestyle = "-.")
ax2.tick_params(axis='y', labelcolor='tab:red')


# Eje Y 3
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel('hg/ha', color='tab:purple')
ax3.plot(df['Ano'], df['Rendimiento'], color='tab:purple', label='Rendimiento', marker="*", linestyle = "-")
ax3.tick_params(axis='y', labelcolor='tab:purple')
#activar leyenda
ax1.legend(loc='upper left', bbox_to_anchor=(0.03, 1), handlelength=2)
ax2.legend(loc='upper left', bbox_to_anchor=(0.03, 0.90), handlelength=2)
ax3.legend(loc='upper left', bbox_to_anchor=(0.03, 0.85), handlelength=2)

#ax3.legend(loc='upper left')

# Configura el eje Y para mostrar los valores completos
ax1.yaxis.set_major_formatter(FuncFormatter(millions))
ax2.yaxis.set_major_formatter(FuncFormatter(millions))
ax3.yaxis.set_major_formatter(FuncFormatter(k))

# Especificar el formato de los ticks del eje X para mostrar los años cada 10 años
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False))

# Establecer los ticks del eje X manualmente cada 10 años
plt.xticks(np.arange(1961, 2020, 3))
#plt.yticks(np.arange(210000, 2020, 3))

#activar cuadricula 
plt.grid()

#activar marcas menores 
plt.minorticks_on()

plt.title("Segun la FAO(1961-2019): Área cosechada, rendimiento y producción en China del Maiz")
plt.show()

