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


lista_numeros = list(range(56, 67))
print(lista_numeros)


indice = list(range(56, 100))

n = 100
s = 200
f = (30*s)

acc = 0

for i in range(n,f+s+n, s):
    guardar_solucion(indice[acc], generate(i))
    acc += 1


