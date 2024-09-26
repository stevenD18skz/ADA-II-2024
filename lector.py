import os


def ALFile(n = 1, ruta_archivo = ""):
    if ruta_archivo == "":
        ruta_script = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_script, 'Entradas', f'Prueba{n}.txt')

    with open(ruta_archivo, 'r') as archivo:
        n_agentes = int(archivo.readline().strip())
        agentes = []
        
        for _ in range(n_agentes):
            linea = archivo.readline().strip()
            entero, real = linea.split(',')
            agentes.append([int(entero), float(real)])
        
        R_max = int(archivo.readline().strip())
    
    return [n_agentes, agentes, R_max]