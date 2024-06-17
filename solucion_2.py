import time



def combinar_listas(lista):
      lista_combinada = []

      for elemento in lista:
        for subElemento in elemento:
            lista_combinada.append(subElemento)

      return lista_combinada


class Node:
    def __init__(self, data, color='red'):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, color='black')
        self.root = self.NIL
        self.node_count = 0



    def create_tree(self, lista, criterio1, criterio2 = ""):
        list(map(lambda x: self.insert(x, criterio1, criterio2 ), lista))
        return self


    def obtenerNumeroNodos(self):
        return self.node_count

    def insert(self, data, criterio1, criterio2 = ""):
        if not isinstance(data, Jugador):
            self.node_count += data.arbol.node_count
        else:
            self.node_count += 1

        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root
        while current != self.NIL:
            time.sleep(0)
            parent = current
            if getattr(new_node.data, 'obtener' + criterio1)() == getattr(current.data, 'obtener' + criterio1)() and criterio2 != "":
                if getattr(new_node.data, 'obtener' + criterio2)() > getattr(current.data, 'obtener' + criterio2)():
                    current = current.left
                else:
                    current = current.right

            elif getattr(new_node.data, 'obtener' + criterio1)() < getattr(current.data, 'obtener' + criterio1)():
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node


            
        elif getattr(new_node.data, 'obtener' + criterio1)() == getattr(parent.data, 'obtener' + criterio1)() and criterio2 != "":
            if getattr(new_node.data, 'obtener' + criterio2)() > getattr(parent.data, 'obtener' + criterio2)():
                parent.left = new_node
            else:
                parent.right = new_node
        elif getattr(new_node.data, 'obtener' + criterio1)() < getattr(parent.data, 'obtener' + criterio1)():
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'red'
        self.fix_insert(new_node)

    def fix_insert(self, k):
        while k != self.root and k.parent.color == 'red':
            if k.parent == k.parent.parent.left:
                uncle = k.parent.parent.right
                if uncle.color == 'red':
                    k.parent.color = 'black'
                    uncle.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.rotate_right(k.parent.parent)
            else:
                uncle = k.parent.parent.left
                if uncle.color == 'red':
                    k.parent.color = 'black'
                    uncle.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.rotate_left(k.parent.parent)
        self.root.color = 'black'

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y





    def INORDER_TREE_WALK(self, node):# ===> o(N)
        if node != self.NIL:
            self.INORDER_TREE_WALK(node.left)
            print(node.data)
            self.INORDER_TREE_WALK(node.right)



    def INORDER_TREE_WALK_escenario(self, node):# ===> o(N)
        if node != self.NIL:
            self.INORDER_TREE_WALK_escenario(node.left)

            #node.data.arbol.print_tree(node.data.arbol.root)
            if isinstance(node.data, Sede):
                print(f"\n Sede {node.data.obtenerNombre()}, Rendimiento: {node.data.obtenerSumatoria()}")
                node.data.arbol.INORDER_TREE_WALK_escenario(node.data.arbol.root)

            elif isinstance(node.data, Equipo):
                print(f"  • {node.data.obtenerNombre()}, Rendimiento: {node.data.obtenerPromedio()}")
                print("    ",node.data.arbol.TREE_SPECIFIC("Id"))

            else:
                print(node.data.obtenerNombre())
                node.data.arbol.INORDER_TREE_WALK_escenario(node.data.arbol.root)


            self.INORDER_TREE_WALK_escenario(node.right)




    def SPECIFIC_INORDER_TREE_WALK_(self, node, action):
        if node != self.NIL:
            self.SPECIFIC_INORDER_TREE_WALK_(node.left, action)
            action(node)
            self.SPECIFIC_INORDER_TREE_WALK_(node.right, action)

    def TREE_SPECIFIC(self, criterio):
        total_elements = []

        def action(node):
            nonlocal total_elements
            total_elements.append(getattr(node.data, 'obtener' + criterio)())

        self.SPECIFIC_INORDER_TREE_WALK_(self.root, action)
        
        return total_elements






    def TREE_WALK_AVERAGE(self, node, action):
        if node != self.NIL:
            self.TREE_WALK_AVERAGE(node.left, action)
            action(node)
            self.TREE_WALK_AVERAGE(node.right, action)

    def TREE_AVERAGE(self, criterio):
        total_sum = 0
        count = 0

        def action(node):
            nonlocal total_sum, count
            total_sum += getattr(node.data, 'obtener' + criterio)()
            count += 1

        self.TREE_WALK_AVERAGE(self.root, action)
        
        if count == 0:
            return 0  # To handle the case where the tree is empty
        return total_sum / count
    

    def TREE_WALK_SUM(self, node, action):
        if node != self.NIL:
            self.TREE_WALK_SUM(node.left, action)
            action(node)
            self.TREE_WALK_SUM(node.right, action)

    def TREE_SUM(self, criterio):
        total_sum = 0

        def action(node):
            nonlocal total_sum
            total_sum += getattr(node.data, 'obtener' + criterio)()

        self.TREE_WALK_SUM(self.root, action)


        return total_sum

    

    def tree_minimum(self):
        current = self.root
        while current.left != self.NIL:
            current = current.left
        return current.data

    def tree_maximum(self):
        current = self.root
        while current.right != self.NIL:
            current = current.right
        return current.data


    
    def print_tree(self, node, indent="", last='updown', side='root'):
        if node != self.NIL:
            side_str = "ROOT" if side == 'root' else ("LEFT" if side == 'left' else "RIGHT")
            print(f"{indent}<{'RED' if node.color == 'red' else 'BLACK'}> {node.data} ({side_str})")
            indent += "   " if last == 'updown' else "|  "
            self.print_tree(node.left, indent, 'up', 'left')
            self.print_tree(node.right, indent, 'down', 'right')

    def __str__(self):
        return f"soy un arbol"
        
    def __repr__(self):
        return self.__str__()







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
        return f"{'{'} id: {self.id}, {self.nombre}, Rendimiento: {self.rendimiento}, Edad: {self.edad} {'}'}"
        
    def __repr__(self):
        return self.__str__()





