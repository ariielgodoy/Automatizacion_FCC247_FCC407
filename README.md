# ⚙️ Automatización FCC 15.247 & FCC 15.407

> 🚀 **Herramienta automatizada para ensayos EMC**  


---

## 🎛️ Vista General de la Interfaz

A continuación, una vista previa de la interfaz principal:

<p align="center">
  <img src="https://github.com/user-attachments/assets/154df958-373c-49cc-8508-58830892d285" width="700" />
</p>

<p align="center"><em>Figura B1. Interfaz principal del programa</em></p>

---

## 🧩 Descripción de los Elementos de la Interfaz

| Nº 🔢 | Elemento 🎨                        | Descripción 📝                                                                                                                                                                                                                 |
|-------|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1️⃣   | **Generación de nombre de archivo** | Campos como oferta, cliente, norma, modulación, canal y puerto activo son usados para nombrar las capturas.                                                                                                                 |
| 2️⃣   | **IP del analizador y controlador** | Introducir la IP del analizador y del controlador (mesa giratoria y mástil). Si se usa **FRANKONIA**, configurar el **tilt** en la web. Si solo se usa un FRANKONIA, introducir la misma IP en ambos campos. En EMC32 deben colocarse como dispositivos virtuales para evitar conflictos. |
| 3️⃣   | **Ruta del template**              | Escribir la ruta al archivo `.dfl` del analizador.                                                                                                                                                                            |
| 4️⃣   | **Archivo Excel**                  | Ruta del archivo Excel exportado desde **EMC32**.                                                                                                                                                                            |
| 5️⃣   | **Duty Cycle**                     | Ingresar el valor medido del duty cycle. El programa aplica la corrección automáticamente:  
`corrección = 10 * log(1/duty)`                                                                                                             |
| 6️⃣   | **Guardar screenshots en:**        | Ruta de la carpeta dentro del analizador donde se guardarán las capturas de pantalla.                                                                                                                                         |

---

## 📤 Exportación del Excel desde EMC32

### 🔍 Paso 1: Maximización

Maximizar todos los puntos necesarios según la norma para encontrar la peor **posición y altura**.

### 📁 Paso 2: Exportar Frecuencias Críticas

Salir del modo de medida y exportar la tabla **Critical_Freqs** haciendo clic en el botón que aparece en la siguiente imagen:

<p align="center">
  <img src="https://github.com/user-attachments/assets/0792fb27-1b7b-4d15-b435-a1185092018b" width="600" />
</p>

<p align="center"><em>Figura B2. Tabla de EMC32 y botón de exportación</em></p>

---

## 🔄 Proceso de Ejecución del Programa

### ▶️ Paso 1: Iniciar Proceso

Una vez rellenados todos los campos, pulsar **"Iniciar proceso"**.

🛠️ El programa:
- Recorre todas las frecuencias.
- Realiza la maximización.
- Controla automáticamente el analizador y el/los controlador(es).
- Guarda capturas de pantalla en la carpeta indicada.
- Genera una tabla con los resultados medidos.

---

### 🧮 Paso 2: Actualizar el EMC32

Volver al EMC32 y **actualizar manualmente** la tabla `Final_Result` con los nuevos valores.

✅ La tabla generada por el programa incluye:
- Margen ya corregido.
- Media de AVG con corrección por duty cycle.

<p align="center">
  <img src="https://github.com/user-attachments/assets/3f1d730f-bbf0-4c9f-bee9-1d0920bc8a86" width="700" />
</p>

<p align="center"><em>Figura B3. Tabla resumen de medidas</em></p>

---

## 👨‍💻 Autores y Créditos

| Rol 📌 | Nombre 🧑‍💻 | Puesto 🏷️ |
|--------|--------------|------------|
| 🧑‍🎓 **Autor** | **Juan Ariel Godoy Báez** | Becario |
| 👨‍🔬 **Director del proyecto** | **Álvaro Borrego Robles** | Técnico de Ensayos |
| 🏢 **Departamento** | **Electromagnetic and Radio Matters (Connected Car)** | |

---

> 💡 *Diseñado para agilizar los ensayos de conformidad EMC bajo las normativas FCC 15.247 y FCC 15.407, con enfoque en precisión, automatización y eficiencia.*

---
