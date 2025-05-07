import subprocess
from pathlib import Path

def transformacion():

    # Ruta del transformacion.py actual
    carpeta_actual = Path(__file__).parent
    # Ir a la carpeta "Limpieza"
    ruta_archivos = carpeta_actual / 'Limpieza'
    # Buscar todos los archivos .py (recursivamente)
    scripts = list(ruta_archivos.rglob('*.py'))
    # Ejecutar cada uno
    for script in scripts:
        print(f"Ejecutando: {script}")
        resultado = subprocess.run(['python', script], capture_output=True, text=True)
        
        print(f"Salida:{resultado.stdout}")
        
        if resultado.stderr:
            print(f"Error:\n{resultado.stderr}")
        
        print("-" * 150)

transformacion()