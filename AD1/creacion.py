import random
import pyperclip



def crear_jugadores(cantidad):
  letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  todo = ""
  acarreo = 1
  pocision = 0

  for i in range (1, cantidad+1):
    print(f'jugador{i} = Jugador({i}, "{letras[pocision]}{acarreo}", {random.randint(1,100)}, {random.randint(1,100)})')
    todo += f'jugador{i} = Jugador({i}, "{letras[pocision]}{acarreo}", {random.randint(1,100)}, {random.randint(1,100)})\n'
    acarreo += 1

    if acarreo > cantidad+1/26:
      pocision += 1
      acarreo = 0
  pyperclip.copy(todo)

  

def crear_equipos(cantidad):
  deportes = ["Futbol", "Volleyball", "Basketball", "Tenis", "Natacion", "pingpong", "esgrima", "atletismo"]
  pocision = 0
  acarreo_id = 1
  todo = ""

  for i in range(1, cantidad+1, 8):
    print(f'e{acarreo_id} = Equipo("{deportes[pocision]}",     [jugador{i},jugador{i+1},jugador{i+2},jugador{i+3},jugador{i+4},jugador{i+5},jugador{i+6},jugador{i+7}])')
    todo += f'e{acarreo_id} = Equipo("{deportes[pocision]}",     [jugador{i},jugador{i+1},jugador{i+2},jugador{i+3},jugador{i+4},jugador{i+5},jugador{i+6},jugador{i+7}])\n'
    acarreo_id += 1
    pocision += 1

    if acarreo_id % 8 == 0:
      pocision = 0
  
  pyperclip.copy(todo)



def crear_sedes(cantidad):
  ciudades_colombia = [
    "Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena",
    "Cúcuta", "Bucaramanga", "Pereira", "Santa Marta", "Ibagué",
    "Pasto", "Manizales", "Neiva", "Soledad", "Villavicencio",
    "Valledupar", "Buenaventura", "Montería", "Popayán", "Sincelejo",
    "Floridablanca", "Palmira", "Bello", "Tuluá", "Envigado",
    "Buga", "Girardot", "Tumaco", "Barrancabermeja", "Dosquebradas",
    "Yumbo", "Soacha", "Facatativá", "Zipaquirá", "Florencia",
    "Maicao", "Riohacha", "Duitama", "Magangué", "Turbo",
    "Jamundí", "Quibdó", "Piedecuesta", "Apartadó", "Arauca",
    "Chía", "Espinal", "Sincelejo", "Montelíbano", "Sogamoso",
    "Ipiales", "Ciénaga", "Funza", "Girón", "Leticia",
    "Madrid", "Rionegro", "Chiquinquirá", "Calarcá", "Pamplona",
    "San Andrés", "Villanueva", "Sabanalarga", "Chinchiná", "Cereté"
  ]

  pocision = 0
  acarreo_id = 1
  todo = ""
  #s1 = Sede("Cali", [e1,e2,e3,e10,e11])
  for i in range(1, cantidad+1, 8):
    print(f'sede{acarreo_id} = Sede("{ciudades_colombia[pocision]}",     [e{i},e{i+1},e{i+2},e{i+3},e{i+4},e{i+5},e{i+6},e{i+7}])')
    todo += f'sede{acarreo_id} = Sede("{ciudades_colombia[pocision]}",     [e{i},e{i+1},e{i+2},e{i+3},e{i+4},e{i+5},e{i+6},e{i+7}])\n'

    acarreo_id += 1
    pocision += 1
  
  pyperclip.copy(todo)




#crear_jugadores(4096)
#crear_equipos(4096)
#crear_sedes(512)



for i in range(1, 65):
  print(f"sede{i}", end =", ")