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


    def calcularExtremismoRS(self, unosAgentes):
        """
        Calcula el nivel de extremismo de una red social.

        Args:
            unosAgentes (list): Lista de agentes, donde cada agente es una tupla (oRS, rRS).

        Returns:
            float: El nivel de extremismo de la red social.
        """
        suma = sum(agente[0] ** 2 for agente in unosAgentes)
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



    def solucionar(self):
        # Paso 1: Crear una lista de beneficio/costo para cada agente (cuáles nos conviene más moderar)
        beneficio_costo = [(0, 0, 0, 0)] * len(self.agentes)  # Inicializar con tuplas vacías
        for i, (opinion_i, receptividad_i) in enumerate(self.agentes):
            beneficio = opinion_i ** 2
            costo = ceil(abs(opinion_i) * (1 - receptividad_i))
            ratio = beneficio / max(costo, 1)
            beneficio_costo[i] = (ratio, i, beneficio, costo)  # Actualizar directamente



        # Paso 2: Organizar los agentes de mayor a menor dependiendo de su valor beneficio/costo
        beneficio_costo.sort(reverse=True, key=lambda x: x[0])

        # Paso 3: Moderar agentes hasta agotar el presupuesto de esfuerzo
        esfuerzo_total = 0
        estrategia = [0] * len(self.agentes)

        # Calcular la suma de los cuadrados de las opiniones al inicio
        suma = 0 

        for ratio, i, beneficio, costo in beneficio_costo:
            if esfuerzo_total + costo <= self.R_max:
                estrategia[i] = 1
                esfuerzo_total += costo

            else:
                suma += beneficio


        # Paso 4: Calcular el extremismo final usando la suma ajustada de cuadrados
        raiz = sqrt(suma)
        extremismo =  raiz / len(self.agentes)

        return [estrategia, extremismo, esfuerzo_total]





















"""
valores_p = [5.8, 21.557, 11.724, 15.717, 9.678, 11.481, 0, 3.652, 5.933, 2.419, 5.65, 4.037, 4.455, 4.24, 1.319, 1.727, 1.406, 3.955, 0.901, 1.406, 2.629, 1.524, 1.927, 0.973, 0.97, 0.815, 0.373, 0.786, 1.17, 0.309, 1.352,
0.872,
1.207,
0.561,
0.449,
0.607,
0.253,
0.228,
0.224,
0.127,
0,
0,
0,
0,
0,]

#print("{:<20} | {:<12} | {:<17} | {:<10} | {:<20} | {:<10}".format("Prueba", "N. Agentes", "Valor Solución", "Solución profe", "Exfuerzo", "diferencias"))
print(f"{"prueba":<20} | { "N.Agentes":<12} | { "Valor voraz":<17} |  { "timepo":<24} | { "Solucion profe":<10} | { "Ezfuerzo techo":<20} | { "diferencia":<10}")

def floor_to_3_decimals(value):
    return math.floor(value * 1000) / 1000

def floor_to_4_decimals(value):
    return math.floor(value * 10000) / 10000

#(20, [....], 74)

for i in range(1, 46):
    n_agentes, agentes, R_max = lector.ALFile(n=i)
    RS = [agentes, R_max]
    solucionVoraz = RedSocialModeracionVoraz(RS)
    start_time = time.time()
    techo = solucionVoraz.algoritmo_voraz()
    end_time = time.time()
    elapsed_time = end_time - start_time
    #dina = SDinacmia(n_agentes, agentes, R_max)
    #mejorada = dina.solucionar()#solucionVoraz.algoritmo_voraz_mejorado()
    mejorada = [0 ,0]

    print(f"{f'Prueba{i}.txt':<20} | {n_agentes:<12} | {floor_to_4_decimals(techo[1]):<17.5f} |  {elapsed_time:<24.20f} | {valores_p[i-1]:<14.3f} | {techo[2]:<20} | {"✔✔✔" if floor_to_4_decimals(valores_p[i-1] - floor_to_3_decimals(techo[1])) >= 0 else "---":<10} ==> {"   " if floor_to_4_decimals(valores_p[i-1] - floor_to_3_decimals(techo[1])) >= 0 else str((valores_p[i-1] * 100) / techo[1]) + '%'     }")


valores_p = [5.8, 21.557, 11.724, 15.717, 9.678, 11.481, 0, 3.652, 5.933, 2.419, 5.65, 4.037, 4.455, 4.24, 1.319, 1.727, 1.406, 3.955, 0.901, 1.406, 2.629, 1.524, 1.927, 0.973, 0.97, 0.815, 0.373, 0.786, 1.17, 0.309]

print("{:<12} | {:<12} | {:<17} | {:<10} | {:<10}".format("Prueba", "N. Agentes", "Valor Solución", "Solución profe", "diferencias"))

for i in range(1, 31):
    n_agentes, agentes, R_max = lector.ALFile(n=i)
    solucionVoraz = RedSocialModeracionVoraz(n_agentes, agentes, R_max)
    r = solucionVoraz.algoritmo_voraz()
    print("{:<12} | {:<12} | {:<17.9f} | {:<10} | {:<10}".format(f"Prueba{i}.txt", n_agentes, r[1], valores_p[i-1], 111 if valores_p[i-1] >= r[1] else 333))

100 - 99.4 +- 98.5
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

"""
80 => limite

voy en 76

10 => 4 10/4 = ?  => 2.5

6 => 2} = 11 6/2 => 3
5 => 2} = 

80



"""