import os


def ALFile(n = 1, ruta_archivo = ""):
    """
    Lee los datos de un archivo de entrada y los estructura para su uso en el modelo de red social.

    Args:
        n (int): Número de archivo de prueba a leer si no se especifica una ruta. Por defecto es 1.
        ruta_archivo (str): Ruta completa al archivo de entrada. Si no se proporciona, se buscará
                            en la carpeta 'Entradas' dentro del directorio del script, con el nombre 
                            'Prueba{n}.txt'.

    Returns:
        list: Una lista con tres elementos:
              - n_agentes (int): Número de agentes en el sistema.
              - agentes (list): Una lista de agentes, donde cada agente es una lista [entero, real].
                                'entero' es la opinión (un número entero) y 'real' es la receptividad 
                                (un número flotante).
              - R_max (int): El esfuerzo máximo permitido para la moderación.
    """
    if ruta_archivo == "":
        ruta_script = os.path.dirname(os.path.abspath(__file__))  # Obtiene el directorio del script actual
        ruta_archivo = os.path.join(ruta_script, 'Entradas', f'Prueba{n}.txt')  # Construye la ruta del archivo de entrada

    with open(ruta_archivo, 'r') as archivo:
        n_agentes = int(archivo.readline().strip())  # Lee el número de agentes de la primera línea
        agentes = []
        
        # Lee cada agente de las siguientes líneas
        for _ in range(n_agentes):
            linea = archivo.readline().strip()
            entero, real = linea.split(',')  # Separa la línea en entero y real
            agentes.append([int(entero), float(real)])  # Agrega el agente a la lista

        R_max = int(archivo.readline().strip())  # Lee el valor de esfuerzo máximo permitido de la última línea
    
    return [n_agentes, agentes, R_max]  # Devuelve el número de agentes, la lista de agentes y el esfuerzo máximo
