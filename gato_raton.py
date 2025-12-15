import random

#Creamos la tabla
def crear_tabla(fila, columna):
    tabla = [["*" for _ in range(columna)] for _ in range(fila) ]
    return tabla

#Funcion que utilizamos para imprimir la tabla a necesidad
def imprimir_tabla(tabla):
    for s in tabla:
        print("  ".join(s))
 
#Funcion que inserta/coloca de manera aleatoria el raton, el gato y la salida
def insertar_raton_gato(fila, columna, tabla):
    posiciones = [(f, c) for f in range(fila) for c in range(columna)] #Crea una lista de posiciones de la tabla/laberinto creado
    random.shuffle(posiciones) #Utilizar esas posiciones creadas/existentes y las mezcla
    
    (f_raton, c_raton), (f_gato, c_gato), (f_salida, c_salida) = posiciones[:3] #Utiliza las tres primeras posiciones ya mezcladas y las ubica de acuerdo al orden solicitado
    
    #Inserta los personajes en la tabla/matriz
    tabla[f_raton][c_raton] = "R" 
    tabla[f_gato][c_gato] = "G" 
    tabla[f_salida][c_salida] = "S"
    
    return tabla, (f_raton, c_raton), (f_gato, c_gato), (f_salida, c_salida)

#Funcion de movimientos posibles
def movimientos_posibles(pos, movimiento, tabla):
    direcciones = {
        "A" : (0, -1),
        "D"   : (0, 1),
        "W"    : (-1, 0),
        "S"     : (1, 0)
    }
    
    if movimiento not in direcciones: #En el caso de que el usuario ingrese un valor no valido
        return tabla, pos
    
    else:
        dx, dy = direcciones[movimiento] 
        fila, columna = pos 
        nueva_fila = fila + dx 
        nueva_columna = columna + dy 
        
        #Verificamos que no salga del limite(matriz/laberinto)
        if not (0 <= nueva_fila < len(tabla) and 0 <= nueva_columna < len(tabla[0])):
            return tabla, pos
        
        agarrar_personaje = tabla[fila][columna] #Guarda el personaje
        destino = tabla[nueva_fila][nueva_columna] #Guarda el destino del personaje
    
        if (agarrar_personaje == "G" and destino == "S") or (agarrar_personaje == "R" and destino == "G"):
            return tabla, pos
        
        tabla[fila][columna] = "*" 
        tabla[nueva_fila][nueva_columna] = agarrar_personaje 
        return tabla, (nueva_fila, nueva_columna)
    
#Calcular la distancia mediante la matriz por posicion de dos elementos (metodo manhattan)
def distancia_manhattan(pos1, pos2):
    distancia = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    return distancia
        
#Funcion que evalua un puntaje para que el minimax tome la mejor decision al momento de moverse
def evaluar_posicion(pos_gato, pos_raton, pos_salida): 
    posicion_evaluada = distancia_manhattan(pos_raton, pos_salida) - distancia_manhattan(pos_gato, pos_raton) #Numero positivo favorece al gato y el numero negativo favorece al raton
    return posicion_evaluada
        
def minimax(tabla, pos_gato, pos_raton, pos_salida, profundidad, es_turno_gato):
    # Caso base: si llegamos a la profundidad máxima o alguien gana
    if profundidad == 0 or pos_gato == pos_raton or pos_raton == pos_salida:
        return evaluar_posicion(pos_gato, pos_raton, pos_salida), None
    
    direcciones = ["A", "D", "W", "S"]     # Diccionario de movimientos posibles

    if es_turno_gato:
        mejor_valor = float("-inf")
        mejor_movimiento = None
        for mov in direcciones:
            tabla_copia = [fila[:] for fila in tabla] # Copiamos la tabla para simular
            nueva_tabla, nueva_pos_gato = movimientos_posibles(pos_gato, mov, tabla_copia) 
            valor, _ = minimax(nueva_tabla, nueva_pos_gato, pos_raton, pos_salida, profundidad-1, False)
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = mov
        return mejor_valor, mejor_movimiento
    
    else:
        mejor_valor = float("inf")
        mejor_movimiento = None
        for mov in direcciones:
            tabla_copia = [fila[:] for fila in tabla] # Copiamos la tabla para simular
            nueva_tabla, nueva_pos_raton = movimientos_posibles(pos_raton, mov, tabla_copia)
            valor, _ = minimax(nueva_tabla, pos_gato, nueva_pos_raton, pos_salida, profundidad-1, True)
            if valor < mejor_valor:
                mejor_valor = valor
                mejor_movimiento = mov
        return mejor_valor, mejor_movimiento

