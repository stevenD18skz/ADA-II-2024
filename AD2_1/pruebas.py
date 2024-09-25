import time
from timeit import timeit
from AlgoritmoVoraz import *
from AlgoritmoBruto import *
from lector import *
from memory_profiler import memory_usage
import pyperclip


def soluicion_voraz(num):
    entrada = ALFile(n=num)
    n_agentes = entrada[0]
    rs = entrada[1:3]
    motor = modexV(rs)
    solucion = motor.solucionar()
    
    return solucion, n_agentes

def soluicion_Segura(num):
    entrada = ALFile(n=num)
    n_agentes = entrada[0]
    rs = entrada[1:3]
    motor = modexPD(rs)
    solucion = motor.solucionar()
    
    return solucion, n_agentes

txt = ""
for i in range(56, 67):
    for x in range (1):
        solucion = soluicion_voraz(i)
        ex_v = solucion[0][1]

        solucion_b = soluicion_Segura(i)
        ex_b = solucion[0][1]


        n_age = solucion[1]

        print(f"prueba nueva {i-55:<2}:  |  N: {n_age:<2}  |  Extremismo Voraz: {ex_v:<12.5f}  |  Extremismo Optimo: {ex_b:<12.5f}  |  {"✅✅✅" if ex_v == ex_b else "⭕⭕⭕"}")

        #tiempo_time = timeit(lambda: medir_memoria_metodo(i), number=1)
        #print(f"{i:<3}    <========> Tiempo Final: {tiempo_time / 1:20.12f}")


        txt += f"{ex_v}	{ex_b}" + "\n"
        pyperclip.copy(txt)

    txt += "\n"



"""
def medir_memoria_metodo(num):
    entrada = ALFile(n=num)
    n_agentes = entrada[0]
    rs = entrada[1:3]
    motor = modexV(rs)
    solucion = motor.solucionar()
    
    return solucion, n_agentes


# Medir el tiempo de ejecución

def floor_to_3_decimals(value):
    return math.floor(value * 1000) / 1000


valores_p = [5.8, 21.557, 11.724, 15.717, 9.678, 11.481, 0, 3.652, 5.933, 2.419, 5.65, 4.037, 4.455, 4.24, 1.319, 1.727, 1.406, 3.955, 0.901, 1.406, 2.629, 1.524, 1.927, 0.973, 0.97, 0.815, 0.373, 0.786, 1.17, 0.309, 1.352,0.872,1.207,0.561,0.449,0.607,0.253,0.228,0.224,0.127,0,0,0,0,0]

txt = ""
for i in range(1, 56):
    for x in range (1):
        inicio = time.time()
        solucion = medir_memoria_metodo(i)
        final = time.time()
        tiempo_time = final-inicio

        n_age = solucion[1]

        print(f"{i:<3} {n_age:<10}  extremismo: {solucion[0][1]:15.10f} <=====> P: {valores_p[i-1]:<8}  {"✅✅✅" if floor_to_3_decimals(solucion[0][1]) <= valores_p[i-1] else "      "}    Tiempo Final: {tiempo_time:20.12f}")

        #tiempo_time = timeit(lambda: medir_memoria_metodo(i), number=1)
        #print(f"{i:<3}    <========> Tiempo Final: {tiempo_time / 1:20.12f}")

        e = solucion[0][1]
        t = tiempo_time
        #txt += f"{t}1	2" + "\n"
        txt += f"{t}	"
        pyperclip.copy(txt)

    txt += "\n"



con el for normal
55     <========> Tiempo Final:      13.484519300000
55     <========> Tiempo Final:      13.277457200002
55     <========> Tiempo Final:      12.741125400000
55     <========> Tiempo Final:      13.329942600001
55     <========> Tiempo Final:      13.642960400000

55     <========> Tiempo Final:      12.287298299998
55     <========> Tiempo Final:      12.189783600003
55     <========> Tiempo Final:      12.967816699998
55     <========> Tiempo Final:      12.802010600000
55     <========> Tiempo Final:      12.731625500001

55     <========> Tiempo Final:      12.558544500000
55     <========> Tiempo Final:      12.957750599999
55     <========> Tiempo Final:      11.957949800002

"""