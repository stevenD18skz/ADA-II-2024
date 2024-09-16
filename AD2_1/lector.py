import os


# Abrir y leer el archivo
def ALFile(n = 1, ruta_archivo = ""):

    if ruta_archivo == "":
        # Obtiene la ruta absoluta del directorio donde está el script
        ruta_script = os.path.dirname(os.path.abspath(__file__))

        # Construye la ruta completa del archivo Prueba1.txt
        ruta_archivo = os.path.join(ruta_script, 'Entradas', f'Prueba{n}.txt')

    with open(ruta_archivo, 'r') as archivo:
        # Leer la primera línea y convertirla a entero para obtener n
        n_agentes = int(archivo.readline().strip())
        
        # Inicializar una lista para guardar las parejas
        agentes = []
        
        # Leer las siguientes n líneas y almacenar cada pareja (entero, real)
        for _ in range(n_agentes):
            linea = archivo.readline().strip()
            entero, real = linea.split(',')  # Dividir por la coma

            agentes.append([int(entero), float(real)])  # Convertir a entero y real, y agregar a la lista
        
        # Leer la última línea y guardarla como un entero
        R_max = int(archivo.readline().strip())
    
    return [n_agentes, agentes, R_max]

"""# Mostrar los resultados
print(f'n: {n_agentes}')
print(f'Parejas: {agentes}')
print(f'Último número: {R_max}')"""