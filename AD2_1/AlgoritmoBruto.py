import  math , copy

class RedSocialModeracion:
    def __init__(self, n_agentes, agentes, R_max):
        """
        Inicializa una instancia de RedSocialModeracion.

        Args:
            agentes (list): Lista de agentes, donde cada agente es una tupla (oRS, rRS).
                            oRS es la opinión del agente, y rRS es su receptividad.
            R_max (int): El esfuerzo máximo permitido para la moderación.
        """
        self.n_agentes = n_agentes
        self.agentes = agentes  # Lista de agentes con sus opiniones y receptividad
        self.R_max = R_max  # Esfuerzo máximo permitido
        self.n = len(agentes)  # Número de agentes

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
        for i in range(self.n):
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
        for i in range(self.n):
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

    def hallarMejorEstrategia(self):
        """
        Encuentra la mejor estrategia de moderación.

        Returns:
            tuple: La mejor estrategia y su nivel de extremismo.
        """
        unasEstrategias = self.generarEstrategias(self.n)
        laPropiaEstrategia = [[], self.calcularExtremismoRS(self.agentes), 0]

        for estrategia in unasEstrategias:
            if self.esEstrategiaAplicable(estrategia):
                nuevaRS = self.generarNuevaRS(estrategia)
                nuevoExtremismo = self.calcularExtremismoRS(nuevaRS)
                if nuevoExtremismo < laPropiaEstrategia[1]:
                    laPropiaEstrategia[0] = estrategia
                    laPropiaEstrategia[1] = nuevoExtremismo

        laPropiaEstrategia[2] = self.calcularEsfuerzo(laPropiaEstrategia[0])
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