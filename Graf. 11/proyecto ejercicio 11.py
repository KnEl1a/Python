import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('punto 11 exportaciones-2023.csv', delimiter=';')

data['FOB US$'] = data['FOB US$'].str.replace(',', '.').astype(float)

labels = data['Category']
sizes = data['FOB US$']

plt.figure(figsize=(8, 8))
plt.pie(sizes, autopct='%1.1f%%', startangle=0)

plt.legend(labels, loc="center left", bbox_to_anchor=(1, 0.5))

#plt.title('Distribución de FOB US$ por Categoría')
#plt.title('Principales exportaciones del Mercosur: Distribución de FOB US$ por Categoría')

plt.show()

