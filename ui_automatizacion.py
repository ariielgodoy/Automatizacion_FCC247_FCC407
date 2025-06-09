import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pyvisa
import time
import pandas as pd
import socket
from pathlib import Path
from tabulate import tabulate
import json


#COSAS A HACER
#Cuando hay que maximizar fuera de la RB, hay que maximizar igual pero el Video BW tienen que ser a 300K y el Resolution BW a 100K

fuera_RB = ""

class Aplicacion:

    def cargar_datos(self):
            if os.path.exists("datos_guardados.json"):
                with open("datos_guardados.json", "r") as f:
                    datos = json.load(f)
                    self.oferta.insert(0, datos.get("oferta", ""))
                    self.cliente.insert(0, datos.get("cliente", ""))
                    self.norma.set(datos.get("norma", ""))
                    self.modulacion.insert(0, datos.get("modulacion", ""))
                    self.canal.insert(0, datos.get("canal", ""))
                    self.ip_analizador.insert(0, datos.get("ip_analizador", ""))
                    self.ip_controlador.insert(0, datos.get("ip_controlador", ""))
                    self.ruta_template.insert(0, datos.get("ruta_template", ""))
                    self.ruta_archivo_excel.set(datos.get("ruta_excel", ""))
                    self.correccion_duty.insert(0, datos.get("correccion_duty", ""))
                    self.ruta_guardar.set(datos.get("ruta_guardar", ""))
                    self.active_port.insert(0, datos.get("active_port", ""))


    
    def guardar_datos(self, datos):
            with open("datos_guardados.json", "w") as f:
                json.dump(datos, f)


    def __init__(self, root):
        self.root = root
        self.root.title("Explorador de Archivos para Pruebas EMC")

        # Campos de entrada
        self.oferta = self.crear_entrada("Oferta:", 0)
        self.cliente = self.crear_entrada("Cliente:", 1)

        # Menú desplegable para seleccionar la norma
        tk.Label(root, text="Norma:").grid(row=2, column=0, sticky="e")
        self.norma = tk.StringVar()
        opciones_norma = ["15.247", "15.407"]
        tk.OptionMenu(root, self.norma, *opciones_norma).grid(row=2, column=1, sticky="w")

        self.modulacion = self.crear_entrada("Modulación:", 3)
        self.canal = self.crear_entrada("Canal:", 4)
        self.active_port = self.crear_entrada("Active Port:", 5)
        self.ip_analizador = self.crear_entrada("IP del analizador:", 6)
        self.ip_controlador = self.crear_entrada("IP del controlador:", 7)
        self.ruta_template = self.crear_entrada("Ruta del template:", 8)

        # Botón para explorar archivo Excel
        self.ruta_archivo_excel = tk.StringVar()
        tk.Label(root, text="Archivo Excel:").grid(row=9, column=0, sticky="e")
        tk.Entry(root, textvariable=self.ruta_archivo_excel, width=50).grid(row=9, column=1)
        tk.Button(root, text="Explorar", command=self.seleccionar_archivo_excel).grid(row=9, column=3)

        # Corrección del duty
        self.correccion_duty = self.crear_entrada("Corrección del duty:", 10)

        # Ruta para guardar screenshots
        self.ruta_guardar = tk.StringVar()
        tk.Label(root, text="Guardar screenshots en:").grid(row=11, column=0, sticky="e")
        tk.Entry(root, textvariable=self.ruta_guardar, width=50).grid(row=12, column=1, columnspan=2)

        # Botón de iniciar
        tk.Button(root, text="Iniciar Proceso", command=self.iniciar_proceso).grid(row=13, column=1, pady=10)
        
        self.cargar_datos()


    def crear_entrada(self, texto, fila):
        tk.Label(self.root, text=texto).grid(row=fila, column=0, sticky="e")
        entrada = tk.Entry(self.root, width=50)
        entrada.grid(row=fila, column=1, columnspan=2)
        return entrada

    def seleccionar_archivo_excel(self):
        archivo = filedialog.askopenfilename(
            filetypes=[("Archivos Excel", "*.xls *.xlsx")],
            title="Seleccionar archivo Excel"
        )
        if archivo:
            self.ruta_archivo_excel.set(archivo)

    def iniciar_proceso(self):
        datos = {
            "oferta": self.oferta.get(),
            "cliente": self.cliente.get(),
            "norma": self.norma.get(),
            "modulacion": self.modulacion.get(),
            "canal": self.canal.get(),
            "active_port": self.active_port.get(),
            "ip_analizador": self.ip_analizador.get(),
            "ip_controlador": self.ip_controlador.get(),
            "ruta_template": self.ruta_template.get(),
            "ruta_excel": self.ruta_archivo_excel.get(),
            "correccion_duty": self.correccion_duty.get(),
            "ruta_guardar": self.ruta_guardar.get()
        }

        self.guardar_datos(datos)

        


        # IP y puerto del controlador CO3000 //Creo que esta parte no hace falta
        HOST = datos["ip_controlador"]
        PORT = 5025


        #ENVIO DE COMANDOS AL CONTROLADOR DEL MASTIL Y LA MESA
        class ControladorCO3000:
            def __init__(self, host, port=5025, timeout=5):
                self.host = host
                self.port = port
                self.timeout = timeout
                self.socket = None

            def conectar(self):
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.settimeout(self.timeout)
                self.socket.connect((self.host, self.port))
                print("Conectado al controlador")

            def enviar_comando(self, comando):
                if self.socket is None:
                    raise RuntimeError("La conexión no está abierta.")
                self.socket.sendall((comando + "\n").encode())
                respuesta = self.socket.recv(1024)
                return respuesta.decode().strip()

            def cerrar(self):
                if self.socket:
                    self.socket.close()
                    self.socket = None
                    print("Conexión cerrada")



        def is_span_in_restricted_band(freq_center, restricted_bands):
            global fuera_RB
            span = 5
            start_span = freq_center - span / 2
            end_span = freq_center + span / 2

            
            
            for start_band, end_band in restricted_bands:
                # Si hay solapamiento

                if (freq_center >= start_band and freq_center <= end_band):
                    if fuera_RB == "SI":
                        fuera_RB = "NO"
                    
                    freq_before = start_band + span / 2
                    freq_after = end_band - span / 2
                    if (start_span > start_band) and (end_span < end_band):
                        return freq_center 
                    elif (start_span < start_band):
                        return freq_before
                    elif(end_span > end_band):
                        return freq_after
                    
            
            fuera_RB = "SI"
            return freq_center



        #LAS BANDAS RESTRINGIDAS DE CADA NORMA

        bandas_restringidas_247 = sorted([
            (960.000000, 1240.000000),
            (1300.000000, 1427.000000),
            (1435.000000, 1626.500000),
            (1645.500000, 1646.500000),
            (1660.000000, 1710.000000),
            (1718.800000, 1722.200000),
            (2200.000000, 2300.000000),
            (2310.000000, 2390.000000),
            (2483.500000, 2500.000000),
            (2690.000000, 2900.000000),
            (3260.000000, 3267.000000),
            (3332.000000, 3339.000000),
            (3345.800000, 3358.000000),
            (3600.000000, 4400.000000),
            (4500.000000, 5150.000000),
            (5350.000000, 5460.000000),
            (7250.000000, 7750.000000),
            (8025.000000, 8500.000000),
            (9000.000000, 9200.000000),
            (9300.000000, 9500.000000),
            (10600.000000, 12700.000000),
            (13250.000000, 13400.000000),
            (14470.000000, 14500.000000),
            (15350.000000, 16200.000000),
            (17700.000000, 21400.000000),
            (22010.000000, 23120.000000),
            (23600.000000, 24000.000000),
            (31200.000000, 31800.000000),
            (36430.000000, 36500.000000),
        ], key=lambda x: x[0])

        bandas_restringidas_407 = sorted([
            (960.000000, 1240.000000),
            (1300.000000, 1427.000000),
            (1435.000000, 1626.500000),
            (1645.500000, 1646.500000),
            (1660.000000, 1710.000000),
            (1718.800000, 1722.200000),
            (2200.000000, 2300.000000),
            (2310.000000, 2390.000000),
            (2483.500000, 2500.000000),
            (2690.000000, 2900.000000),
            (3260.000000, 3267.000000),
            (3332.000000, 3339.000000),
            (3345.800000, 3358.000000),
            (3600.000000, 4400.000000),
            (4500.000000, 5150.000000),
            (5350.000000, 5460.000000),
            (7250.000000, 7750.000000),
            (8025.000000, 8500.000000),
            (9000.000000, 9200.000000),
            (9300.000000, 9500.000000),
            (10600.000000, 12700.000000),
            (13250.000000, 13400.000000),
            (14470.000000, 14500.000000),
            (15350.000000, 16200.000000),
            (17700.000000, 21400.000000),
            (22010.000000, 23120.000000),
            (23600.000000, 24000.000000),
            (31200.000000, 31800.000000),
            (36430.000000, 36500.000000),
        ])




        #Pedirle al usuario que me de los datos para el nombre
        oferta = datos["oferta"]
        cliente = datos["cliente"]
        norma = datos["norma"]
        modulacion = datos["modulacion"]
        canal = datos["canal"]
        ruta_archivo_excel = datos["ruta_excel"]


        df = pd.read_excel(ruta_archivo_excel, header=0)

        unidades = df.iloc[0].to_dict()

        df_datos = df.drop(index=[0,1,2]).reset_index(drop=True)

        df_datos = df_datos.drop_duplicates(subset='Frequency')

        datos_necesarios = df_datos[['Frequency', 'Height','Pol','Azimuth']]

        frecuencias = df_datos['Frequency'].tolist()
        heights = df_datos['Height'].tolist()
        polarizaciones = df_datos['Pol'].tolist()
        azimuts = df_datos['Azimuth'].tolist()

        print(frecuencias)
        print(heights)


        # Dirección del recurso VISA
        visa_address = "TCPIP0::" + datos["ip_analizador"] + "::inst0::INSTR"
        ruta = datos["ruta_template"]

        correccion_duty = datos["correccion_duty"]

        controlador = ControladorCO3000(datos["ip_controlador"])


        try:
            rm = pyvisa.ResourceManager()
            instr = rm.open_resource(visa_address)
            instr.timeout = 40000
            
            # Identificación del instrumento
            print("Identificación:", instr.query("*IDN?"))

            # Seleccionar qué elementos cargar (puede ser USER, ALL, HWSETtings, etc.)
            instr.write("MMEM:SEL:ALL")

            # Cargar la configuración desde el archivo .dfl
            print(f"Cargando archivo: {ruta}")
            instr.write(f'MMEM:LOAD:STAT 1,"{ruta}"')
            
            # Comprobar si hubo errores
            print("Estado del sistema:", instr.query("SYST:ERR?"))

            # Configurar Trace 1 como Max Hold y Trace 2 como Average
            instr.write("TRAC1:MODE MAXH")
            instr.write("TRAC2:MODE AVER")

            # Mostrar ambas trazas en pantalla
            instr.write("DISP:TRAC1 ON")
            instr.write("DISP:TRAC2 ON")




            controlador.conectar()
            resultados = []
            ruta_guardar_screenshot = datos["ruta_guardar"]
            for i in range(len(frecuencias)):
                # 🚀 Lanzar single sweep
                print("Configurando modo single sweep...")
                instr.write("INIT:CONT OFF")

                frecuencias[i] = is_span_in_restricted_band(float(frecuencias[i]), bandas_restringidas_247)
                #Colocar la center frequency
                instr.write("FREQ:CENT " + str(frecuencias[i]) + "MHz")
                print("Colocando la Center Frequency")


                #AÑADIR UNA CONDICION CON LA RESTRICTED BAND
                #Se coloca el span
                instr.write(f"FREQ:SPAN 5MHz")
                print("Definiendo el span")





                #MOVER MASTIL Y MESA
                controlador.enviar_comando("LD DS1 DV")
                controlador.enviar_comando("LD " + str(azimuts[i]) +" DG NP GO")
                controlador.enviar_comando("LD TMPM1 DV")
                controlador.enviar_comando("LD 1 INT AT")
                controlador.enviar_comando("LD " + str(heights[i]) +" CM NP GO")
                controlador.enviar_comando("P" + str(polarizaciones[i]))



                #MONITORIZACION DE LAS POSICIONES
                while True:
                    control_mesa = controlador.enviar_comando("STATUS DS1 ?")
                    control_mastil = controlador.enviar_comando("STATUS TMPM1 ?")

                    partes_mesa = control_mesa.split(',')
                    partes_mastil = control_mastil.split(',')

                    movimiento_mesa = partes_mesa[1].strip()
                    movimiento_mastil = partes_mastil[1].strip()

                    if movimiento_mastil == '0' and movimiento_mesa == '0':
                        break



                #MOVER MARCADOR 1 Y MARCADOR 2
                instr.write("CALC:MARK1:TRAC 1")
                instr.write("CALC:MARK2:TRAC 2")
                print("Lanzando sweep único...")
                instr.write("INIT")
                instr.query("*OPC?")  # Espera a que termine
                print("Sweep único realizado.")
                print("Realizando búsqueda de pico...")
                instr.write("CALC:MARK2:MAX")
                instr.write("CALC:MARK1:MAX")

                peak_level_maxh = instr.query("CALC:MARK1:Y?")
                peak_level_avg = instr.query("CALC:MARK2:Y?")

                print(f"Nivel del pico: {peak_level_maxh.strip()} dBm")
                print(f"Nivel del pico: {peak_level_avg.strip()} dBm")




                #GUARDAR CAPTURA DE PANTALLA
                #FALTA CREAR LA RUTA DEPENDIENDO DE CIERTOS DATOS COMO LA FRECUENCIA Y DEMAS
                #FALTA CREAR EL NOMBRE DEL ARCHIVO
                ruta_screenshot = ruta_guardar_screenshot + oferta + "_" + cliente + "_" + norma + "_" + modulacion + "_" + canal +  "_" + datos["active_port"] + "_" + str(frecuencias[i]) + "MHz" + ".jpeg"
                print(ruta_screenshot)
                print("Guardando captura de pantalla")
                instr.write(f"MMEM:NAME '{ruta_screenshot}'")
                instr.write("HCOP:IMM1")
                instr.query("*OPC?")


                #SUMAR AL MARKER 2 EL DUTY
                average_corregido = float(peak_level_avg) + float(correccion_duty)

                #CALCULAR EL MARGEN
                margin = 54 - average_corregido
                margin_peak = 74 - float(peak_level_maxh)
                print("\n" + "Average corregido: " + str(average_corregido) + ", margen: " + str(margin) + ", Frecuencia: " + str(frecuencias[i]) + "MHz" + "\n")


                resultados.append({
                    "Frecuencia (MHz)": frecuencias[i],
                    "MKR PK (dBm)": float(peak_level_maxh.strip()),
                    "Margen (PEAK)": margin_peak,
                    "MKR AVG (dBm)": float(peak_level_avg.strip()),
                    "AVG CON CORRECCION DUTY": average_corregido,
                    "Margen (AVG)": margin,
                    "Fuera restricted band?": fuera_RB
                })

                print("Proceso ",i , " finalizado, recuerda mirar si se ha guardado todo bien")


            print("\n")
            print("\n")
            print("\n")
            print("\n")
            if resultados:
                print("+" + "-"*60 + "+")
                print("|{:^60}|".format("RESULTADOS DE LA MEDICIÓN"))
                print("+" + "-"*60 + "+")
                print(tabulate(resultados, headers="keys", tablefmt="fancy_grid", floatfmt=".2f"))

            instr.close()
            controlador.cerrar()

        except Exception as e:
            print("Error al acceder al analizador:", e)
        
######################################################################################ACABA LOGICA DEL CODIGO

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
