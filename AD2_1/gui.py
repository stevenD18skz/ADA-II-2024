import tkinter as tk
from tkinter import filedialog, messagebox
from customtkinter import *
import os
import time, timeit



import lector
from AlgoritmoBruto import *
from AlgoritmoVoraz import *

moderacion = None
solucionVoraz = None

def cargar_archivo():
    global moderacion, solucionVoraz
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_entradas = os.path.join(ruta_script, 'Entradas')
    
    file_path = filedialog.askopenfilename(
        title="Seleccionar archivo",
        initialdir=ruta_entradas,
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    
    if file_path:
        with open(file_path, 'r') as f:
            entrada_texto.delete(1.0, tk.END)  # Limpiar el área de texto
            entrada_texto.insert(tk.END, f.read())  # Cargar el contenido
        
        n_agentes, agentes, R_max = lector.ALFile(ruta_archivo=file_path)
        moderacion = RedSocialModeracion(n_agentes, agentes, R_max)
        solucionVoraz = RedSocialModeracionVoraz(n_agentes, agentes, R_max)

        return file_path
    
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

    return None




def solucionar(eleccion):
    global moderacion, solucionVoraz

    diccionario_soluciones = {
        1: moderacion.hallarMejorEstrategia,
        2: solucionVoraz.algoritmo_voraz
    }

    diccionario_titulos = {
        1: "BRUTA",
        2: "VORAZ"
    }






    estado_label.config(text="Cargando...")
    start_time = time.time()
    solucion = diccionario_soluciones[eleccion]()
    end_time = time.time()
    elapsed_time = end_time - start_time
    estado_label.config(text=f"Completado, se ah usado la solucion {diccionario_titulos[eleccion]}, en {elapsed_time:.80f}")

    solucion_outPut = ""
    solucion_outPut += f'{solucion[1]}\n' #extremismo final de la red social arreglada
    solucion_outPut += f'{solucion[2]}\n' #Exfuerzo para mejorar la red social
    for x in solucion[0]:
        solucion_outPut += f"{x}\n"


    # Mostrar la solución en el área de salida
    salida_texto.delete(1.0, tk.END)  # Limpiar el área de salida
    salida_texto.insert(tk.END, solucion_outPut)

    # Guardar la solución en un archivo de texto
    guardar_solucion(solucion_outPut)

    """
    estado_label.config(text="Cargando...")
    timer = timeit.Timer(lambda: moderacion.hallarMejorEstrategia())
    tiempo = timer.timeit(number=1000)
    solucion = moderacion.hallarMejorEstrategia()
    estado_label.config(text=f"Tiempo de ejecución: {tiempo:.6f} segundos")
    """





def guardar_solucion(solucion_outPut):
    with open('./AD2_1/salida.txt', 'w') as file:
        file.write(solucion_outPut)

    messagebox.showinfo("Éxito", "Solución guardada correctamente.")

    return None
    archivo_guardar = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")),
        title="Guardar solución"
    )

    if archivo_guardar:
        with open(archivo_guardar, 'w') as f:
            f.write(solucion_outPut)

        messagebox.showinfo("Éxito", "Solución guardada correctamente.")
        
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó un archivo para guardar.")





# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz de Solución de Problemas")
ventana.geometry("800x600")
ventana.configure(bg="#2C3E50")  # Fondo oscuro para una apariencia moderna

# Obtener el tamaño de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcular la posición para centrar la ventana
ancho_ventana = 800
alto_ventana = 600
pos_x = int((ancho_pantalla - ancho_ventana) / 2)
pos_y = int((alto_pantalla - alto_ventana) / 2)

# Establecer la geometría de la ventana con la posición calculada
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

# Etiqueta de Título
titulo_label = tk.Label(ventana, text="Solución de Problemas - Red Social", font=("Arial", 18, "bold"), bg="#2C3E50", fg="white")
titulo_label.pack(pady=10)

# Frame para dividir la ventana en 3 columnas
frame = tk.Frame(ventana, bg="#2C3E50")
frame.pack(pady=20, padx=20, expand=True, fill="both")

# Área de texto para la entrada (visualizar el archivo cargado)
entrada_texto = tk.Text(frame, height=20, width=30, wrap="word", bg="#ECF0F1", fg="#2C3E50", font=("Arial", 12))
entrada_texto.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Botón de "Cargar Archivo" personalizado
boton_cargar = CTkButton(master=frame, text="Cargar Archivo", corner_radius=10, command=cargar_archivo, 
                                   fg_color="#3498DB", hover_color="#2980B9")
boton_cargar.grid(row=1, column=0, padx=10, pady=10)

# Botón de "Cargar Archivo" personalizado
boton_cargar = CTkButton(master=frame, text="Cargar Archivo", corner_radius=10, command=cargar_archivo, 
                                   fg_color="#3498DB", hover_color="#2980B9")
boton_cargar.grid(row=1, column=0, padx=10, pady=10)

# Botones de "Solucionar 1", "Solucionar 2" y "Solucionar 3"
frame_botones = tk.Frame(frame, bg="#2C3E50")
frame_botones.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

# Botón Solucionar 1
boton_solucionar1 = CTkButton(master=frame_botones, text="Solucionar 1", corner_radius=10, command=lambda: solucionar(1), 
                                       fg_color="#E74C3C", hover_color="#C0392B")
boton_solucionar1.pack(side="left", padx=5)

# Botón Solucionar 2
boton_solucionar2 = CTkButton(master=frame_botones, text="Solucionar 2", corner_radius=10, command=lambda: solucionar(2), 
                                       fg_color="#E67E22", hover_color="#D35400")
boton_solucionar2.pack(side="left", padx=5)

# Botón Solucionar 3
boton_solucionar3 = CTkButton(master=frame_botones, text="Solucionar 3", corner_radius=10, command=lambda: solucionar(3), 
                                       fg_color="#1ABC9C", hover_color="#16A085")
boton_solucionar3.pack(side="left", padx=5)

# Área de texto para la salida (visualizar la solución)
salida_texto = tk.Text(frame, height=20, width=30, wrap="word", bg="#ECF0F1", fg="#2C3E50", font=("Arial", 12))
salida_texto.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

# Etiqueta para mostrar el estado ("Cargando...", "Completado", etc.)
estado_label = tk.Label(ventana, text="", font=("Arial", 12), bg="#2C3E50", fg="white")
estado_label.pack(pady=10)

# Configurar la grilla para que se ajuste al redimensionar
frame.columnconfigure(0, weight=1)
frame.columnconfigure(2, weight=1)
frame.rowconfigure(0, weight=1)

# Iniciar la aplicación
ventana.mainloop()
