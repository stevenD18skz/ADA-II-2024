import lector, math , copy, time

# Usando la estrategia de Mochila 0-1.
# El peso es el esfuerzo de moderar al agente.
# El beneficio se manejará de otra forma, ya no buscando el mejor beneficio (lo más alto), sino buscando el menor (el más bajo), pero el criterio de "beneficio" ahora será el extremismo de la RS si moderamos al agente.
# Al tener que guardar en cada posición cuáles agentes se moderaron y qué extremismo obtuvimos se hacen muchas operaciones lo cual no es óptimo y se tarda más.

n = lector.n_agentes
agentes = lector.agentes
R_max = lector.R_max
inicio = time.perf_counter()

def calcularEsfuerzo(unosAgentes, e):
    esfuerzo = 0
    for i in range(n):
        if (e[i] == 1):
            opinion_i = abs(unosAgentes[i][0])
            receptividad_i = (1 - unosAgentes[i][1])
            esfuerzo += math.ceil(opinion_i*receptividad_i)
    return esfuerzo

def calcularExtremismoRS(unosAgentes):
    suma = 0
    for i in range(n):
        opinion_i = unosAgentes[i][0]
        suma += math.pow(opinion_i, 2)
    raiz = math.pow(suma, 1/2)
    return raiz / n

def calcularExtremismoRS2(unosAgentes):
    suma = 0
    for i in range(1, n):
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

# Guardamos el extremismo de la RS actual para comparar luego
extremismoInicial = calcularExtremismoRS(agentes)

def calcularEsfuerzoAgente(unAgente):
    opinion = abs(unAgente[0])
    receptividad = abs(unAgente[1])
    return math.ceil(opinion * (1 - receptividad))

W = R_max

solucion = [0 for _ in range(n)]

def criterioCasilla():
    return {
        "extremismoObtenido": extremismoInicial,
        "agentesModerados": solucion.copy()
    }

V = [[criterioCasilla() for _ in range(W+1)] for _ in range(n+1)]

for w in range(W):
    V[0][w] = criterioCasilla()
for i in range(1, n):
    V[i][0] = criterioCasilla()
for i in range(1, n+1):
    for w in range(W+1):
        # elemento i puede ser parte de la solución
        pesoAgente_i = calcularEsfuerzoAgente(agentes[i-1])
        if pesoAgente_i <= w:
            resultadoSinPesoDisponible = V[i-1][w-pesoAgente_i]
            agentesModerados = resultadoSinPesoDisponible["agentesModerados"].copy()
            agentesModerados[i-1] = 1
            nuevaRS = generarNuevaRS(agentes, agentesModerados)
            extremismoModerandoAgente_i = calcularExtremismoRS(nuevaRS)

            if extremismoModerandoAgente_i < V[i-1][w]["extremismoObtenido"]:
                V[i][w] = {
                    "extremismoObtenido": extremismoModerandoAgente_i,
                    "agentesModerados": agentesModerados
                }
            else:
                V[i][w] = V[i-1][w]
        else:
            V[i][w] = V[i-1][w] # w_i > w

i = n
k = W

while (i > 0 and k > 0):
    if V[i][k] != V[i-1][k]:
        #marcamos que el item i está en la mochila
        solucion[i-1] = 1
        i = i-1
        k = k-calcularEsfuerzoAgente(agentes[i])
    else:
        i = i-1

nuevaRS = generarNuevaRS(agentes, solucion)
nuevoExtremismo = calcularExtremismoRS(nuevaRS)
esfuerzoEstrategia = calcularEsfuerzo(agentes, solucion)

fin = time.perf_counter()
duracion = fin - inicio

print("Dinamico?:")
print(f'La mejor estrategia es: {solucion}')
print(f'Con extremismo {nuevoExtremismo} en lugar de {extremismoInicial}')
print(f'Con esfuerzo de:  {esfuerzoEstrategia} debajo de {R_max}')
print(f'duracion: {duracion}')