# ⚽ Proyecto Azteca
## _Estadísticas del Fútbol Mundial_

---

### 🏷️ Badges

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)]
[![Power BI](https://img.shields.io/badge/PowerBI-Report-yellow?logo=powerbi)]
[![Estado](https://img.shields.io/badge/Estado-En%20Desarrollo-orange)]
[![Licencia](https://img.shields.io/badge/Licencia-MIT-green)]


📊 El **Proyecto Azteca** tiene como objetivo aprender y aplicar conceptos fundamentales de **Ingeniería de Datos** utilizando estadísticas de fútbol profesional.

---

## 🔧 Características Actuales

### 1. 🗂️ Extracción
- Se utiliza la base de datos oficial de [Football-Data.co.uk](https://www.football-data.co.uk/)
- Actualmente se realiza **de forma manual** (pendiente de automatización)
- Los archivos extraídos se almacenan en la carpeta `_Bronze_`, organizados por país

### 2. 🧹 Transformación
- Se emplea **Python** para limpiar y transformar los datos
- Los archivos limpios se guardan en la carpeta `_Silver_`
  - 🇲🇽 **México**: `Limpieza/Mexico/Trans_Mex_Hist.py`
  - 🇪🇸 **España 1993-1995**: `Limpieza/España/Trans_Esp_1993_1995.py`
  - 🇪🇸 **España 1995-2001**: `Limpieza/España/Trans_Esp_1995_2001.py`

### 3. 📦 Carga
- Se consolidan todos los archivos `.csv` de la carpeta `_Silver_` en un solo archivo llamado `Partidos.csv` ubicado en la carpeta `_Gold_`

### 4. 📈 Visualización (Power BI)
- Con **Power BI** se conecta el archivo `Partidos.csv` para generar visualizaciones en el reporte: `_Azteca.pbix_`

---

## 🚀 Características Futuras

- 🔄 **Automatización de la extracción** y ampliación a otras ligas y temporadas
- 🧪 Mejora continua del proceso de transformación
- 🗃️ Generación de otros formatos para distintos tipos de análisis (parquet, SQL, etc.)
- 🧭 Expansión del dashboard de Power BI con más visualizaciones e insights

---

## 🛠️ Requisitos

- Python 3.x
- Pandas
- Power BI Desktop (para visualizar el archivo `.pbix`)

---

## 📁 Estructura del Proyecto
Proyecto Azteca/
├── Bronze/
│ └── [Países con archivos originales]
├── Silver/
│ └── [Archivos transformados por liga]
├── Gold/
│ └── Partidos.csv
├── Limpieza/
│ ├── Mexico/
│ └── España/
├── Archivos/
│ ├── extraccion.py
│ ├── transformacion.py
│ └── union.py
├── Azteca.pbix
└── README.md
---

## 📬 Contacto

¿Preguntas o sugerencias? ¡Estoy abierto a feedback y colaboración!

---
