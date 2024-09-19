import lector, math , copy, time

# Usando la estrategia de Mochila 0-1.
# El peso es el esfuerzo de moderar al agente.
# El beneficio es la opinión del agente al cuadrado, para observar mejor qué tanta cantidad de "opinión" nos quitamos, lo cual beneficia al hecho de tener menos extremismo al final.
# Al tener un criterio más simple que el otro "AlgoritmoDinamicoPeor" se recorre la matriz más rápido y al final el algoritmo es más eficiente en tiempo.

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

V = [[0 for _ in range(W+1)] for _ in range(n+1)]

for w in range(W):
    V[0][w] = 0
for i in range(1, n):
    V[i][0] = 0
for i in range(1, n+1):
    for w in range(W+1):
        # elemento i puede ser parte de la solución
        pesoAgente_i = calcularEsfuerzoAgente(agentes[i-1])
        if pesoAgente_i <= w:
            beneficioModerarAgente = pow(agentes[i-1][0], 2)
            if beneficioModerarAgente + V[i-1][w-pesoAgente_i] > V[i-1][w]:
                V[i][w] = beneficioModerarAgente + V[i-1][w-pesoAgente_i]
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