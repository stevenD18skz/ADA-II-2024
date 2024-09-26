import tkinter as tk
from tkinter import filedialog, messagebox
from customtkinter import *
import os
import time

import lector
from AlgoritmoBruto import *
from AlgoritmoVoraz import *
from AlgoritmoDinamico import *

class GUI:
    def __init__(self):
        self.moderacion = None
        self.solucionVoraz = None
        self.dinamica = None
        self.ventana = None
        self.entrada_texto = None
        self.nombre_archivo_label = None
        self.salida_texto = None
        self.estado_label = None

    def cargar_archivo(self):
        ruta_script = os.path.dirname(os.path.abspath(__file__))
        ruta_entradas = os.path.join(ruta_script, 'Entradas')
        
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo",
            initialdir=ruta_entradas,
            filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
        )
        
        if file_path:
            with open(file_path, 'r') as f:
                self.entrada_texto.delete(1.0, tk.END)  # Limpiar el área de texto
                self.entrada_texto.insert(tk.END, f.read())  # Cargar el contenido

            # Actualizar la etiqueta con el nombre del archivo
            self.nombre_archivo_label.config(text=f"Archivo cargado: {os.path.basename(file_path)}")
            
            n_agentes, agentes, R_max = lector.ALFile(ruta_archivo=file_path)
            RS = (agentes, R_max)
            self.moderacion = modexFB(RS)
            self.solucionVoraz = modexV(RS)
            self.dinamica = modexPD(RS)

            return file_path
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")
        return None

    def solucionar(self, eleccion):
        diccionario_soluciones = {
            1: self.moderacion.solucionar,
            2: self.solucionVoraz.solucionar,
            3: self.dinamica.solucionar
        }

        diccionario_titulos = {
            1: "BRUTA",
            2: "VORAZ",
            3: "DINAMICA"
        }

        self.estado_label.config(text="Cargando...")
        start_time = time.time()
        solucion = diccionario_soluciones[eleccion]()  # Solucion
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.estado_label.config(text=f"Completado, se ha usado la solución {diccionario_titulos[eleccion]}, en {elapsed_time:.6f} segundos")

        solucion_outPut = f'{solucion[1]}\n{solucion[2]}\n'
        for x in solucion[0]:
            solucion_outPut += f"{x}\n"

        # Mostrar la solución en el área de salida
        self.salida_texto.delete(1.0, tk.END)
        self.salida_texto.insert(tk.END, solucion_outPut)

        # Guardar la solución en un archivo de texto
        self.guardar_solucion(solucion_outPut)

    def guardar_solucion(self, solucion_outPut):
        with open('./AD2_1/salida.txt', 'w') as file:
            file.write(solucion_outPut)

        messagebox.showinfo("Éxito", "Solución guardada correctamente.")

    def run(self):
        self.ventana = tk.Tk()
        self.ventana.title("Interfaz de Solución de Problemas")
        self.ventana.geometry("800x600")
        self.ventana.configure(bg="#2C3E50")

        # Obtener tamaño de la pantalla y centrar la ventana
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        ancho_ventana = 800
        alto_ventana = 600
        pos_x = int((ancho_pantalla - ancho_ventana) / 2)
        pos_y = int((alto_pantalla - alto_ventana) / 2)
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

        # Etiqueta de título
        titulo_label = tk.Label(self.ventana, text="Solución de Problemas - Red Social", font=("Arial", 18, "bold"), bg="#2C3E50", fg="white")
        titulo_label.pack(pady=10)

        # Frame para dividir la ventana en columnas
        frame = tk.Frame(self.ventana, bg="#2C3E50")
        frame.pack(pady=20, padx=20, expand=True, fill="both")

        # Área de texto para la entrada
        self.entrada_texto = tk.Text(frame, height=20, width=30, wrap="word", bg="#ECF0F1", fg="#2C3E50", font=("Arial", 12))
        self.entrada_texto.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Etiqueta para mostrar el nombre del archivo cargado
        self.nombre_archivo_label = tk.Label(frame, text="Ningún archivo cargado", font=("Arial", 10), bg="#2C3E50", fg="white")
        self.nombre_archivo_label.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")


        # Botón para cargar archivo
        boton_cargar = CTkButton(master=frame, text="Cargar Archivo", corner_radius=10, command=self.cargar_archivo,
                                fg_color="#3498DB", hover_color="#2980B9")
        boton_cargar.grid(row=2, column=0, padx=10, pady=10)

        # Botones de solución
        frame_botones = tk.Frame(frame, bg="#2C3E50")
        frame_botones.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        # Botones de solución con distintos algoritmos
        boton_solucionar1 = CTkButton(master=frame_botones, text="Solución BRUTA", corner_radius=10, command=lambda: self.solucionar(1),
                                      fg_color="#E74C3C", hover_color="#C0392B")
        boton_solucionar1.pack(side="left", padx=5)

        boton_solucionar2 = CTkButton(master=frame_botones, text="Solución VORAZ", corner_radius=10, command=lambda: self.solucionar(2),
                                      fg_color="#E67E22", hover_color="#D35400")
        boton_solucionar2.pack(side="left", padx=5)

        boton_solucionar3 = CTkButton(master=frame_botones, text="Solución DINÁMICA", corner_radius=10, command=lambda: self.solucionar(3),
                                      fg_color="#1ABC9C", hover_color="#16A085")
        boton_solucionar3.pack(side="left", padx=5)

        # Área de texto para la salida
        self.salida_texto = tk.Text(frame, height=20, width=30, wrap="word", bg="#ECF0F1", fg="#2C3E50", font=("Arial", 12))
        self.salida_texto.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        # Etiqueta de estado
        self.estado_label = tk.Label(self.ventana, text="", font=("Arial", 12), bg="#2C3E50", fg="white")
        self.estado_label.pack(pady=10)

        # Configurar la grilla para redimensionar
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(2, weight=1)
        frame.rowconfigure(0, weight=1)

        # Iniciar el bucle de la aplicación
        self.ventana.mainloop()
