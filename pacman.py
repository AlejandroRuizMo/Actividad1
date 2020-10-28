#Alejandro Ruiz A01177251
#Luis García A01733800
#28 de octube del 2020

#El propósito de este código es modificar un poco el juego de Pac-Man a nuestro gusto para agregarla dificultad o facilidad
#En nuestro caso, le agregamos dificultad al hacer fantasmas inteligentes y agregarles velocidad

from random import choice
from turtle import *
from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)

#El vector aim nos da la velocidad y dirección inicial de nuestro pacman
aim = vector(5, 0)
pacman = vector(-40, -80)

#El conjunto de vectores ghostos, determinan la posición, velocidad y dirección de los fantasmas
ghosts = [
    [vector(-180, 160), vector(10, 0)],
    [vector(-180, -160), vector(0, 10)],
    [vector(100, 160), vector(0, -10)],
    [vector(100, -160), vector(-10, 0)],
]

#Este vector "tiles" representa el mapa del juego, los 1 es el camino que puede ser recorrido por pacman o los fantasmas y los 0 son bordes.
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

#función que dibuja los cuadrados que construyen el mapa
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0
#dibuja el mapa con los colores elegidos
def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)
#puntos del pacman
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')
#movimientos de personajes
def move():
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])

    clear()
#el pac man se movera a donde indiquen las flechas
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    
    #Tamaño y color del pac-man
    dot(20, 'yellow')
#movimiento de fantasmas
    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
            
            #Si pacman cambia de dirección, los fantasmas cambiaran tambien en la misma
            if valid(pacman + aim):
                plan = 2*aim #Se multiplica x2 porque los fantasmas tienen el doble de velocidad que pacman
                course.x = plan.x
                course.y = plan.y
            
        else:
            #Estos son los vectores que determinan la
            #dirección y velocidad de los fantasmas cuando
            #se mueven
            options = [
                vector(10, 0), #derecha
                vector(-10, 0), #izuierda
                vector(0, 10), #arriba
                vector(0, -10), #abajo
            ]

            plan = choice(options) #el plan de los fantasmas es
            #elegir una dirección entre sus opciones
            #arriba, abajo, izquierda, derecha
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        
        #tamaño y color del fantasma
        dot(20, 'red')

    update()
#fin del juego cuando la posición de X y Y entre
#un fantasma y el pacman sea la misma con valor
#absoluto para que cuando toque un borde acabe el juego
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)
#cambio de dirección del pacman
def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
#Estos vectores harán que cambie su velocidad (pacman), por ende mientras mayor el valor del vector, más rapido se movera
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()