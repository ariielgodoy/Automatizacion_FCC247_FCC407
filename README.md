# 🛰️ Interfaz de Automatización para Pruebas EMC

Este proyecto es una interfaz gráfica (GUI) desarrollada en **Python con Tkinter** para automatizar la secuencia de pruebas EMC (Compatibilidad Electromagnética), interactuando con un **analizador de espectros** y un **controlador de mástil/mesa rotatoria** mediante conexiones **VISA y TCP/IP**.

> Diseñado para facilitar mediciones en laboratorio según normativas **FCC 15.247** y **15.407**, gestionando variables como frecuencia, altura, polarización y azimut, y capturando resultados automáticamente.

---

## 📷 Captura de pantalla de ejemplo

![demo](https://via.placeholder.com/800x400.png?text=Interfaz+EMC+Test+Automation)

---

## ⚙️ Características principales

- 📋 **Formulario interactivo** para ingresar los parámetros de la prueba.
- 🔌 **Conexión VISA** al analizador de espectros.
- 🛠️ **Control por socket TCP/IP** del mástil y la mesa de pruebas.
- 📊 **Lectura automática de datos desde Excel**.
- 📸 **Captura de pantalla del analizador** y guardado con nombres personalizados.
- 📁 **Persistencia de datos**: guarda y recupera configuraciones automáticamente.
- 📈 **Análisis de resultados** con cálculos de márgenes (AVG + DUTY y PEAK).
- 🚧 Detecta si una frecuencia está en banda restringida y ajusta la medición.

---

## 🧰 Tecnologías utilizadas

- `Python 3`
- `Tkinter` – Interfaz gráfica
- `PyVISA` – Comunicación con instrumentos de medida
- `Pandas` – Lectura de Excel y procesamiento de datos
- `Socket` – Control del sistema de posicionamiento
- `Tabulate` – Presentación elegante de resultados

---

## 📝 Cómo usar

1. **Instalación de dependencias**:
   ```bash
   pip install pyvisa pandas tabulate
