from obejtos import *

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
jugador13 = Jugador(13, "jhon lenono", 30, 95)
jugador14 = Jugador(14, "Sisa mano", 30, 99)



cali_futbol = Equipo("Cali Football", [jugador10, jugador2])
cali_voley = Equipo("Cali Volleyball", [jugador1, jugador9, jugador12, jugador6])
cali_pongping = Equipo("Cali Pingpong", [jugador13])



medellin_futbol = Equipo("Medellin Football", [jugador11, jugador8, jugador7])
medellin_voley = Equipo("Medellin Volleyball", [jugador3, jugador4, jugador5])
medellin_pongping = Equipo("Medellin Pingpong", [jugador14])



sede_cali = Sede("Cali", [cali_futbol, cali_voley])
sede_medellin = Sede("Medellin", [medellin_futbol, medellin_voley])



colombia_sport = Organizacion("Colombia Sport", [sede_cali, sede_medellin])





def escenario(org):
  for i in org.sedes:
    print(f"{i.obtenerNombre()}:")
    for x in i.equipos:
      print(f"• {x.obtenerNombre()}: [", end="")
      for z in x.jugadores:
        print(f"{z.obtenerId()}", end=", ")
      print("]")



escenario(colombia_sport)
print("\n******************************************\n")
colombia_sport.ordenarSedes()
print("\n******************************************\n")
escenario(colombia_sport)





all_jugadores = colombia_sport.obtenerTodosJugadores()



rankingJugadores = merge_sort(all_jugadores, ["Rendimiento", "Edad"])
rankingJugadoresIds = list(map(lambda j: j.obtenerId(), rankingJugadores))
edadJugadores = merge_sort(all_jugadores, ["Edad"])



promedio_edad_jugadores = promedio(all_jugadores, "Edad")
promedio_rendimiento_jugadores = promedio(all_jugadores, "Rendimiento")



all_equipos = colombia_sport.obtenerTodosLosEquipos()
rankingEquipos = merge_sort(all_equipos, ["Promedio", "NumeroJugadores"])


print(
  "\n",
  f"Ranking Jugadores: {rankingJugadoresIds}\n\n",
  f"Equipo con mayor rendimiento: {rankingEquipos[len(rankingEquipos) - 1].obtenerNombre()}\n",
  f"Equipo con menor rendimiento: {rankingEquipos[0].obtenerNombre()}\n",
  f"Jugador con mayor rendimiento: {rankingJugadores[len(rankingJugadores) - 1]}\n",
  f"Jugador con menor rendimiento: {rankingJugadores[0]}\n",
  f"Jugador mas joven: {edadJugadores[0]}\n",
  f"Jugador mas cucho: {edadJugadores[len(edadJugadores) - 1]}\n",
  f"Promedio de edad de los jugadores: {promedio_edad_jugadores}\n",
  f"Promedio del rendimiento de los jugadores: {promedio_rendimiento_jugadores}\n",
)



#     & C:/Users/braya/AppData/Local/Programs/Python/Python312/python.exe c:/Users/braya/Desktop/ADA/solucion.py



#print(list(map(lambda x: x*x, [1,2,3,4])))
#lista_equipos_cali = [e1]
#print(  list(sum(list(x.obtenerRendimiento() for x in y)) / len(y) for y in lista_equipos_cali)   )
#cali_futbol.ordenarJugadores()
#print([x.obtenerId() for x in cali_futbol.jugadores])


#sede_cali.odenarEquiposPorPuntaje()
#print("xxx")
#print([x.obtenerNombre() for x in sede_cali.equipos])

#print(jugador1)
#print(cali_futbol)
#print(sede_cali)