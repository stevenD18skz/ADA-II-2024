import math, copy, time

class modexPD:
    """
    Implementación del algoritmo de mochila 0-1 para moderar agentes con opiniones extremas,
    optimizando la reducción del extremismo en una red social (RS).

    Atributos:
        n_agentes (int): Número de agentes en la red social.
        agentes (list): Lista de agentes representada como una lista de tuplas, 
                        donde cada tupla contiene la opinión del agente (float) y 
                        su receptividad (float).
        R_max (int): Esfuerzo máximo permitido para moderar a los agentes.

    Métodos:
        calcularEsfuerzo(unosAgentes, e):
            Calcula el esfuerzo total para moderar una lista de agentes con base en una 
            selección binaria dada.
        
        calcularExtremismoRS(unosAgentes):
            Calcula el extremismo de la red social como la raíz cuadrada de la suma de 
            los cuadrados de las opiniones de los agentes, normalizada por el número 
            de agentes.

        calcularExtremismoRS2(unosAgentes):
            Similar a `calcularExtremismoRS` pero ignora al primer agente.
        
        generarNuevaRS(unosAgentes, e):
            Genera una nueva red social con los agentes seleccionados moderados (su 
            opinión se vuelve 0).

        solucionar():
            Implementa el algoritmo de mochila 0-1 para encontrar la mejor selección de 
            agentes a moderar con el fin de minimizar el extremismo, considerando el esfuerzo 
            máximo permitido.
    """

    def __init__(self, RS):
        """
        Inicializa una instancia de RedSocialModeracion.

        Args:
            agentes (list): Lista de agentes, donde cada agente es una tupla (oRS, rRS).
                            oRS es la opinión del agente, y rRS es su receptividad.
            R_max (int): El esfuerzo máximo permitido para la moderación.
        """
        self.n_agentes = len(RS[0])
        self.agentes = RS[0]  # Lista de agentes con sus opiniones y receptividad
        self.R_max = RS[1]  # Esfuerzo máximo permitido

    def calcularEsfuerzo(self, unosAgentes, e):
        """
        Calcula el esfuerzo total necesario para moderar a los agentes seleccionados.

        Args:
            unosAgentes (list): Lista de agentes con sus opiniones y receptividades.
            e (list): Lista binaria indicando si el agente fue seleccionado para moderar (1) o no (0).

        Returns:
            int: El esfuerzo total requerido para moderar a los agentes seleccionados.
        """
        esfuerzo = 0
        for i in range(self.n_agentes):
            if (e[i] == 1):
                opinion_i = abs(unosAgentes[i][0])
                receptividad_i = (1 - unosAgentes[i][1])
                esfuerzo += math.ceil(opinion_i * receptividad_i)
        return esfuerzo

    def calcularExtremismoRS(self, unosAgentes):
        """
        Calcula el nivel de extremismo de una red social dada.

        Args:
            unosAgentes (list): Lista de agentes con sus opiniones.

        Returns:
            float: El nivel de extremismo en la red social.
        """
        suma = 0
        for i in range(self.n_agentes):
            opinion_i = unosAgentes[i][0]
            suma += math.pow(opinion_i, 2)
        raiz = math.pow(suma, 1/2)
        return raiz / self.n_agentes

    def calcularExtremismoRS2(self, unosAgentes):
        """
        Similar a `calcularExtremismoRS` pero omite el primer agente.

        Args:
            unosAgentes (list): Lista de agentes con sus opiniones.

        Returns:
            float: El nivel de extremismo en la red social (omitiendo al primer agente).
        """
        suma = 0
        for i in range(1, self.n_agentes):
            opinion_i = unosAgentes[i][0]
            suma += math.pow(opinion_i, 2)
        raiz = math.pow(suma, 1/2)
        return raiz / self.n_agentes

    def generarNuevaRS(self, unosAgentes, e):
        """
        Genera una nueva red social en la que los agentes seleccionados para moderación
        tienen su opinión cambiada a 0.

        Args:
            unosAgentes (list): Lista de agentes con sus opiniones.
            e (list): Lista binaria indicando si el agente fue seleccionado para moderar (1) o no (0).

        Returns:
            list: Nueva lista de agentes con opiniones actualizadas.
        """
        nuevosAgentes = copy.deepcopy(unosAgentes)
        for i in range(self.n_agentes):
            if e[i] == 1:
                nuevosAgentes[i][0] = 0
        return nuevosAgentes

    def solucionar(self):
        """
        Implementa el algoritmo de mochila 0-1 para encontrar la mejor combinación
        de agentes a moderar, de manera que se minimice el extremismo de la red social
        respetando el esfuerzo máximo permitido.

        Returns:
            list: La solución binaria que indica qué agentes moderar (1) o no (0),
                  el nuevo nivel de extremismo, y el esfuerzo total utilizado.
        """
        extremismoInicial = self.calcularExtremismoRS(self.agentes)

        def calcularEsfuerzoAgente(unAgente):
            opinion = abs(unAgente[0])
            receptividad = abs(unAgente[1])
            return math.ceil(opinion * (1 - receptividad))

        W = self.R_max
        solucion = [0 for _ in range(self.n_agentes)]
        V = [[0 for _ in range(W+1)] for _ in range(self.n_agentes+1)]

        for w in range(W):
            V[0][w] = 0

        for i in range(1, self.n_agentes):
            V[i][0] = 0

        for i in range(1, self.n_agentes+1):
            for w in range(W+1):
                pesoAgente_i = calcularEsfuerzoAgente(self.agentes[i-1])
                if pesoAgente_i <= w:
                    beneficioModerarAgente = pow(self.agentes[i-1][0], 2)
                    V[i][w] = max(beneficioModerarAgente + V[i-1][w-pesoAgente_i], V[i-1][w])
                else:
                    V[i][w] = V[i-1][w]

        i = self.n_agentes
        k = W

        while (i > 0 and k > 0):
            if V[i][k] != V[i-1][k]:
                solucion[i-1] = 1
                i = i-1
                k = k-calcularEsfuerzoAgente(self.agentes[i])
            else:
                i = i-1

        nuevaRS = self.generarNuevaRS(self.agentes, solucion)
        nuevoExtremismo = self.calcularExtremismoRS(nuevaRS)
        esfuerzoEstrategia = self.calcularEsfuerzo(self.agentes, solucion)
        
        return [solucion, nuevoExtremismo, esfuerzoEstrategia]
