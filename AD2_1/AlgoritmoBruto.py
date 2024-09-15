import lector, math , copy

n = lector.n_agentes
agentes = lector.agentes
R_max = lector.R_max
Estrategias = []

def generarEstrategia(e, n):
    if n == 0:
        Estrategias.append(e)
    else:
        e_0 = e.copy()
        e_1 = e.copy()
        e_0.append(0)
        e_1.append(1)
        generarEstrategia(e_0, n-1)
        generarEstrategia(e_1, n-1)

# Generamos todas las posibles estrategias combinando 0's y 1's en arreglos de tamaño n, obteniendo 2^n estrategias diferentes

generarEstrategia([], n)

def calcularEsfuerzo(unosAgentes, e):
    esfuerzo = 0
    for i in range(n):
        if (e[i] == 1):
            opinion_i = abs(unosAgentes[i][0])
            receptividad_i = (1 - unosAgentes[i][1])
            esfuerzo += math.ceil(opinion_i*receptividad_i)
    return esfuerzo

""" def esEstrategiaAplicable(unosAgentes, e):
    esfuerzo = calcularEsfuerzo(unosAgentes, e)
    return (esfuerzo <= R_max) """

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

""" def hallarMejorEstrategia(unasEstrategias, unosAgentes):
    for estrategia in unasEstrategias:
        if esEstrategiaAplicable(unosAgentes, estrategia):
            nuevaRS = generarNuevaRS(unosAgentes, estrategia)
            nuevoExtremismo = calcularExtremismoRS(nuevaRS)
            if nuevoExtremismo < laPropiaEstrategia[1]:
                laPropiaEstrategia[0] = estrategia
                laPropiaEstrategia[1] = nuevoExtremismo """

def hallarMejorEstrategia(unasEstrategias, unosAgentes):
    for estrategia in unasEstrategias:
        esfuerzoEstrategia = calcularEsfuerzo(unosAgentes, estrategia)
        if esfuerzoEstrategia <= R_max:  # La estrategia es aplicable
            nuevaRS = generarNuevaRS(unosAgentes, estrategia)
            nuevoExtremismo = calcularExtremismoRS(nuevaRS)
            if nuevoExtremismo < laPropiaEstrategia[1]:
                laPropiaEstrategia[0] = estrategia
                laPropiaEstrategia[1] = nuevoExtremismo

# Guardamos el extremismo de la RS actual para comparar luego
extremismoInicial = calcularExtremismoRS(agentes)

# Vamos guardando la estrategia que sea aplicable y tenga un extremismo menor al actual
laPropiaEstrategia = [[], extremismoInicial, 0]     # [estrategia , extremismo , esfuerzo]

hallarMejorEstrategia(Estrategias, agentes)

print(f'La mejor estrategia es: {laPropiaEstrategia[0]}')
print(f'Con extremismo {laPropiaEstrategia[1]} en lugar de {extremismoInicial}')
print(f'Con esfuerzo de:  {calcularEsfuerzo(agentes, laPropiaEstrategia[0])} debajo de {R_max}')

#Mostrar:
"""
Extremismo RS salida
Esfuerzo
mod0  # mostrar la opinión de cada agente
mod1
mod2
.
mod(n-1)
"""