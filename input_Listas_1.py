from solucion_1 import Jugador, Equipo, Sede, Organizacion, merge_sort, promedio
"""
CREACION DE DATOS
"""
jugador1 = Jugador(1, "Sofia García", 21, 66)
jugador2 = Jugador(2, "Alejandro Torres", 27, 24)
jugador3 = Jugador(3, "Valentina Rodriguez", 19, 15)
jugador4 = Jugador(4, "Juan López", 22, 78)
jugador5 = Jugador(5, "Martina Martinez", 30, 55)
jugador6 = Jugador(6, "Sebastián Pérez", 25, 42)
jugador7 = Jugador(7, "Camila Fernández", 24, 36)
jugador8 = Jugador(8, "Mateo González", 29, 89)
jugador9 = Jugador(9, "Isabella Díaz", 21, 92)
jugador10 = Jugador(10, "Daniel Ruiz", 17, 57)
jugador11 = Jugador(11, "Luciana Sánchez", 18, 89)
jugador12 = Jugador(12, "Lucas Vásquez", 26, 82)

cali_futbol = Equipo("Cali Football", [jugador10, jugador2])
cali_voley = Equipo("Cali Volleyball", [jugador1, jugador9, jugador12, jugador6])
medellin_futbol = Equipo("Medellin Football", [jugador11, jugador8, jugador7])
medellin_voley = Equipo("Medellin Volleyball", [jugador3, jugador4, jugador5])

sede_cali = Sede("Cali", [cali_futbol, cali_voley])
sede_medellin = Sede("Medellin", [medellin_futbol, medellin_voley])


colombia_sport = Organizacion("Colombia Sport", [sede_cali, sede_medellin])


def escenario(org):
  for i in org.sedes:
    print(f"\n Sede {i.obtenerNombre()} , Rendimiento: {i.obtenerSumatoria()}")
    for x in i.equipos:
      print(f"  • {x.obtenerNombre()}, Rendimiento: {x.obtenerPromedio()} \n    [", end="")
      for z in x.jugadores:
        print(f"{z.obtenerId()}", end=", ")
      print("]")

escenario(colombia_sport)
print("\n******************************************\n")
colombia_sport.ordenarSedes()
print("\n******************************************\n")
escenario(colombia_sport)





all_jugadores    = colombia_sport.obtenerTodosJugadores()
rankingJugadores = merge_sort(all_jugadores, ["Rendimiento", "Edad"])
edadJugadores    = merge_sort(all_jugadores, ["Edad"])

all_equipos    = colombia_sport.obtenerTodosLosEquipos()
rankingEquipos = merge_sort(all_equipos, ["Promedio", "NumeroJugadores"])



rankingJugadoresIds            = list(map(lambda j: j.obtenerId(), rankingJugadores))
equipo_mejor_rendimiento       = rankingEquipos[len(rankingEquipos) - 1].obtenerNombre()
equipo_menor_rendimiento       = rankingEquipos[0].obtenerNombre()
jugador_mejor_rendimiento      = rankingJugadores[len(rankingJugadores) - 1]
jugador_menor_rendimiento      = rankingJugadores[0]
jugador_mas_joven              = edadJugadores[0]
jugador_con_mas_edad           = edadJugadores[len(edadJugadores) - 1]
promedio_edad_jugadores        = promedio(all_jugadores, "Edad")
promedio_rendimiento_jugadores = promedio(all_jugadores, "Rendimiento")
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