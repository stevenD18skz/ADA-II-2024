import  math , copy, lector
from pprint import pprint

class RedSocialModeracionVoraz:
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

    def algoritmo_voraz(self):
        # Paso 1: Crear una lista de beneficio/costo para cada agente
        self.agentes2 =  [
            [50, 0.9],   # Agente 1: opinión 50, receptividad 0.9
            [-75, 0.5],  # Agente 2: opinión -75, receptividad 0.5
            [20, 0.2],   # Agente 3: opinión 20, receptividad 0.2
            [-40, 0.8],  # Agente 4: opinión -40, receptividad 0.8
            [30, 0.3],   # Agente 5: opinión 30, receptividad 0.3
            [10, 0.3],  
            [50, 0.3],  
            [90, 0.3],  
            [50, 0.1],  
            [50, 0.5],  
            [50, 0.9],  
            [100, 1],  
        ]

        beneficio_costo = []
        for i in range(len(self.agentes)):
            opinion_i = self.agentes[i][0]
            receptividad_i = self.agentes[i][1]
            # Beneficio: reducción en el extremismo si la opinión es moderada a 0
            beneficio = opinion_i ** 2
            # Costo: esfuerzo de moderar la opinión, influido por la receptividad
            costo = abs(opinion_i) * (1 - receptividad_i)
            #print(f"{abs(opinion_i)} {receptividad_i} {(1 - receptividad_i)} {costo}")
            ratio = beneficio / (costo if costo > 0 else 1)
            beneficio_costo.append((ratio, i, beneficio, costo))
        
        
        beneficio_costo.sort(reverse=True, key=lambda x: x[0])

        # Paso 3: Moderar agentes hasta agotar el presupuesto de esfuerzo
        esfuerzo_total = 0
        estrategia = [0] * len(self.agentes)  # Inicia sin moderar a nadie
        
        for ratio, i, beneficio, costo in beneficio_costo:
            if esfuerzo_total + costo <= self.R_max:
                estrategia[i] = 1  # Moderamos al agente i
                esfuerzo_total += costo

        # Paso 4: Devolver la estrategia final y el extremismo resultante
        nueva_red = self.generarNuevaRS(estrategia)
        extremismo_final = self.calcularExtremismoRS(nueva_red)

        solucion = [estrategia, extremismo_final, esfuerzo_total]
        print(f"termine {solucion}")
        return solucion


        #pprint(beneficio_costo)
        #print("\n".join([f"Ratio: {item[0]:.2f}, Index: {item[1]}, Beneficio: {item[2]:.2f}, Costo: {item[3]:.4f}" for item in beneficio_costo]))








