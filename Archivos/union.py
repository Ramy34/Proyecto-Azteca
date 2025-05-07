# Se realiza la unión de los archivos historicos y limpios

# Importamos pandas para leer el archivo csv
import pandas as pd
from pathlib import Path
import glob
import os
import re

# Ruta del archivo .py actual
carpeta_actual = Path(__file__).parent
# Subir a la raíz del proyecto
carpeta_proyecto = carpeta_actual.parent
# Ruta de la carpeta con los CSV
carpeta_silver = carpeta_proyecto / 'Silver'
# Nombre del archivo unido
archivo_salida = carpeta_proyecto / 'Gold\partidos.csv'

# Buscar todos los CSV
archivos_csv = glob.glob(os.path.join(carpeta_silver, '*.csv'))

# Lista para guardar los DataFrames
dfs = []

# Leer y combinar todos
df_combinado = pd.concat([pd.read_csv(f) for f in archivos_csv], ignore_index=True)

# Exportar archivo limpio
df_combinado.to_csv(archivo_salida, index=False, encoding='utf-8-sig')

print(f"\nArchivo limpio y listo para Power BI: {archivo_salida}")