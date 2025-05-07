# Proyecto Azteca
## _Estadisticas del Futbol Mundial_

El proyecto Azteca tiene la finalidad de aprender algunas bases de la Ingeniería de Datos
### Caracteristicas Actuales
- Extracción: Utilizamos la base de datos de https://www.football-data.co.uk/, de momento esa parte se realiza de manera manual, queda pendiente automatizarla. Los archivos se almacenan en la carpeta _Bronze_ en la carpeta de su país
- Transformación: Se utiliza Python para la limpieza y transformación de los datos, el resultado del proceso se almacena en la carpeta _Silver_
-- México: Limpieza/Mexico/Trans_Mex_Hist.py
-- España 1993-1995: Limpieza/España/Trans_Esp_1993_1995.py
-- España 1995-2001: Limpieza/España/Trans_Esp_1995_2001.py
- Carga: Se realiza el proceso de consolidar los archivos de la carpeta _Silver_ en un solo archivo csv llamado _Partidos_ en la carpeta _Gold_
- Con Power Bi (_Azteca.pbix_) se conecta al archivo csv de partidos para generar un reporte

### Caracteristicas Futuras
- Extracción: Ver la manera de automatizar el proceso, agregar más ligas
- Transformación: Mejorar el proceso
- Carga: Generar otro tipo de archivos para otro tipo de analisis
- 