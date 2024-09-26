from AlgoritmoDinamico import *
from math import ceil, sqrt


class modexV:
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


    def solucionar(self):
        beneficio_costo = [(0, 0, 0, 0)] * len(self.agentes)
        for i, (opinion_i, receptividad_i) in enumerate(self.agentes):
            beneficio = opinion_i ** 2
            costo = ceil(abs(opinion_i) * (1 - receptividad_i))
            ratio = beneficio / max(costo, 1)
            beneficio_costo[i] = (ratio, i, beneficio, costo)

        beneficio_costo.sort(reverse=True, key=lambda x: x[0])

        esfuerzo_total = 0
        estrategia = [0] * len(self.agentes)

        suma = 0
        for ratio, i, beneficio, costo in beneficio_costo:
            if esfuerzo_total + costo <= self.R_max:
                estrategia[i] = 1
                esfuerzo_total += costo

            else:
                suma += beneficio


        raiz = sqrt(suma)
        extremismo =  raiz / len(self.agentes)
        return [estrategia, extremismo, esfuerzo_total]