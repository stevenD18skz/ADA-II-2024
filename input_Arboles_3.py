from solucion_2 import Jugador, Equipo, Sede, Organizacion, RedBlackTree
"""
CREACION DE DATOS
"""
j1 = Jugador(1, "Sofia Garcia", 21, 66)
j2 = Jugador(2, "Alejandro Torres", 27, 24)
j3 = Jugador(3, "Valentina Rodriguez", 19, 15)
j4 = Jugador(4, "Juan Lopez", 22, 78)
j5 = Jugador(5, "Martina Martinez", 30, 55)
j6 = Jugador(6, "Sebastian Perez", 25, 42)
j7 = Jugador(7, "Camila Fernandez", 24, 36)
j8 = Jugador(8, "Mateo Gonzalez", 29, 89)
j9 = Jugador(9, "Isabella Diaz", 40, 92)
j10 = Jugador(10, "Daniel Ruiz", 17, 57)
j11 = Jugador(11, "Luciana Sanchez", 18, 89)
j12 = Jugador(12, "Lucas Vasquez", 26, 82)
j13 = Jugador(13, "William Hernandez", 30, 44)
j14 = Jugador(14, "Laura Perez", 20, 78)
j15 = Jugador(15, "Santiago Rodriguez", 23, 32)
j16 = Jugador(16, "Maria Gonzalez", 28, 65)
j17 = Jugador(17, "Carlos Lopez", 19, 72)
j18 = Jugador(18, "Valeria Martinez", 21, 45)
j19 = Jugador(19, "Andres Perez", 30, 78)
j20 = Jugador(20, "Sara Hernandez", 22, 56)


e1 = Equipo("Futbol", [j10, j2])
e2 = Equipo("Volleyball", [j1, j9, j12, j6])
e3 = Equipo("Futbol", [j11, j8, j7])
e4 = Equipo("Volleyball", [j3, j4, j5])
e5 = Equipo("Basketball", [j13, j14, j15, j16])
e6 = Equipo("Basketball", [j17, j18, j19, j20])

s1 = Sede("Cali", [e1, e2, e5])
s2 = Sede("Medellin", [e3, e4, e6])


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