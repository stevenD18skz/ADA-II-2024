import lector, math , copy, time

# Generamos todas las posibles estrategias.
# No tenemos en cuenta las que vayan excediendo el esfuerzo disponible.
# Vamos calculandole el extremismo que llegaría a tener la nueva RS si aplicamos lo que va de la estrategia, y al final lo guardamos, tendríamos tuplas de [estrategia, extremismoSiSeUsaLaEstrategia]
# Al revisar, miramos de cada una con cuál estrategia obtenemos el menor extremismo (valor que está en la tupla), en lugar de calcular de nuevo el extremismo para cada estrategia candidata que tengamos.

n = lector.n_agentes
agentes = lector.agentes
R_max = lector.R_max
Estrategias = []
inicio = time.perf_counter()

def generarEstrategia(e, n, costo, subExtremismo):
    if costo <= R_max:
        if n == 0:
            Estrategias.append([e, subExtremismo])
        else:
            e_0 = e.copy()
            e_1 = e.copy()
            e_0.append(0)
            e_1.append(1)
            indice = len(e)
            agente = agentes[indice]
            subExtremismoAdicional = pow(agente[0], 2)
            generarEstrategia(e_0, n-1, costo, subExtremismo + subExtremismoAdicional)
            costoAgente = math.ceil(abs(agente[0]) * (1 - agente[1]))
            generarEstrategia(e_1, n-1, costo + costoAgente, subExtremismo)

def calcularEsfuerzo(unosAgentes, e):
    esfuerzo = 0
    for i in range(len(e)):
        if (e[i] == 1):
            opinion_i = abs(unosAgentes[i][0])
            receptividad_i = (1 - unosAgentes[i][1])
            esfuerzo += math.ceil(opinion_i*receptividad_i)
    return esfuerzo

# Generamos todas las posibles estrategias combinando 0's y 1's en arreglos de tamaño n, obteniendo 2^n estrategias diferentes
generarEstrategia([], n, 0, 0)

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

def hallarMejorEstrategia():
    strategies = deque(Estrategias)
    #while len(unasEstrategias) > 0:
    while strategies:
        estrategia = strategies.popleft()
        unaSolucion = estrategia[0]
        nuevoExtremismo = estrategia[1]
        if nuevoExtremismo < laPropiaEstrategia[1]:
            laPropiaEstrategia[0] = unaSolucion
            laPropiaEstrategia[1] = nuevoExtremismo

# Guardamos el extremismo de la RS actual para comparar luego
extremismoInicial = calcularExtremismoRS(agentes)

# Vamos guardando la estrategia que sea aplicable y tenga un extremismo menor al maximo posible
laPropiaEstrategia = [[], pow(100,2)*n]     # [estrategia , extremismoMaximo]

hallarMejorEstrategia()
fin = time.perf_counter()

#aplicamos la formula real del extremismo
nuevoExtremismo = math.pow(laPropiaEstrategia[1], 1/2)/n
esfuerzoUsado = calcularEsfuerzo(agentes, laPropiaEstrategia[0])

print("BrutoMasMejor:")
if (laPropiaEstrategia[0] != []):
    print(f'La mejor estrategia es: {laPropiaEstrategia[0]}')
    print(f'Con extremismo {nuevoExtremismo} en lugar de {extremismoInicial}')
    print(f'Con esfuerzo de:  {esfuerzoUsado} debajo de {R_max}')
else:
    print(f'No hay ninguna estrategia aplicable o que genere menos extremismo que {extremismoInicial}')
duracion = fin - inicio
print(f'duracion: {duracion}')