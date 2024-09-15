# Abrir y leer el archivo
with open('/Entradas/Prueba13txt', 'r') as archivo:
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

# Mostrar los resultados
print(f'n: {n_agentes}')
print(f'Parejas: {agentes}')
print(f'Último número: {R_max}')