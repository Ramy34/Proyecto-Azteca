# Se realiza la unión de los archivos historicos y limpios

# Importamos pandas para leer el archivo csv
import pandas as pd
import glob
import os
import re

# Ruta de la carpeta con los CSV
carpeta = 'Silver'

# Nombre del archivo unido
archivo_salida = 'Gold\partidos.csv'

# Buscar todos los CSV
archivos_csv = glob.glob(os.path.join(carpeta, '*.csv'))

# Lista para guardar los DataFrames
dfs = []

# Leer y combinar todos
df_combinado = pd.concat([pd.read_csv(f) for f in archivos_csv], ignore_index=True)

# Exportar archivo limpio
df_combinado.to_csv(archivo_salida, index=False, encoding='utf-8-sig')

print(f"\nArchivo limpio y listo para Power BI: {archivo_salida}")