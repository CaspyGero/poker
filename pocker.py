from random import randint
#VARIABLES INICIALES
colores = ["corazon", "diamante", "picas", "treboles"]
cartasPorColor = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
cartas = []
#GENERAR CARTAS QUE SE USARAN
for color in colores:
    for carta in cartasPorColor:
        cartas.append(color + str(carta))
"""
COMBINACIONES:
ESCALERA REAL: ESCALERA [10, A] DEL MISMO COLOR
ESCALERA COLOR: ESCALERA CON LAS CARTAS DEL MISMO COLOR
POKER: 4 CARTAS IGUALES
FULLHOUSE: UN PAR Y UN TRIO
COLOR: 5 CARTAS DEL MISMO COLOR
ESCALERA: 5 CARTAS CON NUMEROS CONSECUTIVOS
TRIO: 3 CARTAS IGUALES
DOBLE PAR: 2 PARES
PAR: 2 CARTAS IGUALES
HIGH CARD: LA CARTA MAS ALTA
"""
#Declarar clases
class claseJugador:
    def __init__(self, nombre:str, fichas:int):
        self.nombre = nombre #Un str con el nombre del jugador
        self.fichas = fichas #Un int con las fichas(Sin contar apuesta) del jugador
        self.apuesta = None #Un int con la apuesta del jugador
        self.cartas = [] #Una lista con las 2 cartas que se le dan a el jugador
        self.cartasJugables = [] #Una lista con las cartas en mano y las cartas de la mesa
        self.mejorJugada = None #Se escribe en numeros, del 1 al 10
    def __str__(self):
        return f"El jugador {self.nombre} tiene {self.fichas} fichas."
class claseCartasJugables:
    def __init__(self, cartas:list):
        self.cartas = cartas
        self.colores = []
        for i in range(0, 7):
            self.colores.append(self.cartas[i])
class claseMesa:
    def __init__(self, pozo=0):
        self.pozo = pozo
        self.cartas = []
class jugadas:
    def obtenerColores(cartas):
        for i in range(0, len(cartas)):
            cartas[i] = cartas[i][:-1]
    def contar(elementos, minimo):
        contador = {}
        for elemento in elementos:
            if elemento in elementos:
                contador[elemento] += 1
        else:
            contador[elemento] = 1
        for elemento, cantidad in contador.items():
            if cantidad > minimo:
                return True
            else:
                return False
    def escaleraReal(cartas):
        colores = jugadas.obtenerColores(cartas)
        if jugadas.contar(colores, 5):
            pass
        return True
jugadores = []
mesa = claseMesa()
cantidadJugadores = int(input("Cantidad jugadores: "))
fichasIniciales = int(input("Ingresela cantidad de fichas iniciales para cada jugador: "))
#Repartir cartas
for i in range(0, cantidadJugadores):
    jugadores.append(claseJugador(input(f"Ingrese el nombre del jugador {i + 1}: "), fichasIniciales))
    jugadores[i].cartas.append(cartas.pop(randint(0, len(cartas) - 1)))
    jugadores[i].cartas.append(cartas.pop(randint(0, len(cartas) - 1)))
for i in range(0, 5):
    mesa.cartas.append(cartas.pop(randint(0, len(cartas) - 1)))
for i in range(0, cantidadJugadores):
    jugadores[i].cartasJugables = claseCartasJugables(jugadores[i].cartas + mesa.cartas)

#TODO: ACA PONER LAS RONDAS, APUESTAS Y ESO

#Comprobar posibles jugadas
for i in range(0, cantidadJugadores):
    if jugadas.escaleraReal(jugadores[i].cartasJugables):
        jugadores[i].mejorJugada = 10

#TODO: ELIMINAR DESPUES
for i in jugadores:
    print(i)
print(cartas)