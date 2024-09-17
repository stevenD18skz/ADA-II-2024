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
        # Paso 1: Crear una lista de beneficio/costo para cada agente (cuales nso conviene mas moderar)
        self.agentes2 =  [ # array de prueba
            [50, 0.9],   
            [-75, 0.5], 
            [20, 0.2],   
            [-40, 0.8],  
            [30, 0.3],   
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
        
        # Paso 2: organizar los agentes de mayor a menor dependiendo de su valor beneficio
        beneficio_costo.sort(reverse=True, key=lambda x: x[0])

        # Paso 3: Moderar agentes hasta agotar el presupuesto de esfuerzo
        esfuerzo_total = 0
        estrategia = [0] * len(self.agentes) 
        
        for ratio, i, beneficio, costo in beneficio_costo:
            if esfuerzo_total + costo <= self.R_max:
                estrategia[i] = 1  # Moderamos al agente i => la posisicon de este agente en el array original
                esfuerzo_total += costo

        # Paso 4: Devolver la estrategia final y el extremismo resultante
        nueva_red = self.generarNuevaRS(estrategia)
        extremismo_final = self.calcularExtremismoRS(nueva_red)

        solucion = [estrategia, extremismo_final, esfuerzo_total]
        #print(f"termine {solucion}")
        return solucion


        #pprint(beneficio_costo)
        #print("\n".join([f"Ratio: {item[0]:.2f}, Index: {item[1]}, Beneficio: {item[2]:.2f}, Costo: {item[3]:.4f}" for item in beneficio_costo]))





"""
valores_p = [5.8, 21.557, 11.724, 15.717, 9.678, 11.481, 0, 3.652, 5.933, 2.419, 5.65, 4.037, 4.455, 4.24, 1.319, 1.727, 1.406, 3.955, 0.901, 1.406, 2.629, 1.524, 1.927, 0.973, 0.97, 0.815, 0.373, 0.786, 1.17, 0.309]

print("{:<12} | {:<12} | {:<17} | {:<10} | {:<10}".format("Prueba", "N. Agentes", "Valor Solución", "Solución profe", "diferencias"))

for i in range(1, 31):
    n_agentes, agentes, R_max = lector.ALFile(n=i)
    solucionVoraz = RedSocialModeracionVoraz(n_agentes, agentes, R_max)
    r = solucionVoraz.algoritmo_voraz()
    print("{:<12} | {:<12} | {:<17.9f} | {:<10} | {:<10}".format(f"Prueba{i}.txt", n_agentes, r[1], valores_p[i-1], 111 if valores_p[i-1] >= r[1] else 333))


Prueba       | N. Agentes   | Valor Solución    | Solución profe | diferencias
Prueba1.txt  | 5            | 5.800000000       | 5.8        | ✔✔✔       
Prueba2.txt  | 5            | 21.557365331      | 21.557     | ✔✔✔       
Prueba3.txt  | 10           | 11.724333670      | 11.724     | ✔✔✔     
Prueba4.txt  | 10           | 15.717506164      | 15.717     | ✔✔✔       
Prueba5.txt  | 20           | 9.697551237       | 9.678      | ✘✘✘       
Prueba6.txt  | 20           | 11.518788999      | 11.481     | ✘✘✘       
Prueba7.txt  | 35           | 0.000000000       | 0          | ✔✔✔       
Prueba8.txt  | 50           | 3.583350388       | 3.652      | ✔✔✔       
Prueba9.txt  | 50           | 5.839897259       | 5.933      | ✔✔✔       
Prueba10.txt | 100          | 2.358304476       | 2.419      | ✔✔✔       
Prueba11.txt | 100          | 5.622935177       | 5.65       | ✔✔✔       
Prueba12.txt | 125          | 4.010937048       | 4.037      | ✔✔✔       
Prueba13.txt | 125          | 4.424311020       | 4.455      | ✔✔✔       
Prueba14.txt | 150          | 4.224552573       | 4.24       | ✔✔✔       
Prueba15.txt | 200          | 1.279521395       | 1.319      | ✔✔✔       
Prueba16.txt | 200          | 1.687631476       | 1.727      | ✔✔✔       
Prueba17.txt | 300          | 1.381553071       | 1.406      | ✔✔✔       
Prueba18.txt | 300          | 3.943654537       | 3.955      | ✔✔✔       
Prueba19.txt | 350          | 0.862667907       | 0.901      | ✔✔✔       
Prueba20.txt | 400          | 1.385911253       | 1.406      | ✔✔✔       
Prueba21.txt | 500          | 2.614770353       | 2.629      | ✔✔✔       
Prueba22.txt | 500          | 1.508879054       | 1.524      | ✔✔✔
Prueba23.txt | 750          | 1.915931337       | 1.927      | ✔✔✔
Prueba24.txt | 750          | 0.955317283       | 0.973      | ✔✔✔       
Prueba25.txt | 800          | 0.954773370       | 0.97       | ✔✔✔
Prueba26.txt | 1000         | 0.763475605       | 0.815      | ✔✔✔
Prueba27.txt | 1500         | 0.289319508       | 0.373      | ✔✔✔
Prueba28.txt | 1500         | 0.762445481       | 0.786      | ✔✔✔       
Prueba29.txt | 2000         | 1.146792483       | 1.17       | ✔✔✔
Prueba30.txt | 2500         | 0.233969229       | 0.309      | ✔✔✔ 
"""

