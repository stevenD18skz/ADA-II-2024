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



def promedio(lista, criterio):
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



  def __str__(self):
    return f"{'{'} id: {self.id}, {self.nombre}, Rendimiento: {self.rendimiento}, Edad: {self.edad} {'}'}"
    
  def __repr__(self):
    return self.__str__()





class Equipo:
  # Atributos
  nombre = ""
  jugadores = ""
  

  # Constructor (método __init__)
  def __init__(self, nombre, jugadores):
    self.nombre = nombre
    self.jugadores = jugadores
  
  def obtenerNombre(self):
    return self.nombre

  def obtenerNumeroJugadores(self):
    return len(self.jugadores)

  def obtenerPromedio(self):
    return promedio(self.jugadores, "Rendimiento")

  def ordenarJugadores(self):
    self.jugadores = merge_sort(self.jugadores, ["Rendimiento", "Edad"])

  def __str__(self):
    return f"{self.nombre}: {list(x.obtenerId() for x in self.jugadores)}"
  
  def __repr__(self):
    return self.__str__()





class Sede:
  nombre = ""
  equipos = ""


  def __init__(self, nombreSede, equipos):
    self.nombre = nombreSede
    self.equipos = equipos
  
  def obtenerNombre(self):
    return self.nombre
  
  def obtenerPromedio(self):
    return sum(list(x.obtenerPromedio() for x in self.equipos)) / len(self.equipos)

  def obtenerNumeroJugadores(self):
    return sum(list(x.obtenerNumeroJugadores() for x in self.equipos))
    
  def ordenarEquipos(self):
    self.equipos = merge_sort(self.equipos, ["Promedio", "NumeroJugadores"])[::-1]




class Organizacion:
  nombre = ""
  sedes = ""


  def __init__(self, nombreI, sedesI):
    self.nombre = nombreI
    self.sedes = sedesI

  def obtenerNombre(self):
    return self.nombre

  def obtenerSedes(self):
    return self.sedes
  
  def obtenerTodosJugadores(self):
    return combinar_listas(list(equipo.jugadores for equipo in combinar_listas(list(sede.equipos for sede in self.sedes))))

  def obtenerTodosLosEquipos(self):
    return combinar_listas(list(sede.equipos for sede in self.sedes))
  
  def ordenarSedes(self):
    self.sedes = merge_sort(self.sedes, ["Promedio", "NumeroJugadores"])[::-1]
    list(map(lambda se: se.ordenarEquipos(), self.sedes))
    list(map(lambda sedeMap: list(map(lambda eq: eq.ordenarJugadores(), sedeMap.equipos)), self.sedes))

    




