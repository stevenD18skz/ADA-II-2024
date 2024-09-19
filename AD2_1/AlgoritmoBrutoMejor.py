import lector, math , copy, time

# Generamos todas las posibles estrategias.
# No tenemos en cuenta las que vayan excediendo el esfuerzo disponible.
# Vamos mirando cuál es mejor, eliminando las que vamos revisando.

n = lector.n_agentes
agentes = lector.agentes
R_max = lector.R_max
Estrategias = []
inicio = time.perf_counter()

def generarEstrategia(e, n, costo):
    if costo <= R_max:
        if n == 0:
            Estrategias.append(e)
        else:
            e_0 = e.copy()
            e_1 = e.copy()
            e_0.append(0)
            e_1.append(1)
            generarEstrategia(e_0, n-1, costo)
            indice = len(e)
            agente = agentes[indice]
            costoAgente = calcularEsfuerzoAgente(agente)
            generarEstrategia(e_1, n-1, costo + costoAgente)

def calcularEsfuerzo(unosAgentes, e):
    esfuerzo = 0
    for i in range(len(e)):
        if (e[i] == 1):
            opinion_i = abs(unosAgentes[i][0])
            receptividad_i = (1 - unosAgentes[i][1])
            esfuerzo += math.ceil(opinion_i*receptividad_i)
    return esfuerzo

def calcularEsfuerzoAgente(unAgente):
    opinion = abs(unAgente[0])
    receptividad = abs(unAgente[1])
    return math.ceil(opinion * (1 - receptividad))

def calcularExtremismoRS(unosAgentes):
    suma = 0
    for i in range(n):
        opinion_i = unosAgentes[i][0]
        suma += math.pow(opinion_i, 2)
    raiz = math.pow(suma, 1/2)
    return raiz / n

def generarNuevaRS(unosAgentes, e):
    nuevosAgentes = copy.deepcopy(unosAgentes)
    for i in range(n):
        if e[i] == 1:
            nuevosAgentes[i][0] = 0
    return nuevosAgentes

from collections import deque

def hallarMejorEstrategia(unosAgentes):
    strategies = deque(Estrategias)
    while strategies:
        estrategia = strategies.popleft()
        esfuerzoEstrategia = calcularEsfuerzo(unosAgentes, estrategia)
        if esfuerzoEstrategia <= R_max:  # La estrategia es aplicable
            nuevaRS = generarNuevaRS(unosAgentes, estrategia)
            nuevoExtremismo = calcularExtremismoRS(nuevaRS)
            if nuevoExtremismo < laPropiaEstrategia[1]:
                laPropiaEstrategia[0] = estrategia
                laPropiaEstrategia[1] = nuevoExtremismo

# Generamos todas las posibles estrategias combinando 0's y 1's en arreglos de tamaño n, obteniendo 2^n estrategias diferentes
generarEstrategia([], n, 0)

# Guardamos el extremismo de la RS actual para comparar luego
extremismoInicial = calcularExtremismoRS(agentes)

# Vamos guardando la estrategia que sea aplicable y tenga un extremismo menor al actual
laPropiaEstrategia = [[], extremismoInicial, 0]     # [estrategia , extremismo]

hallarMejorEstrategia(agentes)
fin = time.perf_counter()

print("BrutoMejor:")
if (laPropiaEstrategia[0] != []):
    print(f'La mejor estrategia es: {laPropiaEstrategia[0]}')
    print(f'Con extremismo {laPropiaEstrategia[1]} en lugar de {extremismoInicial}')
    print(f'Con esfuerzo de:  {calcularEsfuerzo(agentes, laPropiaEstrategia[0])} debajo de {R_max}')
else:
    print(f'No hay ninguna estrategia aplicable o que genere menos extremismo que {extremismoInicial}')
duracion = fin - inicio
print(f'duracion: {duracion}')