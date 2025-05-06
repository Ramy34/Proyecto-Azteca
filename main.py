# Archivo main, desde aquí se ejecuta todo el proceso
import subprocess

def main():
    print("El proyecto azteca conta de varias partes")
    print("1) Se realiza el proceso de limpiado y transformación de los datos")
    print("2) Se realiza la unión de los archivos historicos de cada liga")
    print("*********************************************************************************")
    print("Se comienza con el proceso de limpieza y transformación de la liga mexicana")
    resultado = subprocess.run(['python', 'Trans_Mex_Hist.py'], capture_output=True, text=True)
    print('Salida:', resultado.stdout)
    print("Se comienza con el proceso de limpieza y transformación de la liga española - Tipo 1")
    resultado = subprocess.run(['python', 'Trans_Mex_Hist.py'], capture_output=True, text=True)
    print('Salida:', resultado.stdout)
    print("Se comienza con el proceso de limpieza y transformación de la liga española - Tipo 2")
    resultado = subprocess.run(['python', 'Trans_Mex_Hist.py'], capture_output=True, text=True)
    print('Salida:', resultado.stdout)
    print("Se comienza con el proceso de unión de datos")
    resultado = subprocess.run(['python', 'Union.py'], capture_output=True, text=True)
    print('Salida:', resultado.stdout)
main()