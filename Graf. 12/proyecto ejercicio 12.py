import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('principales-paises punto 12.csv', delimiter=';')

data['% Participación'] = data['% Participación'].str.replace(',', '.').astype(float)

labels = data['Category']
sizes = data['% Participación']

plt.figure(figsize=(10, 8))
plt.pie(sizes, startangle=0)

plt.legend(labels, loc="center left", bbox_to_anchor=(1, 0.5))

#plt.title('Distribución de FOB US$ por Categoría')
#plt.title('Principales exportaciones del Mercosur: Distribución de FOB US$ por Categoría')

plt.show()