class Equipo:
    # Atributos
    nombre = ""
    jugadores = ""
    arbol = ""
    promedio = ""
    

    # Constructor (método __init__)
    def __init__(self, nombre, jugadores):
        self.nombre = nombre
        self.jugadores = jugadores
        self.arbol = RedBlackTree()
    
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerJugadores(self):
        return self.jugadores

    def obtenerNumeroJugadores(self):
        return self.arbol.node_count

    def obtenerPromedio(self):
        return self.promedio

    def ordenarJugadores(self):
        self.arbol.create_tree(self.jugadores, "Rendimiento", "Edad")
        self.promedio = self.arbol.TREE_AVERAGE("Rendimiento")

    def __str__(self):
        return f"{self.nombre} sede "
    
    def __repr__(self):
        return self.__str__()





class Sede:
    nombre = ""
    equipos = ""
    arbol = ""
    sumatoria = ""


    def __init__(self, nombreSede, equipos):
        self.nombre = nombreSede
        self.equipos = equipos
        self.arbol = RedBlackTree()
    
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerSumatoria(self):
        return self.sumatoria

    def obtenerNumeroJugadores(self):
        return self.arbol.node_count
        
    def ordenarEquipos(self):
        self.arbol.create_tree(self.equipos, "Promedio", "NumeroJugadores")
        self.sumatoria = self.arbol.TREE_SUM("Promedio")





class Organizacion:
    nombre = ""
    sedes = ""
    arbol = ""
    todosLosJugadores = ""
    todosLosEquipos = ""


    def __init__(self, nombreI, sedesI):
        self.nombre = nombreI
        self.sedes = sedesI
        self.arbol = RedBlackTree()
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
    

        ########## Tiempo de ordenamiento individual ########## 
    def ordenarSedes(self):
        start_time = time.time()
        list(map(lambda sedeMap: list(map(lambda eq: eq.ordenarJugadores(), sedeMap.equipos)), self.sedes))
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"El tiempo de organizacion de jugadores fue {elapsed_time} segundos")

        start_time = time.time()
        list(map(lambda se: se.ordenarEquipos(), self.sedes))
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"El tiempo de organizacion de equipos fue {elapsed_time} segundos")

        start_time = time.time()
        self.arbol.create_tree(self.sedes, "Sumatoria", "NumeroJugadores")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"El tiempo de organizacion de sedes fue {elapsed_time} segundos")





def todo(organizacion):
    def escenario():
        for i in organizacion.sedes:
            print(f"Sede {i.obtenerNombre()}:")
            for j in i.equipos:
                print(f"• {j.obtenerNombre()}: [", end="")
                for k in j.jugadores:
                    print(f"{k.obtenerId()}", end=", ")
                print("]")

    escenario()
    print("\n\n******************************************")
    organizacion.ordenarSedes()
    print("******************************************\n\n")
    organizacion.arbol.INORDER_TREE_WALK_escenario(organizacion.arbol.root)




    print("\n\n******************************************")
    all_jugadores    = organizacion.obtenerTodosJugadores()
    rankingJugadores = RedBlackTree()
    start_time = time.time()
    rankingJugadores.create_tree(all_jugadores, "Rendimiento", "Edad")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"El tiempo de organizacion de todos los jugadores por rendimietno fue {elapsed_time} segundos")

    edadJugadores = RedBlackTree()
    start_time = time.time()
    edadJugadores.create_tree(all_jugadores, "Edad")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"El tiempo de organizacion de todos los jugadores por edad fue {elapsed_time} segundos")


    all_equipos    = organizacion.obtenerTodosLosEquipos()
    rankingEquipos = RedBlackTree()
    start_time = time.time()
    rankingEquipos.create_tree(all_equipos, "Promedio", "NumeroJugadores")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"El tiempo de organizacion de todas las sedes por suma de rendimientos fue {elapsed_time} segundos")
    print("******************************************\n\n")




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