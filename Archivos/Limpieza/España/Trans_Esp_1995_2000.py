# Se realiza la transformación y limpieza de los datos historicos (1995-2000) de la Liga Española

# Importamos pandas para leer el archivo csv
import pandas as pd
import glob
import os
import re
from pathlib import Path

#Variables globales
pais = "España"
ruta_entrada = "Bronze//" + pais + "/Primera Division/Tipo 2"
nombre_archivo_salida = "LigaEsp_historico_limpio.csv"

def rutaArchivos(tipo):
    # Ruta del archivo py actual
    carpeta_actual = Path(__file__).parent
    # Subir tres niveles para llegar a "Proyecto Azteca"
    carpeta_proyecto = carpeta_actual.parent.parent.parent
    if (tipo == "E"):
        # Ir a la carpeta destino: Proyecto Azteca/Bronze/España/Primera Division/Tipo 1
        ruta_final = carpeta_proyecto / ruta_entrada
    elif (tipo == "S"):
        # Ir a la carpeta destino: Proyecto Azteca/Silver/
        ruta_final = carpeta_proyecto / "Silver" / nombre_archivo_salida
    # Mostrar la ruta como texto
    return str(ruta_final)

def Trans_Esp_1995_2000():
    #Inicio del Proceso
    print("Se comienza con el proceso de limpieza y transformación de la liga española en el periodo de 1995 a 2001")
    # Nombre del archivo de entrada
    ruta_entrada = rutaArchivos("E")
    # Nombre del archivo de salida
    archivo_salida = rutaArchivos("S")

    # Buscar todos los CSV
    archivos_csv = glob.glob(os.path.join(ruta_entrada, '*.csv'))

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

    df_combinado['Puntos Local'] = df_combinado['Resultado'].apply(puntos)
    df_combinado['Puntos Visitante'] = df_combinado['Puntos Local'].apply(lambda x: 1 if x == 1 else 3 - x if x in [0, 3] else None)

    # Abrimos el archivo historico
    df_historico = pd.read_csv(archivo_salida)

    #Juntamos ambos archivos en uno solo
    df_final = pd.concat([df_historico, df_combinado], ignore_index=True)

    # Exportar archivo limpio
    df_final.to_csv(archivo_salida, index=False, encoding='utf-8-sig')

    print(f"\nArchivo limpio y listo para realizar la unión: {archivo_salida}")

Trans_Esp_1995_2000()