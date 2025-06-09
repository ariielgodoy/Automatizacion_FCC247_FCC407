# 🛰️ Interfaz de Automatización para Pruebas EMC

Este proyecto es una interfaz gráfica (GUI) desarrollada en **Python con Tkinter** para automatizar la secuencia de pruebas EMC (Compatibilidad Electromagnética), interactuando con un **analizador de espectros** y un **controlador de mástil/mesa rotatoria** mediante conexiones **VISA y TCP/IP**.

> Diseñado para facilitar mediciones en laboratorio según normativas **FCC 15.247** y **15.407**, gestionando variables como frecuencia, altura, polarización y azimut, y capturando resultados automáticamente.

---

## 📷 Captura de pantalla de ejemplo

![image](https://github.com/user-attachments/assets/01df1300-e2eb-4a16-90a6-a28858b5829f)


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
2. **Realización de la medición**:
- `Introducir los parámetros pedidos en la interfaz`
- `La ruta al excel pedida es la del archivo exportado desde EMC32 en formato .xls`
- `La ruta del template debe ser la ruta dentro del analizador, debe incluir el .dfl`
- `"Guardar screenshots en:" pregunta por la ruta en donde guardar las screenshots **EN EL ANALIZADOR**`
- `La corrección del duty debe calcularla el usuario y aplicarle los debidos cálculos, sin embargo, se está trabajando para automatizar ese paso`
