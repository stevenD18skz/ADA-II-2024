import time



def merge_sort(lista, criterios):
  if len(lista) <= 1:
    return lista

  # Dividir la lista en dos mitades
  mitad = len(lista) // 2
  izquierda = merge_sort(lista[:mitad], criterios)
  derecha = merge_sort(lista[mitad:], criterios)


  def merge(izquierda, derecha):
    resultado = []
    i = 0
    j = 0
    while i < len(izquierda) and j < len(derecha):
      time.sleep(0.1)
      if getattr(izquierda[i], 'obtener' + criterios[0])() == getattr(derecha[j], 'obtener' + criterios[0])() and (len(criterios) > 1):
        if getattr(izquierda[i], 'obtener' + criterios[1])() > getattr(derecha[j], 'obtener' + criterios[1])():
          resultado.append(izquierda[i])
          i += 1
        else:
          resultado.append(derecha[j])
          j += 1
      
      else:
        if getattr(izquierda[i], 'obtener' + criterios[0])() <= getattr(derecha[j], 'obtener' + criterios[0])():
          resultado.append(izquierda[i])
          i += 1
        else:
          resultado.append(derecha[j])
          j += 1

    # Agregar los elementos restantes de la lista que no se han procesado
    resultado += izquierda[i:]
    resultado += derecha[j:]

    return resultado
  # Combinar las dos mitades ordenadas
  return merge(izquierda, derecha)



def promedio(lista, criterio):# => o(n)
  c = 0
  for i in lista:
    c+= getattr(i, 'obtener' + criterio)()
  return c/len(lista)



def combinar_listas(lista):
      lista_combinada = []

      for elemento in lista:
        for subElemento in elemento:
          lista_combinada.append(subElemento)

      return lista_combinada





class Jugador:
  # Atributos
  id = 0
  nombre = ""
  edad = 0
  rendimiento = 0

  # Constructor (método __init__)
  def __init__(self,id_inicial, nombre_inicial, edad_inicial, rendimientdo_inicial):
    self.id = id_inicial
    self.nombre = nombre_inicial
    self.edad = edad_inicial
    self.rendimiento = rendimientdo_inicial

  def obtenerId(self):
    return self.id

  def obtenerNombre(self):
    return self.nombre

  def obtenerEdad(self):
    return self.edad

  def obtenerRendimiento(self):
    return self.rendimiento
  

  def mostrarInformacion(self, criterios):
        info = []
        for c in criterios:
            info.append(getattr(self, 'obtener' + c)())
        return info

  def __str__(self):
    return f"soy {self.nombre}"
    
  def __repr__(self):
    return self.__str__()





class Equipo:
  # Atributos
  nombre = ""
  jugadores = ""
  promedio = ""
  numeroDejugadores = ""
  

  # Constructor (método __init__)
  def __init__(self, nombre, jugadores):
    self.nombre = nombre
    self.jugadores = jugadores
    self.promedio = promedio(jugadores, "Rendimiento")
    self.numeroDejugadores = len(self.jugadores)
  
  def obtenerNombre(self):
    return self.nombre
  
  def obtenerJugadores(self):
    return self.jugadores
  
  def obtenerPromedio(self):
    return self.promedio

  def obtenerNumeroJugadores(self):
    return self.numeroDejugadores

  def ordenarJugadores(self):
    self.jugadores = merge_sort(self.jugadores, ["Rendimiento", "Edad"])

  def __str__(self):
    return f"soy {self.nombre}"
  
  def __repr__(self):
    return self.__str__()





class Sede:
  nombre = ""
  equipos = ""
  sumatoria = ""
  numeroJugadores = ""


  def __init__(self, nombreSede, equipos):
    self.nombre = nombreSede
    self.equipos = equipos
    self.sumatoria = sum(list(map(lambda x: x.obtenerPromedio(), equipos)))
    self.numeroJugadores = sum(list(equipo.obtenerNumeroJugadores() for equipo in self.equipos))
  
  def obtenerNombre(self):
    return self.nombre
  
  def obtenerEquipos(self):
    return self.equipos

  def obtenerSumatoria(self):
    return self.sumatoria

  def obtenerNumeroJugadores(self):
    return self.numeroJugadores

  def ordenarEquipos(self):
    self.equipos = merge_sort(self.equipos, ["Promedio", "NumeroJugadores"])[::-1]





