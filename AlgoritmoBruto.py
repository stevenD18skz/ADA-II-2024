import  math , copy

class modexFB:
    def __init__(self, RS):
        """
        Inicializa una instancia de RedSocialModeracion.

        Args:
            agentes (list): Lista de agentes, donde cada agente es una tupla (oRS, rRS).
                            oRS es la opinión del agente, y rRS es su receptividad.
            R_max (int): El esfuerzo máximo permitido para la moderación.
        """
        self.n_agentes = len(RS[0]) #numero total de agentes en la red social
        self.agentes = RS[0]  # Lista de agentes con sus opiniones y receptividad
        self.R_max = RS[1]  # Esfuerzo máximo permitido



    def generarEstrategias(self, n):
        """
        Genera todas las posibles estrategias de moderación.

        Args:
            n (int): Número de agentes.

        Returns:
            list: Lista de todas las posibles estrategias de moderación (listas binarias).
        """
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



    def calcularExtremismoRS(self, unosAgentes):
        """
        Calcula el nivel de extremismo de una red social.

        Args:
            unosAgentes (list): Lista de agentes, donde cada agente es una tupla (oRS, rRS).

        Returns:
            float: El nivel de extremismo de la red social.
        """
        suma = sum(list(map(lambda x: math.pow(x[0], 2), unosAgentes)))
        raiz = math.pow(suma, 1/2)
        return raiz / len(unosAgentes)



    def calcularEsfuerzo(self, e):
        """
        Calcula el esfuerzo total de moderación para una estrategia.

        Args:
            e (list): Lista binaria que representa la estrategia de moderación.

        Returns:
            int: El esfuerzo total necesario para aplicar la estrategia.
        """
        esfuerzo = 0
        for i in range(self.n_agentes):
            if e[i] == 1:
                opinion_i = abs(self.agentes[i][0])
                receptividad_i = (1 - self.agentes[i][1])
                esfuerzo += math.ceil(opinion_i * receptividad_i)
        return esfuerzo



    def generarNuevaRS(self, e):
        """
        Genera una nueva red social a partir de la red original aplicando una estrategia de moderación.

        Args:
            e (list): Lista binaria que representa la estrategia de moderación.

        Returns:
            list: Nueva lista de agentes, donde las opiniones de los agentes moderados han sido cambiadas a 0.
        """
        nuevosAgentes = copy.deepcopy(self.agentes)
        for i in range(self.n_agentes):
            if e[i] == 1:
                nuevosAgentes[i][0] = 0
        return nuevosAgentes



    def esEstrategiaAplicable(self, e):
        """
        Verifica si una estrategia de moderación es aplicable.

        Args:
            e (list): Lista binaria que representa la estrategia de moderación.

        Returns:
            bool: True si la estrategia es aplicable, False en caso contrario.
        """
        esfuerzo = self.calcularEsfuerzo(e)
        return esfuerzo <= self.R_max



    def solucionar(self):
        """
        Encuentra la mejor estrategia de moderación.

        Returns:
            tuple: La mejor estrategia y su nivel de extremismo.
        """
        unasEstrategias = self.generarEstrategias(self.n_agentes)
        laPropiaEstrategia = [[], self.calcularExtremismoRS(self.agentes), 0]

        for estrategia in unasEstrategias:
            if self.esEstrategiaAplicable(estrategia):
                nuevaRS = self.generarNuevaRS(estrategia)
                nuevoExtremismo = self.calcularExtremismoRS(nuevaRS)
                if nuevoExtremismo < laPropiaEstrategia[1]:
                    laPropiaEstrategia[0] = estrategia
                    laPropiaEstrategia[1] = nuevoExtremismo

        laPropiaEstrategia[2] = self.calcularEsfuerzo(laPropiaEstrategia[0])
        return laPropiaEstrategia #estrategia, extermismoResultannte, Exfuerzo