## SaludEstable AI

**SaludEstable AI** es una aplicación desarrollada con **Streamlit** para la **evaluación y predicción automatizada del riesgo financiero** en entidades de salud colombianas (**EPS / IPS**).  
Analiza archivos contables en formato Excel, detecta columnas automáticamente, calcula indicadores financieros clave y clasifica el nivel de riesgo de cada entidad mediante un modelo ponderado y normalizado por percentiles.

---

## Características principales

-  **Carga múltiple de archivos Excel** (`.xlsx`, `.xls`, `.csv`)
-  **Detección automática** de columnas relevantes (`Entidad`, `Denominación`, `Valor`)
-  **Cálculo inteligente de indicadores financieros:**
  - Liquidez Corriente  
  - Endeudamiento Total  
  - Margen Neto  
  - ROA (Rentabilidad sobre Activos)  
  - Rotación de Activos
-  **Normalización automática** de métricas mediante percentiles
-  **Evaluación global ponderada** de riesgo financiero
-  **Predicción de tendencia financiera** (Mejora, Estable o Riesgo)
-  **Visualización dinámica** con gráficos interactivos de Plotly
-  **Descarga de resultados completos** en Excel

---

## 📁 Estructura del proyecto

```
SaludEstable-AI/
│
├── app.py                     # Código principal de la aplicación Streamlit
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Documentación del proyecto
└── data/                      # (Opcional) Carpeta para archivos de ejemplo
```

---

## ⚙️ Instalación y ejecución local

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tuusuario/SaludEstable-AI.git
cd SaludEstable-AI
```

### 2️⃣ Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate      # En Linux / Mac
venv\Scripts\activate       # En Windows
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar la aplicación

```bash
streamlit run app.py
```

Luego abre tu navegador y visita 👉 **http://localhost:8501**

---

##  Dependencias principales

- **streamlit** → interfaz interactiva  
- **pandas / numpy** → manipulación y análisis de datos  
- **plotly** → gráficos dinámicos  
- **openpyxl** → lectura y escritura de archivos Excel  

*(Estas librerías ya están definidas en `requirements.txt`)*

---

##  Lógica de evaluación de riesgo

Cada entidad es evaluada mediante un **índice ponderado de riesgo global (0–100)**.  
Los factores y sus pesos por defecto son:

| Indicador             | Peso | Inverso | Descripción |
|------------------------|------|----------|--------------|
| Liquidez Corriente     | 0.25 | ❌ | Capacidad de pagar deudas a corto plazo |
| Endeudamiento Total    | 0.25 | ✅ | Nivel de deuda frente a activos |
| Margen Neto            | 0.20 | ❌ | Rentabilidad final |
| ROA                    | 0.15 | ❌ | Rentabilidad sobre activos |
| Rotación de Activos    | 0.15 | ❌ | Eficiencia en uso de activos |

El riesgo se clasifica automáticamente según el puntaje obtenido:

| Rango | Categoría | Descripción |
|--------|------------|-------------|
| < 45 | 🔴 **Alto riesgo (Crítico)** | Riesgo financiero severo |
| 45–60 | 🟠 **Riesgo medio (Vigilancia)** | Necesita monitoreo |
| > 60 | 🟢 **Bajo riesgo (Estable)** | Situación financiera sólida |

---

## 🔮 Predicción automática

El modelo estima la **tendencia financiera** de cada entidad según la relación entre liquidez, endeudamiento y margen:

| Resultado | Símbolo | Interpretación |
|------------|----------|----------------|
| 📈 Mejora sostenida | Liquidez y margen altos, endeudamiento bajo |
| ➖ Estable | Comportamiento balanceado |
| ⚠️ Riesgo financiero | Liquidez baja y endeudamiento alto |

---

## 📊 Visualizaciones

La app genera gráficos interactivos con **Plotly**, incluyendo:

- Barras horizontales con la clasificación de riesgo por entidad  
- Métricas resumen globales  
- Tablas ordenables y exportables

---

## 💾 Exportación de resultados

Al finalizar el análisis, puedes descargar el archivo consolidado con todos los cálculos e indicadores:

```
Resultados_SaludEstableAI_Full.xlsx
```

---

##  Ideas de mejora (roadmap)

- [ ] Añadir un modelo predictivo basado en **Machine Learning** (árbol de decisión o regresión logística)
- [ ] Permitir ajuste manual de pesos (`FACTORES_RIESGO`) desde la interfaz
- [ ] Crear **panel de control histórico** con comparación año a año
- [ ] Implementar **modo API** para integración con sistemas externos (ERP o Power BI)

---

## 📄 Derechos de Autor

© 2025 Wilfredo López. Todos los derechos reservados.
Este proyecto, SaludEstable AI, y su código fuente están protegidos bajo licencia de uso académico y no comercial.
Queda prohibida su reproducción, distribución o modificación sin autorización expresa del autor.
Para colaboraciones o permisos de uso, contactar a: [tu correo o perfil de GitHub].

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.  
Puedes usarlo, modificarlo y distribuirlo libremente, dando crédito al autor original.

---

**💊 SaludEstable AI — Inteligencia Financiera para un Sistema de Salud más Sostenible.**