class Organizacion:
  nombre = ""
  sedes = ""
  todosLosJugadores = ""
  todosLosEquipos = ""


  def __init__(self, nombreI, sedesI):
    self.nombre = nombreI
    self.sedes = sedesI
    self.todosLosJugadores = combinar_listas(list(equipo.jugadores for equipo in combinar_listas(list(sede.equipos for sede in self.sedes))))
    self.todosLosEquipos = combinar_listas(list(sede.equipos for sede in self.sedes))

  def obtenerNombre(self):
    return self.nombre

  def obtenerSedes(self):
    return self.sedes
  
  def obtenerTodosJugadores(self):
    return self.todosLosJugadores 

  def obtenerTodosLosEquipos(self):
    return self.todosLosEquipos
  
  def ordenarSedes(self):
    ########## Tiempo de ordenamiento general ########## 
    """     
    start_time = time.time()
    self.sedes = merge_sort(self.sedes, ["Sumatoria", "NumeroJugadores"])[::-1] 
    list(map(lambda se: se.ordenarEquipos(), self.sedes))
    list(map(lambda sedeMap: list(map(lambda eq: eq.ordenarJugadores(), sedeMap.equipos)), self.sedes))

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"El tiempo de organizacion fue {elapsed_time} segundos")
    """

    ########## Tiempo de ordenamiento individual ########## 
    start_time = time.time()
    self.sedes = merge_sort(self.sedes, ["Sumatoria", "NumeroJugadores"])[::-1]
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"El tiempo de organizacion de sedes fue {elapsed_time} segundos")



    start_time2 = time.time()
    list(map(lambda se: se.ordenarEquipos(), self.sedes))
    end_time2 = time.time()
    elapsed_time2 = end_time2 - start_time2
    print(f"El tiempo de organizacion de equipos fue {elapsed_time2} segundos")



    start_time3 = time.time()
    list(map(lambda sedeMap: list(map(lambda eq: eq.ordenarJugadores(), sedeMap.equipos)), self.sedes))
    end_time3 = time.time()
    elapsed_time3 = end_time3 - start_time3
    print(f"El tiempo de organizacion de jugadores fue {elapsed_time3} segundos")





def todo(organizacion):
  def escenario():
    for i in organizacion.sedes:
      print(f"\n Sede {i.obtenerNombre()}, Rendimiento: {i.obtenerSumatoria()}")
      for x in i.equipos:
        print(f"  • {x.obtenerNombre()}, Rendimiento: {x.obtenerPromedio()} \n    [", end="")
        for z in x.jugadores:
          print(f"{z.obtenerId()}", end=", ")
        print("]")

  escenario()
  print("\n\n******************************************")
  organizacion.ordenarSedes()
  print("******************************************\n\n")
  escenario()


  print("\n\n******************************************")
  all_jugadores = organizacion.obtenerTodosJugadores()

  start_time = time.time()
  rankingJugadores = merge_sort(all_jugadores, ["Rendimiento", "Edad"])
  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"El tiempo de organizacion de todos los jugadores por rendimietno fue {elapsed_time} segundos")

  start_time = time.time()
  edadJugadores    = merge_sort(all_jugadores, ["Edad"])
  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"El tiempo de organizacion de todos los jugadores por edad fue {elapsed_time} segundos")

  start_time = time.time()
  all_equipos    = organizacion.obtenerTodosLosEquipos()
  rankingEquipos = merge_sort(all_equipos, ["Promedio", "NumeroJugadores"])
  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"El tiempo de organizacion de todas las sedes {elapsed_time} segundos")
  print("******************************************\n\n")



  rankingJugadoresIds            = list(map(lambda j: j.obtenerId(), rankingJugadores))
  equipo_mejor_rendimiento       = rankingEquipos[len(rankingEquipos) - 1].obtenerNombre()
  equipo_menor_rendimiento       = rankingEquipos[0].obtenerNombre()
  jugador_mejor_rendimiento      = rankingJugadores[len(rankingJugadores) - 1].mostrarInformacion(["Id", "Nombre", "Rendimiento"])
  jugador_menor_rendimiento      = rankingJugadores[0].mostrarInformacion(["Id", "Nombre", "Rendimiento"])
  jugador_mas_joven              = edadJugadores[0].mostrarInformacion(["Id", "Nombre", "Edad"])
  jugador_con_mas_edad           = edadJugadores[len(edadJugadores) - 1].mostrarInformacion(["Id", "Nombre", "Edad"])
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

