import os
import random
import pyperclip


def guardar_solucion(n, solucion_outPut):
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script[:45], 'Entradas', f'Prueba{n}.txt')

    print(ruta_archivo)

    #ruta = "c:\Users\braya\Desktop\PRY\ADA-II-2024\AD2_1\nuevas\Prueba56.txt"

    with open(ruta_archivo, 'w') as file:
        file.write(solucion_outPut)



def generate(n):
    todo = [f"{n}\n"]
    for i in range(n):
        todo.append(f"{random.randint(-100, 100)}, {random.uniform(0, 1)}\n")

    #print(n*random.randint(3, 30))
    todo.append(str(n * random.randint(3, 25)))

    result = ''.join(todo)

    pyperclip.copy(result)

    return result




for i in range(15,26):
    guardar_solucion(i+41, generate(i))


