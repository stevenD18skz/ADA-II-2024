from solucion_2 import Jugador, Equipo, Sede, Organizacion, RedBlackTree
"""
CREACION DE DATOS
"""
j1 = Jugador(1, "Juan", 20, 94)
j2 = Jugador(2, "Maria", 21, 94)
j3 = Jugador(3, "Pedro", 22, 21)
j4 = Jugador(4, "Ana", 23, 25)
j5 = Jugador(5, "Carlos", 24, 66)
j6 = Jugador(6, "Laura", 25, 52)
j7 = Jugador(7, "Jose", 26, 48)
j8 = Jugador(8, "Luis", 27, 73)
j9 = Jugador(9, "Sara", 28, 92)
j10 = Jugador(10, "Jorge", 29, 51)
j11 = Jugador(11, "Lorena", 30, 90)
j12 = Jugador(12, "Raul", 31, 100)

e1 = Equipo("Futbol", [j1, j2, j3])
e2 = Equipo("Volleyball", [j4, j5, j6])
e3 = Equipo("Futbol", [j7, j8, j9])
e4 = Equipo("Volleyball", [j10, j11, j12])

s1 = Sede("Cali", [e1, e2])
s2 = Sede("Medellin", [e3, e4])


colombia_sport = Organizacion("Colombia Sport", [s1, s2])


colombia_sport = Organizacion("Colombia Sport", [s1, s2])




def escenario(org):
    for i in org.sedes:
        print(f"{i.obtenerNombre()}:")
        for j in i.equipos:
            print(f"• {j.obtenerNombre()}: [", end="")
            for k in j.jugadores:
                print(f"{k.obtenerId()}", end=", ")
            print("]")

escenario(colombia_sport)
print("\n******************************************\n")
colombia_sport.ordenarSedes()
print("\n******************************************\n")
colombia_sport.arbol.INORDER_TREE_WALK_escenario(colombia_sport.arbol.root)




all_jugadores    = colombia_sport.obtenerTodosJugadores()
rankingJugadores = RedBlackTree()
rankingJugadores.create_tree(all_jugadores, "Rendimiento", "Edad")

edadJugadores = RedBlackTree()
edadJugadores.create_tree(all_jugadores, "Edad")


all_equipos    = colombia_sport.obtenerTodosLosEquipos()
rankingEquipos = RedBlackTree()
rankingEquipos.create_tree(all_equipos, "Promedio", "NumeroJugadores")



rankingJugadoresIds            = rankingJugadores.TREE_SPECIFIC("Id")
equipo_mejor_rendimiento       = rankingEquipos.tree_maximum()
equipo_menor_rendimiento       = rankingEquipos.tree_minimum()
jugador_mejor_rendimiento      = rankingJugadores.tree_maximum().mostrarInformacion(["Id", "Nombre", "Rendimiento"])
jugador_menor_rendimiento      = rankingJugadores.tree_minimum().mostrarInformacion(["Id", "Nombre", "Rendimiento"])
jugador_mas_joven              = edadJugadores.tree_minimum().mostrarInformacion(["Id", "Nombre", "Edad"])
jugador_con_mas_edad           = edadJugadores.tree_maximum().mostrarInformacion(["Id", "Nombre", "Edad"])
promedio_edad_jugadores        = edadJugadores.TREE_AVERAGE("Edad")
promedio_rendimiento_jugadores = rankingJugadores.TREE_AVERAGE("Rendimiento")

print(
    "\n",
    f"Ranking Jugadores: {rankingJugadoresIds}\n\n",
    f"Equipo con mayor rendimiento:  {equipo_mejor_rendimiento}\n",
    f"Equipo con menor rendimiento:  {equipo_menor_rendimiento}\n",
    f"Jugador con mayor rendimiento: {jugador_mejor_rendimiento}\n",
    f"Jugador con menor rendimiento: {jugador_menor_rendimiento}\n",
    f"Jugador mas joven: {jugador_mas_joven}\n",
    f"Jugador mas cucho: {jugador_con_mas_edad}\n",
    f"Promedio de edad de los jugadores: {promedio_edad_jugadores}\n",
    f"Promedio del rendimiento de los jugadores: {promedio_rendimiento_jugadores}\n",
)