import pandas as pd
import matplotlib.pyplot as plt

import os

print("Directorio actual:", os.getcwd())

# Cargar el archivo de texto
archivo = "C:\\Users\\34664\\Documents\\fisica\\4º curso\\TFG\\plantilla_latex\\gráficas_simulacion\\1us_500uA_50nF_200kO.txt"

# Leer el archivo con pandas (salta la primera fila de cabecera si es necesario)
df = pd.read_csv(archivo, delim_whitespace=True)


# Verifica si las columnas son correctas
print(df.head())

# Crear la gráfica
plt.figure(figsize=(10, 6)) 
plt.plot(df['time'], df['V(n001)'], label='V(n001)', color = 'g', linewidth=1)
plt.plot(df['time'], df['V(n002)'], label='V(n002)', color = 'b', linewidth=1)
plt.plot(df['time'], df['V(n004)'], label='V(n004)', color = 'r', linewidth=1)

# Estética de la gráfica
plt.title('Voltajes en nodos vs Tiempo', fontsize=24)
plt.xlabel('Tiempo [s]', fontsize=20)
plt.ylabel('Voltaje [V]', fontsize=20)
# plt.legend(loc= 'center right',fontsize=18)
plt.legend(loc="upper right", bbox_to_anchor=(0.9, 0.9), fontsize=18)
plt.grid(True)
plt.tight_layout()
plt.show()