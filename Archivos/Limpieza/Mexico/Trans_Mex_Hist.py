# Se realiza la transformación y limpieza de los datos historicos (2012-2025) de la liga MX

# Importamos pandas para leer el archivo csv
import pandas as pd
from pathlib import Path

#Variables globales
pais = "Mexico"
nombre_archivo_entrada = "MEX.csv"
nombre_archivo_salida = "LigaMX_historico_limpio.csv"

def rutaArchivos(tipo):
    # Ruta del archivo py actual
    carpeta_actual = Path(__file__).parent
    # Subir tres niveles para llegar a "Proyecto Azteca"
    carpeta_proyecto = carpeta_actual.parent.parent.parent
    if (tipo == "E"):
        # Ir a la carpeta destino: Proyecto Azteca/Bronze/Mexico
        ruta_final = carpeta_proyecto / "Bronze" / pais / nombre_archivo_entrada
    elif (tipo == "S"):
        # Ir a la carpeta destino: Proyecto Azteca/Silver
        ruta_final = carpeta_proyecto / "Silver" / nombre_archivo_salida
    # Mostrar la ruta como texto
    return str(ruta_final)

def Trans_Mex_Hist():
    #Inicio del Proceso
    print("Se comienza con el proceso de limpieza y transformación de la liga mexicana")
    # Nombre del archivo de entrada
    archivo_entrada = rutaArchivos("E")
    # Nombre del archivo de salida
    archivo_salida = rutaArchivos("S")
    # Leemos el archivo y la almacenamos en df
    df = pd.read_csv(archivo_entrada)
    # Seleccionar columnas clave
    columnas_usar = ['Country','League','Season','Date','Home', 'Away', 'HG', 'AG', 'Res']
    df = df[columnas_usar]

    # Renombrar columnas para más claridad
    df.columns = ['País', 'Liga', 'Temporada', 'Fecha', 'Equipo Local', 'Equipo Visitante', 'Goles Local', 'Goles Visitante', 'Resultado']

    # Convertir fechas correctamente
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['Fecha'])
    df['Fecha'] = df['Fecha'].dt.strftime('%Y-%m-%d')

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

Trans_Mex_Hist()