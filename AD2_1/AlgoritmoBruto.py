import lector, math , copy



def generarEstrategias(n):
    def generarEstrategia(e, n):
        if n == 0:
            return [e]
        else:
            e_0 = e.copy()
            e_1 = e.copy()
            e_0.append(0)
            e_1.append(1)
            return generarEstrategia(e_0, n-1) + generarEstrategia(e_1, n-1)

    return generarEstrategia([], n)





def calcularExtremismoRS(unosAgentes):
    """
    Calcula el nivel de extremismo de una red social.

    El nivel de extremismo se define como la raíz cuadrada de la suma de los cuadrados
    de las opiniones de los agentes, dividida entre el número total de agentes.

    Args:
        unosAgentes (list): Lista de agentes, donde cada agente es una tupla (oRS, rRS).
                            oRS es la opinión del agente, y rRS es su receptividad.

    Returns:
        float: El nivel de extremismo de la red social, calculado como la raíz cuadrada
               de la suma de los cuadrados de las opiniones, dividido por el número de agentes.
    """
    suma = sum(list(map(lambda x: math.pow(x[0], 2), unosAgentes)))
    raiz = math.pow(suma, 1/2)
    return raiz / len(unosAgentes)





def calcularEsfuerzo(unosAgentes, e):
    """
    Calcula el esfuerzo total de moderación para una red social dada una estrategia de moderación.

    Args:
        unosAgentes (list): Lista de agentes, donde cada agente es una tupla (oRS, rRS).
                            oRS es la opinión del agente, y rRS es su receptividad.
        e (list): Lista binaria que representa la estrategia de moderación.
                  Un valor de 1 en la posición i indica que el agente i será moderado,
                  mientras que un valor de 0 indica que no lo será.

    Returns:
        int: Esfuerzo total necesario para aplicar la estrategia de moderación a la red social,
             calculado como el producto entre la magnitud de la opinión del agente y su receptividad
             restada de 1, redondeado hacia arriba.
    """
    esfuerzo = 0
    for i in range(n):
        if (e[i] == 1):
            opinion_i = abs(unosAgentes[i][0])
            receptividad_i = (1 - unosAgentes[i][1])
            esfuerzo += math.ceil(opinion_i*receptividad_i)
    return esfuerzo





def generarNuevaRS(unosAgentes, e):
    """
    Genera una nueva red social a partir de la red original, aplicando una estrategia de moderación.

    Los agentes cuya estrategia de moderación es 1 tendrán su opinión reducida a 0.

    Args:
        unosAgentes (list): Lista de agentes, donde cada agente es una tupla (oRS, rRS).
                            oRS es la opinión del agente, y rRS es su receptividad.
        e (list): Lista binaria que representa la estrategia de moderación.
                  Un valor de 1 en la posición i indica que el agente i será moderado,
                  mientras que un valor de 0 indica que no lo será.

    Returns:
        list: Nueva lista de agentes, donde las opiniones de los agentes moderados
              han sido cambiadas a 0.
    """
    nuevosAgentes = copy.deepcopy(unosAgentes)
    for i in range(n):
        if e[i] == 1:
            nuevosAgentes[i][0] = 0
    return nuevosAgentes





def esEstrategiaAplicable(unosAgentes, e):
    """
    Verifica si una estrategia de moderación es aplicable a la red social.

    La estrategia es aplicable si el esfuerzo total necesario para aplicarla es menor
    o igual a un valor máximo de esfuerzo permitido (R_max).

    Args:
        unosAgentes (list): Lista de agentes, donde cada agente es una tupla (oRS, rRS).
                            oRS es la opinión del agente, y rRS es su receptividad.
        e (list): Lista binaria que representa la estrategia de moderación.
                  Un valor de 1 en la posición i indica que el agente i será moderado,
                  mientras que un valor de 0 indica que no lo será.

    Returns:
        bool: True si la estrategia es aplicable (el esfuerzo es menor o igual a R_max),
              False en caso contrario.
    """
    esfuerzo = calcularEsfuerzo(unosAgentes, e)
    return (esfuerzo <= R_max) 





def hallarMejorEstrategia(unosAgentes):
    """
    Encuentra la mejor estrategia de moderación entre una lista de estrategias aplicables.

    La mejor estrategia es aquella que minimiza el nivel de extremismo de la red social,
    siempre y cuando el esfuerzo para aplicarla sea menor o igual a R_max.

    Args:
        unasEstrategias (list): Lista de posibles estrategias de moderación.
                                Cada estrategia es una lista binaria donde 1 indica que el
                                agente será moderado y 0 que no lo será.
        unosAgentes (list): Lista de agentes, donde cada agente es una tupla (oRS, rRS).
                            oRS es la opinión del agente, y rRS es su receptividad.

    Returns:
        tuple: Una tupla que contiene la mejor estrategia (lista binaria) y su nivel de extremismo.
               Si no se encuentra ninguna estrategia aplicable, retorna None.
    """

    unasEstrategias = generarEstrategias(len(unosAgentes))
    laPropiaEstrategia = [[], calcularExtremismoRS(unosAgentes), 0]     # [estrategia , extremismo , esfuerzo]

    for estrategia in unasEstrategias:
        if esEstrategiaAplicable(unosAgentes, estrategia):
            nuevaRS = generarNuevaRS(unosAgentes, estrategia)
            nuevoExtremismo = calcularExtremismoRS(nuevaRS)
            if nuevoExtremismo < laPropiaEstrategia[1]:
                laPropiaEstrategia[0] = estrategia
                laPropiaEstrategia[1] = nuevoExtremismo 
    
    laPropiaEstrategia[2] = calcularEsfuerzo(unosAgentes, laPropiaEstrategia[0])
    
    return laPropiaEstrategia




"""
n, agentes, R_max = lector.ALFile()
laPropiaEstrategia = hallarMejorEstrategia(agentes)



def escribirSalida():
    # Abrir (o crear) un archivo llamado "salida.txt" en modo escritura ('w')
    with open('./AD2_1/salida.txt', 'w') as file:
        # Escribir las líneas en el archivo
        file.write(f'{laPropiaEstrategia[1]}\n')#extremismo
        file.write(f'{laPropiaEstrategia[2]}\n')#Exfuerzo
        list(map(lambda x: file.write(f"{x}\n"), laPropiaEstrategia[0]))# Escribir la estrategia en el archivo usando map y lambda






print(f"                    ===> INICIALIZACION DEL PROBLEMA <===")
print(f'n: {n}')
print(f'Parejas: {agentes}')
print(f'Último número: {R_max}')
print(f'Extremismo inicial: {calcularExtremismoRS(agentes)}')
print(f"\n\n                    ===> RESULTADOS DEL PROBLEMA <===")
print(f'La mejor estrategia es: {laPropiaEstrategia[0]}')
print(f'Con extremismo {laPropiaEstrategia[1]}')
print(f'Con esfuerzo de: {calcularEsfuerzo(agentes, laPropiaEstrategia[0])} debajo de (<=) {R_max}')
"""