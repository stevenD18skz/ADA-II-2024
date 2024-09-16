import tkinter as tk
from tkinter import filedialog, messagebox
from customtkinter import *
import os

import lector
from AlgoritmoBruto import *

agentes = None

# Función para cargar el archivo de texto con el problema
def cargar_archivo():
    global agentes  # Indica que vamos a modificar la variable global agentes
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    
    
    if archivo:
        with open(archivo, 'r') as f:
            entrada_texto.delete(1.0, tk.END)  # Limpiar el área de texto
            entrada_texto.insert(tk.END, f.read())  # Cargar el contenido
        
        n_agentes, agentes, R_max = lector.ALFile(ruta_archivo=archivo)
        print(n_agentes, agentes, R_max)

        return archivo
    
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

    return None




# Función para procesar el problema y mostrar la solución
def solucionar():
    global agentes  # Indica que vamos a usar la variable global agentes
    solucion = hallarMejorEstrategia(agentes)
    print(solucion)
    print("="*80)

    # Mostrar la solución en el área de salida
    salida_texto.delete(1.0, tk.END)  # Limpiar el área de salida
    salida_texto.insert(tk.END, solucion)

    # Guardar la solución en un archivo de texto
    guardar_solucion(solucion)




def guardar_solucion(solucion):
    archivo_guardar = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")),
        title="Guardar solución"
    )
    if archivo_guardar:
        with open(archivo_guardar, 'w') as f:
            f.write(solucion)
        messagebox.showinfo("Éxito", "Solución guardada correctamente.")
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó un archivo para guardar.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz de Solución de Problemas")
ventana.geometry("800x600")
ventana.configure(bg="#2C3E50")  # Fondo oscuro para una apariencia moderna

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

# Botón de "Solucionar" personalizado
boton_solucionar = CTkButton(master=frame, text="Solucionar", corner_radius=10, command=solucionar, 
                                       fg_color="#E74C3C", hover_color="#C0392B")
boton_solucionar.grid(row=0, column=1, padx=10, pady=10)

# Área de texto para la salida (visualizar la solución)
salida_texto = tk.Text(frame, height=20, width=30, wrap="word", bg="#ECF0F1", fg="#2C3E50", font=("Arial", 12))
salida_texto.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

# Configurar la grilla para que se ajuste al redimensionar
frame.columnconfigure(0, weight=1)
frame.columnconfigure(2, weight=1)
frame.rowconfigure(0, weight=1)

# Iniciar la aplicación
ventana.mainloop()
