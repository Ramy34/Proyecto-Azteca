# Se realiza la transformación y limpieza de los datos historicos (1993-1995) de la Liga Española

# Importamos pandas para leer el archivo csv
import pandas as pd

# Nombre de los archivos a leer
archivo_entrada_1993_1994 = 'Bronze\España\Primera Division\Tipo 1\SP-1993_1994.csv'
archivo_entrada_1994_1995 = 'Bronze\España\Primera Division\Tipo 1\SP-1994_1995.csv'

# Nombre del archivo limpio
archivo_salida = 'Silver\LigaEsp_historico_limpio.csv'

# Leemos el archivo y la almacenamos en df
df_1993 = pd.read_csv(archivo_entrada_1993_1994)
df_1994 = pd.read_csv(archivo_entrada_1994_1995)

df_1993.insert(loc=0, column='Temporada', value="1993/1994")
df_1994.insert(loc=0, column='Temporada', value="1994/1995")


#Juntamos ambos archivos en uno solo
df = pd.concat([df_1993, df_1994], ignore_index=True)

# Seleccionar columnas clave
columnas_usar = ['Temporada','Date','HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']
df = df[columnas_usar]

# Renombrar columnas para más claridad
df.columns = ['Temporada','Fecha', 'Equipo Local', 'Equipo Visitante', 'Goles Local', 'Goles Visitante', 'Resultado']

# Convertir fechas correctamente
df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['Fecha'])

# Se agregan nuevas columnas
df['Goles Medio Tiempo Local'] = df['Goles Local']
df['Goles Medio Tiempo Visitante'] = df['Goles Visitante']
df['Resultado Medio Tiempo'] = df['Resultado']

df.insert(loc=0, column='País', value='España')
df.insert(loc=1, column='Liga', value='LaLiga')

# Agregar columnas extra (opcional)
def puntos(resultado):
    if resultado == 'H':
        return 3  # Gana local
    elif resultado == 'A':
        return 0  # Pierde local
    elif resultado == 'D':
        return 1  # Empate
    return None

df['Puntos_Local'] = df['Resultado'].apply(puntos)
df['Puntos_Visitante'] = df['Puntos_Local'].apply(lambda x: 1 if x == 1 else 3 - x if x in [0, 3] else None)

# Exportar archivo limpio
df.to_csv(archivo_salida, index=False, encoding='utf-8-sig')

print(df)

print(f"\nArchivo limpio y listo para Power BI: {archivo_salida}")