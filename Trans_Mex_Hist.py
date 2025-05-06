# Se realiza la transformación y limpieza de los datos historicos (2012-2025) de la liga MX

# Importamos pandas para leer el archivo csv
import pandas as pd

# Nombre del archivo a leer
archivo_entrada = 'Bronze\Mexico\MEX.csv'

# Nombre del archivo limpio
archivo_salida = 'Silver\LigaMX_historico_limpio.csv'

# Leemos el archivo y la almacenamos en df
df = pd.read_csv(archivo_entrada)

# Seleccionar columnas clave
columnas_usar = ['Country','League','Season','Date','Home', 'Away', 'HG', 'AG', 'Res']
df = df[columnas_usar]

# Renombrar columnas para más claridad
df.columns = ['País', 'Liga', 'Temporada', 'Fecha', 'Equipo Local', 'Equipo Visitante', 'Goles Local', 'Goles Visitante', 'Resultado']

# 5. Convertir fechas correctamente
df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['Fecha'])

# Se agregan nuevas columnas
df['Goles Medio Tiempo Local'] = df['Goles Local']
df['Goles Medio Tiempo Visitante'] = df['Goles Visitante']
df['Resultado Medio Tiempo'] = df['Resultado']

# Agregar columnas extra (opcional)
def puntos(resultado):
    if resultado == 'H':
        return 3  # Gana local
    elif resultado == 'A':
        return 0  # Pierde local
    elif resultado == 'D':
        return 1  # Empate
    return None

df['Puntos Local'] = df['Resultado'].apply(puntos)
df['Puntos Visitante'] = df['Puntos Local'].apply(lambda x: 1 if x == 1 else 3 - x if x in [0, 3] else None)

# Exportar archivo limpio
df.to_csv(archivo_salida, index=False, encoding='utf-8-sig')

print(f"\nArchivo limpio y listo para realizar la unión: {archivo_salida}")