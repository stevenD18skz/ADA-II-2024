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
jugador13 = Jugador(13, "Carlos Mendoza", 23, 73)
jugador14 = Jugador(14, "Ana Ramírez", 22, 68)
jugador15 = Jugador(15, "Ricardo Fernández", 28, 81)
jugador16 = Jugador(16, "Elena Morales", 24, 64)
jugador17 = Jugador(17, "Jorge García", 30, 56)
jugador18 = Jugador(18, "María López", 21, 79)
jugador19 = Jugador(19, "Luis Rodríguez", 27, 43)
jugador20 = Jugador(20, "Sofía González", 19, 54)
jugador21 = Jugador(21, "Pablo Martínez", 25, 76)
jugador22 = Jugador(22, "Lorena Torres", 20, 83)
jugador23 = Jugador(23, "Fernando Pérez", 26, 92)
jugador24 = Jugador(24, "Gabriela Fernández", 28, 49)
jugador25 = Jugador(25, "Emilio Vázquez", 23, 38)
jugador26 = Jugador(26, "Andrea Díaz", 22, 41)
jugador27 = Jugador(27, "Diego Sánchez", 21, 67)
jugador28 = Jugador(28, "Paula Mendoza", 20, 85)
jugador29 = Jugador(29, "Rodrigo Ramírez", 19, 59)
jugador30 = Jugador(30, "Natalia Fernández", 24, 73)
jugador31 = Jugador(31, "Alberto García", 27, 77)
jugador32 = Jugador(32, "Julia López", 22, 88)
jugador33 = Jugador(33, "Esteban Rodríguez", 23, 64)
jugador34 = Jugador(34, "Claudia González", 29, 71)
jugador35 = Jugador(35, "Julio Martínez", 26, 53)
jugador36 = Jugador(36, "Inés Torres", 25, 45)
jugador37 = Jugador(37, "Héctor Pérez", 28, 63)
jugador38 = Jugador(38, "Teresa Fernández", 30, 82)
jugador39 = Jugador(39, "Manuel Díaz", 21, 90)
jugador40 = Jugador(40, "Irene Sánchez", 22, 58)
jugador41 = Jugador(41, "José Mendoza", 19, 50)
jugador42 = Jugador(42, "Carmen Ramírez", 24, 72)
jugador43 = Jugador(43, "Pedro García", 27, 47)
jugador44 = Jugador(44, "Cristina López", 26, 36)
jugador45 = Jugador(45, "Miguel Rodríguez", 23, 79)
jugador46 = Jugador(46, "Marina González", 28, 91)
jugador47 = Jugador(47, "Antonio Martínez", 25, 52)
jugador48 = Jugador(48, "Sara Torres", 30, 68)
jugador49 = Jugador(49, "Javier Pérez", 21, 73)
jugador50 = Jugador(50, "Angela Fernández", 22, 86)
jugador51 = Jugador(51, "Raúl Díaz", 27, 45)
jugador52 = Jugador(52, "Eva Sánchez", 24, 60)
jugador53 = Jugador(53, "Victor Mendoza", 26, 78)
jugador54 = Jugador(54, "Patricia Ramírez", 19, 69)
jugador55 = Jugador(55, "David García", 23, 57)
jugador56 = Jugador(56, "Isabel López", 28, 80)
jugador57 = Jugador(57, "Gonzalo Rodríguez", 22, 66)
jugador58 = Jugador(58, "Clara González", 29, 55)
jugador59 = Jugador(59, "Martín Martínez", 21, 82)
jugador60 = Jugador(60, "Rosa Torres", 20, 62)
jugador61 = Jugador(61, "Lucas Pérez", 30, 90)
jugador62 = Jugador(62, "Diana Fernández", 27, 77)
jugador63 = Jugador(63, "Alejandro Díaz", 24, 71)
jugador64 = Jugador(64, "Beatriz Sánchez", 23, 44)
jugador65 = Jugador(65, "Marcos Mendoza", 22, 51)
jugador66 = Jugador(66, "Silvia Ramírez", 25, 88)
jugador67 = Jugador(67, "Joaquín García", 19, 67)
jugador68 = Jugador(68, "Nuria López", 26, 74)
jugador69 = Jugador(69, "Felipe Rodríguez", 30, 83)
jugador70 = Jugador(70, "Ana González", 21, 69)
jugador71 = Jugador(71, "Iván Martínez", 28, 61)
jugador72 = Jugador(72, "Olga Torres", 24, 47)
jugador73 = Jugador(73, "Rubén Pérez", 23, 54)
jugador74 = Jugador(74, "Alba Fernández", 19, 79)
jugador75 = Jugador(75, "Guillermo Díaz", 27, 85)
jugador76 = Jugador(76, "Victoria Sánchez", 22, 68)
jugador77 = Jugador(77, "Fabián Mendoza", 26, 91)
jugador78 = Jugador(78, "Alicia Ramírez", 21, 58)
jugador79 = Jugador(79, "Andrés García", 20, 53)
jugador80 = Jugador(80, "Celia López", 30, 66)
jugador81 = Jugador(81, "Adrián Rodríguez", 25, 72)
jugador82 = Jugador(82, "Natalia González", 28, 89)
jugador83 = Jugador(83, "Ernesto Martínez", 22, 77)
jugador84 = Jugador(84, "María Torres", 19, 49)
jugador85 = Jugador(85, "Gabriel Pérez", 27, 64)
jugador86 = Jugador(86, "Susana Fernández", 23, 87)
jugador87 = Jugador(87, "Enrique Díaz", 24, 71)
jugador88 = Jugador(88, "Carolina Sánchez", 26, 52)
jugador89 = Jugador(89, "Julian Mendoza", 30, 82)
jugador90 = Jugador(90, "Lucia Ramírez", 21, 60)
jugador91 = Jugador(91, "Ricardo García", 22, 74)
jugador92 = Jugador(92, "Lorena López", 25, 68)
jugador93 = Jugador(93, "Carlos Rodríguez", 27, 56)
jugador94 = Jugador(94, "Marta González", 29, 81)
jugador95 = Jugador(95, "Jorge Martínez", 23, 50)
jugador96 = Jugador(96, "Teresa Torres", 20, 77)
jugador97 = Jugador(97, "Roberto Pérez", 26, 63)
jugador98 = Jugador(98, "Daniela Fernández", 19, 91)
jugador99 = Jugador(99, "Mario Díaz", 24, 70)
jugador100 = Jugador(100, "Rita Sánchez", 21, 83)
jugador101 = Jugador(101, "Alberto Mendoza", 27, 68)
jugador102 = Jugador(102, "Elena Ramírez", 28, 45)
jugador103 = Jugador(103, "Francisco García", 25, 66)
jugador104 = Jugador(104, "Verónica López", 22, 81)
jugador105 = Jugador(105, "Hugo Rodríguez", 29, 53)
jugador106 = Jugador(106, "Esther González", 21, 78)
jugador107 = Jugador(107, "David Martínez", 24, 59)
jugador108 = Jugador(108, "Pilar Torres", 30, 85)
jugador109 = Jugador(109, "Oscar Pérez", 23, 71)
jugador110 = Jugador(110, "Lidia Fernández", 26, 88)
jugador111 = Jugador(111, "Vicente Díaz", 27, 60)
jugador112 = Jugador(112, "Cristina Sánchez", 19, 72)
jugador113 = Jugador(113, "Alfredo Mendoza", 22, 90)
jugador114 = Jugador(114, "Laura Ramírez", 28, 74)
jugador115 = Jugador(115, "Rafael García", 25, 69)
jugador116 = Jugador(116, "Isabel López", 21, 56)
jugador117 = Jugador(117, "Emilio Rodríguez", 26, 80)
jugador118 = Jugador(118, "Adriana González", 23, 89)
jugador119 = Jugador(119, "Raquel Martínez", 24, 75)
jugador120 = Jugador(120, "Miguel Torres", 30, 93)
jugador120 = Jugador(120, "Elena Ramos", 23, 52)


e1 = Equipo("Futbol", [jugador1, jugador2, jugador3])
e2 = Equipo("Volleyball", [jugador4, jugador5, jugador6])
e3 = Equipo("Futbol", [jugador7, jugador8, jugador9])
e4 = Equipo("Volleyball", [jugador10, jugador11, jugador12])

s1 = Sede("Cali", [e1, e2])
s2 = Sede("Medellin", [e3, e4])


colombia_sport = Organizacion("Colombia Sport", [s1, s2])


colombia_sport = Organizacion("Colombia Sport", [s1, s2])


def escenario(org):
  for i in org.sedes:
    print(f"\n Sede {i.obtenerNombre()} , Rendimiento: {i.obtenerPromedio()}")
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
