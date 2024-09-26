import time
from timeit import timeit
from AlgoritmoVoraz import *
from AlgoritmoBruto import *
from lector import *
from memory_profiler import memory_usage
import pyperclip


def floor_to_3_decimals(value):
    return math.floor(value * 1000) / 1000


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

for i in range(56, 87):
    for x in range (1):

        inicio = time.time()
        voraz = soluicion_voraz(i)
        final = time.time()
        t = final - inicio
        E_v = floor_to_3_decimals(voraz[0][1])

        dinamica = soluicion_Segura(i)
        E_D = floor_to_3_decimals(dinamica[0][1])


        n_age = voraz[1]

        print(f"prueba nueva {i:<2}:  |  N: {n_age:<2}  |  Extremismo Voraz: {E_v:<12.5f}  |  Extremismo Optimo: {E_D:<12.5f}  |  {"✅✅✅" if E_v == E_D else "⭕⭕⭕"}  |  Tiempo: {t}")

        #tiempo_time = timeit(lambda: medir_memoria_metodo(i), number=1)
        #print(f"{i:<3}    <========> Tiempo Final: {tiempo_time / 1:20.12f}")

        
        op = "✅✅✅" if E_v == E_D else "⭕⭕⭕"
        

        txt += f"{n_age:<2}	{E_v}	{E_D}	{op}	{t}"
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

[[[34, 0.5249591123887468], [-97, 0.06662575262643888], [-96, 0.9909023877685615], [-5, 0.7095964332655594], [13, 0.5730892184411239], [-77, 0.3990264318559328], [11, 0.9862096012203873], [65, 0.41386829191945196], [-27, 0.6627728079835299], [-45, 0.37708482008389566], [92, 0.12287758092115264], [-85, 0.29319887852162296], [78, 0.0033000534752198885], [-59, 0.7607528856502521], [4, 0.0647508445318502], [-47, 0.5994834265364559], [97, 0.7588520698928425], [85, 0.2251905822498278], [2, 0.2450440390223817], [-98, 0.6804499082649875]], 225]


def floor_to_3_decimals(value):
    return math.floor(value * 1000) / 1000




txt = ""
for i in range(1, 56):
    for x in range (1):
        inicio = time.time()
        solucion = medir_memoria_metodo(i)
        final = time.time()
        tiempo_time = final-inicio

        n_age = solucion[1]

        print(f"{i:<3} {n_age:<10}  extremismo: {solucion[0][1]:15.10f}")

        #tiempo_time = timeit(lambda: medir_memoria_metodo(i), number=1)
        #print(f"{i:<3}    <========> Tiempo Final: {tiempo_time / 1:20.12f}")

        e = solucion[0][1]
        t = tiempo_time
        #txt += f"{t}1	2" + "\n"
        txt += f"{t}	"
        pyperclip.copy(txt)

    txt += "\n"


"""