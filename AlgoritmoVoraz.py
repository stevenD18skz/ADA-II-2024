from AlgoritmoDinamico import *
from math import ceil, sqrt


class modexV:
    def __init__(self, RS):
        """
        Inicializa una instancia de la clase modexV, que modela un sistema de moderación de agentes
        dentro de una red social.

        Args:
            RS (tuple): Una tupla con dos elementos:
                        - RS[0] es una lista de agentes, donde cada agente es una tupla (oRS, rRS),
                          siendo oRS la opinión del agente (valor entre -1 y 1) y rRS la receptividad 
                          del agente (valor entre 0 y 1).
                        - RS[1] es el esfuerzo máximo permitido (R_max) para la moderación.
        """
        self.n_agentes = len(RS[0])  # Número de agentes en la red
        self.agentes = RS[0]  # Lista de agentes con sus opiniones y receptividad
        self.R_max = RS[1]  # Esfuerzo máximo permitido para la moderación

    def solucionar(self):
        """
        Determina una estrategia de moderación que maximiza el beneficio en la red social, 
        dado un límite de esfuerzo total, y calcula el extremismo resultante de la red.

        Este método realiza lo siguiente:
        1. Calcula una lista de tuplas (ratio, índice, beneficio, costo) para cada agente.
           - El ratio se calcula como el beneficio dividido por el costo.
           - El beneficio es la opinión del agente elevada al cuadrado.
           - El costo es una función de la opinión y receptividad del agente.
        2. Ordena a los agentes por su ratio de beneficio/costo en orden descendente.
        3. Selecciona los agentes para moderar, sin exceder el esfuerzo máximo permitido (R_max).
        4. Calcula el extremismo de la red basado en los agentes no moderados.

        Returns:
            list: Una lista con tres elementos:
                  - estrategia (list): Una lista binaria donde el valor 1 indica que el agente fue
                                       seleccionado para moderación, y 0 indica que no lo fue.
                  - extremismo (float): El nivel de extremismo en la red social, calculado como la raíz 
                                        cuadrada de la suma de los beneficios de los agentes no moderados,
                                        dividido por el número total de agentes.
                  - esfuerzo_total (int): El esfuerzo total utilizado en la moderación.
        """
        beneficio_costo = [(0, 0, 0, 0)] * len(self.agentes)  # Inicializa lista de ratios (beneficio/costo)
        
        # Calcula beneficio, costo y ratio para cada agente
        for i, (opinion_i, receptividad_i) in enumerate(self.agentes):
            beneficio = opinion_i ** 2  # Beneficio es el cuadrado de la opinión
            costo = ceil(abs(opinion_i) * (1 - receptividad_i))  # Costo es una función de opinión y receptividad
            ratio = beneficio / max(costo, 1)  # Ratio de beneficio/costo, con un costo mínimo de 1 para evitar división por cero
            beneficio_costo[i] = (ratio, i, beneficio, costo)

        # Ordena los agentes por su ratio beneficio/costo de mayor a menor
        beneficio_costo.sort(reverse=True, key=lambda x: x[0])

        print(self.agentes)
        print(beneficio_costo)

        esfuerzo_total = 0  # Esfuerzo acumulado en la moderación
        estrategia = [0] * len(self.agentes)  # Estrategia inicial: ningún agente está moderado

        suma = 0  # Beneficio acumulado de los agentes no moderados

        # Selecciona los agentes para moderación, sin exceder el esfuerzo máximo permitido (R_max)
        for ratio, i, beneficio, costo in beneficio_costo:
            if esfuerzo_total + costo <= self.R_max:
                estrategia[i] = 1  # Se selecciona el agente para moderación
                esfuerzo_total += costo  # Se acumula el esfuerzo utilizado
            else:
                suma += beneficio  # Se acumula el beneficio de los agentes no moderados

        # Calcula el extremismo como la raíz cuadrada de la suma de beneficios de los no moderados
        raiz = sqrt(suma)
        extremismo = raiz / len(self.agentes)  # Normaliza el extremismo por el número total de agentes
        
        return [estrategia, extremismo, esfuerzo_total]  # Devuelve la estrategia, extremismo y esfuerzo total
