# Archivo main, desde aquí se ejecuta todo el proceso
import subprocess

def main():
    print("El proyecto azteca consta de varias partes")
    print("1) Se realiza el proceso de extracción")
    resultado = subprocess.run(['python', 'Archivos/extraccion.py'], capture_output=True, text=True)
    print('Salida:', resultado.stdout)
    print("2) Se realiza el proceso de limpiado y transformación de los datos")
    resultado = subprocess.run(['python', 'Archivos/transformacion.py'], capture_output=True, text=True)
    print('Salida:', resultado.stdout)
    print("3) Se realiza el proceso unión de los archivos historicos de cada liga")
    resultado = subprocess.run(['python', 'Archivos/union.py'], capture_output=True, text=True)
    print('Salida:', resultado.stdout)

main()