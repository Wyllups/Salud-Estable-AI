# 📊 Datos de Ejemplo – SaludEstable AI

Esta carpeta contiene **archivos de ejemplo** utilizados por la aplicación **SaludEstable AI** para demostrar el análisis automatizado del riesgo financiero en entidades de salud colombianas.

---

## 🏥 ¿Qué son las EPS e IPS?

- **EPS (Entidades Promotoras de Salud)**:  
  Son instituciones encargadas de **afiliar a los ciudadanos al sistema de salud** y **administrar los recursos** destinados a la atención médica.  
  Ejemplos: Nueva EPS, Sanitas, Sura EPS, etc.

- **IPS (Instituciones Prestadoras de Salud)**:  
  Son los **hospitales, clínicas y centros médicos** que **brindan directamente los servicios de salud** a los pacientes.  
  Ejemplos: Hospital Universitario del Valle, Clínica Colsanitas, etc.

En conjunto, las EPS **gestionan los fondos** y las IPS **prestan los servicios**.

---

## 📄 Origen de los datos

Los datos incluidos en esta carpeta provienen de **fuentes públicas y datos simulados** con fines educativos y demostrativos.  
Entre las fuentes utilizadas están:

- 📘 **Superintendencia Nacional de Salud (Supersalud)** — reportes públicos de estados financieros y gestión de EPS/IPS.  
  [https://www.supersalud.gov.co](https://www.supersalud.gov.co)
- 📊 **Ministerio de Salud y Protección Social** — información estadística del sistema general de seguridad social en salud.  
  [https://www.minsalud.gov.co](https://www.minsalud.gov.co)
- 📁 **Datos simulados** generados por el autor para pruebas del modelo y demostraciones interactivas en Streamlit.

> ⚠️ **Importante:** Los archivos incluidos no representan información confidencial ni datos financieros reales de entidades específicas.  
> Su propósito es únicamente **mostrar el funcionamiento del algoritmo de análisis y visualización** de la aplicación.

---

## 📂 Archivos incluidos

| Archivo | Descripción |
|----------|--------------|
| `ejemplo_eps.xlsx` | Datos simulados de una EPS (Entidad Promotora de Salud) con cuentas contables comunes. |
| `ejemplo_ips.xlsx` | Datos simulados de una IPS (Institución Prestadora de Salud). |
| `demo_variado.csv` | Archivo mixto con columnas desordenadas para probar la detección automática de la app. |

---

## 🧾 Formato esperado de los archivos

Cada archivo debe contener, al menos, tres columnas principales:

| Columna | Descripción | Ejemplo |
|----------|--------------|----------|
| **Entidad** | Nombre de la EPS o IPS | “NUEVA EPS”, “CLÍNICA CENTRAL” |
| **Denominación** | Nombre de la cuenta contable | “Ingresos operacionales”, “Pasivos corrientes” |
| **Valor** | Monto numérico correspondiente | 125000000 |

---

## 👨‍💻 Autor y créditos

**Wilfredo Calderón Pérez**  
📍 Colombia  
📧 [wilfredocalderonperez@gmail.com](mailto:wilfredocalderonperez@gmail.com)

Proyecto: **SaludEstable AI – Inteligencia Financiera para un Sistema de Salud más Sostenible**

---

## ⚖️ Licencia

Estos datos son de **uso libre y educativo**, publicados bajo licencia **MIT**.  
Se permite su uso, copia y adaptación siempre que se mencione la fuente original del proyecto.

---
