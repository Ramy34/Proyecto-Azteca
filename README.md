# ⚽ Proyecto Azteca
## _Estadísticas del Fútbol Mundial_

---

### 🏷️ Badges

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)]
[![Power BI](https://img.shields.io/badge/PowerBI-Report-yellow?logo=powerbi)]
[![Estado](https://img.shields.io/badge/Estado-En%20Desarrollo-orange)]
[![Licencia](https://img.shields.io/badge/Licencia-MIT-green)]


📊 El **Proyecto Azteca** tiene como objetivo aprender y aplicar conceptos fundamentales de **Ingeniería de Datos** (Procesos ETL y Arquitectura Medallón) utilizando estadísticas de fútbol profesional.

---

## 🏗️ Arquitectura y Flujo de Datos

El proyecto sigue un diseño de capas de datos estructurado y es orquestado de forma automática desde el script principal `main.py`:

### 1. 🥉 Capa Bronze (Extracción) | `Archivos/extraccion.py`
- **Origen:** Archivos originales de la base de datos de Football-Data.co.uk.
- **Proceso:** Actualmente la descarga es manual (pendiente de automatizar en el script).
- **Almacenamiento:** Los archivos se guardan crudos en la carpeta `Bronze/`, organizados por país y división.

### 2. 🥈 Capa Silver (Transformación) | `Archivos/transformacion.py`
- **Proceso:** Un script dinámico que busca y ejecuta recursivamente todos los procesos de limpieza ubicados en la carpeta `Archivos/Limpieza/`.
- **Lógica aplicada:** Limpieza de datos, homologación de nombres de columnas, formateo de fechas y creación de nuevas métricas (como Puntos de Local y Visitante).
- **Scripts actuales:**
  - 🇲🇽 **México**: `Limpieza/Mexico/Trans_Mex_Hist.py`
  - 🇪🇸 **España 1993-1995**: `Limpieza/España/Trans_Esp_1993_1995.py`
  - 🇪🇸 **España 1995-2000**: `Limpieza/España/Trans_Esp_1995_2000.py`
- **Almacenamiento:** Archivos históricos estandarizados en la carpeta `Silver/`.

### 3. 🥇 Capa Gold (Carga y Unión) | `Archivos/union.py`
- **Proceso:** Lee de manera automatizada todos los archivos `.csv` generados en la capa Silver.
- **Almacenamiento:** Los concatena verticalmente y exporta un único archivo maestro llamado `partidos.csv` directamente en la carpeta `Gold/`.

### 4. 📈 Visualización (Power BI)
- Con **Power BI** se conecta el archivo final de la capa Gold (`Gold/partidos.csv`) para nutrir el reporte analítico interactivo: `_Azteca.pbix_`.

---

## 🚀 Cómo Ejecutar el Proyecto

Para correr el proceso (ETL) completo desde la terminal, simplemente debes ejecutar el archivo orquestador:

```bash
python main.py
```
*Este comando lanzará secuencialmente la Extracción (1), la Transformación dinámica de todas las ligas (2) y la Unión final de la información (3).*

---

## 🚀 Características Futuras

- 🔄 **Automatización de la extracción** y ampliación a otras ligas y temporadas
- 🧪 Mejora continua del proceso de transformación
- 🗃️ Generación de otros formatos para distintos tipos de análisis (parquet, SQL, etc.)
- 🧭 Expansión del dashboard de Power BI con más visualizaciones e insights

---

## 🛠️ Requisitos

- Python 3.x
- Librerías: `pandas`
- Power BI Desktop (para visualizar el archivo `.pbix`)
---

## 📬 Contacto

¿Preguntas o sugerencias? ¡Estoy abierto a feedback y colaboración!

---
