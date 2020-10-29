#Alejandro Ruiz A01177251
#Luis García A01733800
#29 de octube del 2020

#proposito del codigo
#modificar un codigo ya hecho de forma que la velocidad
#en objetivos y la bola que se lanza sea más rápido
#y también que el juego sea infinito o que nunca termine
#aunque los objetivos a eliminar lleguen al otro lado de
#la pantalla


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
        #Mientras menor sea el número por el que se divide, mayor será la velocidad
        speed.x = (x + 200) / 20 
        speed.y = (y + 200) / 20

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
        y = randrange(-150, 150) #rango donde aparecen los targets
        target = vector(200, y) 
        targets.append(target)

    for target in targets: #Velocidad de los targets
        target.x -=  2

    if inside(ball):
        speed.y -= 0.35 #Desaceleración en el Eje Y
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe: #como eliminar objetivos
        #Esto se saca restando el tamaño de la bola al tamaño del target para que cada vez que esta distancia sean menor a esto, se desaparezca el target
        if abs(target - ball) > 14:
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