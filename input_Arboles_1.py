from solucion_2 import Jugador, Equipo, Sede, Organizacion, RedBlackTree, todo
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
todo(colombia_sport)