from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200) #desde donde se tira la bola
speed = vector(0, 0) #velocidad
targets = [] #bolas azules objetivo

def tap(x, y): #accion de tocar la pantalla marcando
    #a donde sera lanzada la bola
    "Respond to screen tap."
    if not inside(ball): #si la bola no esta en el rango establecido
        #la bola sera lanzada fuera del area de juego
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy): #marca el rango del juego
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():#acción del juego
    "Draw ball and targets."
    clear()

    for target in targets: #objetivos
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball): #bola a lanzar
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move(): #descripción del movimiento de la bola
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35 #VELOCIDAD DE LA BOLA A LANZAR
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe: #como eliminar objetivos
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    ontimer(move, 50) #acercamiento de abjetivos al
    #otro lado del mapa

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()