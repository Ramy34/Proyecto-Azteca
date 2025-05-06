# Se realiza la transformación y limpieza de los datos historicos (1995-2000) de la Liga Española

# Importamos pandas para leer el archivo csv
import pandas as pd
import glob
import os
import re

# Nombre del archivo limpio
archivo_salida = 'Silver\LigaEsp_historico_limpio.csv'

# Ruta de la carpeta con los CSV
carpeta = 'Bronze\España\Primera Division\Tipo 2'

# Buscar todos los CSV
archivos_csv = glob.glob(os.path.join(carpeta, '*.csv'))

# Lista para guardar los DataFrames
dfs = []

# Leer cada archivo y agregarle la columna 'archivo_origen'
for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    nombre_archivo = os.path.basename(archivo)  # solo el nombre, sin la ruta
    # Extraer XXXX y YYYY con regex (desde SP-XXXX_YYYY.csv)
    match = re.match(r'SP-(\d+)_(\d+)', nombre_archivo)
    if match:
        nuevo_valor = f'{match.group(1)}/{match.group(2)}'
    else:
        nuevo_valor = 'formato_desconocido'
    df.insert(loc=0, column='Temporada', value=nuevo_valor)
    dfs.append(df)
# Combinar todos
df_combinado = pd.concat(dfs, ignore_index=True)

# Seleccionar columnas clave
columnas_usar = ['Temporada','Date','HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR']
df_combinado = df_combinado[columnas_usar]

# Renombrar columnas para más claridad
df_combinado.columns = ['Temporada','Fecha', 'Equipo Local', 'Equipo Visitante', 'Goles Local', 'Goles Visitante', 'Resultado', 'Goles Medio Tiempo Local','Goles Medio Tiempo Visitante', 'Resultado Medio Tiempo']

# Convertir fechas correctamente
df_combinado['Fecha'] = pd.to_datetime(df_combinado['Fecha'], dayfirst=True, errors='coerce')
df_combinado = df_combinado.dropna(subset=['Fecha'])

df_combinado.insert(loc=0, column='País', value='España')
df_combinado.insert(loc=1, column='Liga', value='LaLiga')

# Agregar columnas extra (opcional)
def puntos(resultado):
    if resultado == 'H':
        return 3  # Gana local
    elif resultado == 'A':
        return 0  # Pierde local
    elif resultado == 'D':
        return 1  # Empate
    return None

df_combinado['Puntos_Local'] = df_combinado['Resultado'].apply(puntos)
df_combinado['Puntos_Visitante'] = df_combinado['Puntos_Local'].apply(lambda x: 1 if x == 1 else 3 - x if x in [0, 3] else None)

# Abrimos el archivo historico
df_historico = pd.read_csv(archivo_salida)

#Juntamos ambos archivos en uno solo
df_final = pd.concat([df_historico, df_combinado], ignore_index=True)

# Exportar archivo limpio
df_final.to_csv(archivo_salida, index=False, encoding='utf-8-sig')

print(df_final)

print(f"\nArchivo limpio y listo para Power BI: {archivo_salida}")