def ganar_perder(pos_gato, pos_raton, pos_salida):
    if pos_raton == pos_gato:
        print("Usted ha sido atrapado por el gato :(")
        return False
    elif pos_raton == pos_salida:
        print("Usted escapo con exito del gato")
        return False
    else:
        return True
 

valor_bool = True
while True:
    try:
        fila = int(input("Inserte la cantidad de filas (tiene que ser necesariamente mayor o igual a 2): "))
        if fila >= 2:
            break
        else:
            print("El numero de filas tiene que ser mayor o igual a 2.")
    except ValueError:
        print("Debe ingresar un valor valido")

while True:
    try:
        columna = int(input("Inserte la cantidad de columna (tiene que ser necesariamente mayor o igual a 2): "))
        if columna >= 2:
            break
        else:
            print("El numero de columna tiene que ser mayor o igual a 2.")
    except ValueError:
        print("Debe ingresar un valor valido")

niveles = """
Ingrese el nivel de dificultad que desea jugar:
1-Facil
2-Medio
3-Dificil
"""
opciones_validas = (1, 2, 3)

while True:
    try:
        profundidad = int(input(niveles + "\nIngrese el numero: "))
        if profundidad in opciones_validas:
            break
        else:
            print("El numero ingresado no esta entre las opciones")
    except ValueError:
        print("Debe ingresar un valor valido.")
    
casos = """
Usted desea jugar en forma:
1-Gato-IA vs Raton(Jugar usted como Raton contra la IA)
2-Raton-IA vs Gato(Jugar usted como Gato contra la IA)
3-Gato vs Raton(Jugar con un amigo)
"""

while True:
    try:
        caso_elegido = int(input(casos + "\nIngrese el numero del metodo de juego: "))
        if caso_elegido in opciones_validas:
            break
        else:
            print("El numero ingresado no esta entre las opciones")
    except ValueError:
        print("Debe ingresar un valor valido.")
         
tabla = crear_tabla(fila, columna)
tabla, pos_raton, pos_gato, pos_salida = insertar_raton_gato(fila, columna, tabla)
imprimir_tabla(tabla)

while valor_bool:
    match caso_elegido:
        case 1:
            movimiento_raton = input("Ingrese el movimiento del raton (W/S/A/D): ").upper()
            print("El ratón decide moverse:", movimiento_raton)
            _, movimiento_gato = minimax(tabla, pos_gato, pos_raton, pos_salida, profundidad, es_turno_gato=True)
            print("El gato decide moverse:", movimiento_gato)
        case 2:
            _, movimiento_raton = minimax(tabla, pos_gato, pos_raton, pos_salida, profundidad, es_turno_gato=False)
            print("El ratón decide moverse:", movimiento_raton)
            movimiento_gato = input("Ingrese el movimiento del gato (W/S/A/D): ").upper()
            print("El gato decide moverse:", movimiento_gato)
        case 3:
            movimiento_raton = input("Ingrese el movimiento del raton (W/S/A/D): ").upper()
            print("El ratón decide moverse:", movimiento_raton)
            movimiento_gato = input("Ingrese el movimiento del gato (W/S/A/D): ").upper()
            print("El gato decide moverse:", movimiento_gato)

    tabla, pos_raton = movimientos_posibles(pos_raton, movimiento_raton, tabla)
    tabla, pos_gato = movimientos_posibles(pos_gato, movimiento_gato, tabla)
    
    imprimir_tabla(tabla)
    valor_bool = ganar_perder(pos_gato, pos_raton, pos_salida)
    