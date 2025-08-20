# Automatización FFC 15.247 y FCC 15.407
## Interfaz de Usuario

A continuación se muestra la interfaz principal del programa:

![image](https://github.com/user-attachments/assets/83358e3f-9c1b-453f-b397-50428729e396)



  
*Figura B1. Interfaz principal del programa.*

---

## Descripción de los elementos de la interfaz

| Nº | Elemento en la interfaz             | Descripción                                                                 |
|----|-------------------------------------|-----------------------------------------------------------------------------|
| 1  | **Generación de nombre de archivo** | Los campos oferta, cliente, norma, modulación, canal y active port son usados para nombrar las capturas                         |
| 2  | **IP analizador e IP controlador**  | Se introduce la IP del analizador y del controlador de la mesa giratoria y mástil|
| 3  | **Ruta del template**          | Se escribe la ruta al template dentro del analizador incluyendo el .dfl                |
| 4  | **Archivo excel**      | Ruta al archivo excel que ha sido exportado desde EMC32             |
| 5  | **Corrección del duty**    | se introduce la correccion del duty según la expresión: corrección = 10*log(1/duty)                          |
| 6  | **Guardar screenshots en:**    | Especificar la ruta de la carpeta en donde guardar las capturas de pantallas **DENTRO** del analizador                          |

---
## Obtención del excel de EMC32
### 1º Maximización en EMC32.
Se maximizan todos los puntos necesarios según indique la norma para encontrar la posición y altura peor. 
### 2º Exportar Frecuencias
Salir del modo de medida, y exportar la tabla de Critical_Freqs haciendo clic en el botón que se ve en la imagen:

![image]([https://github.com/user-attachments/assets/977fae63-518d-41bf-8d35-c10d97d29917](https://github.com/user-attachments/assets/e9fbd9a3-bc80-42b9-80b7-7a7b17678fa9))


*Figura B2. Tabla EMC32 y botón de exportar*

---

## Proceso de actuación del programa
### 1º Iniciar proceso
Una vez rellenados los campos, pulsar el botón "Iniciar proceso".  Resultado: una por una, el programa busca todas las frecuencias y hace la maximización, tomando el control del analizador y el controlador de la mesa y mástil. Las capturas quedan guardadas donde hemos indicado, y además, el programa devuelve una tabla con la información medida

### 2º Actualizar el emc32
Finalmente, volvemos al emc32 y manualmente actualizamos la tabla de Final_Result, con los valores nuevos, para que se corrija la posición de los puntos. En la tabla que devuelve el programa el margen ya está corregido, así como la media de AVG con el duty cycle.

![image]([https://github.com/user-attachments/assets/3f1d730f-bbf0-4c9f-bee9-1d0920bc8a86](https://github.com/user-attachments/assets/b0fc1a42-77ed-4ddf-9f23-14804f4f0cd6))


*Figura B3. Tabla de resumen de medidas*


---

**Autor:** Juan Ariel Godoy Báez        
**Puesto:** Becario

**Director del proyecto:** Álvaro Borrego Robles          
**Puesto:** Técnico de ensayos

**Departamento:** Electromagnetic and Radio Matters (Connected Car)
