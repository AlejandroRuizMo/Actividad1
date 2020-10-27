from turtle import *
from random import randrange
import random
from freegames import square, vector
color = ['blue', 'green', 'yellow', 'black']
c1 = random.choice(color)
c2 = random.choice(color)
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y): #cambio de direccion de la vibora
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move(): #movimiento de la vibora
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake: #que pasa si la vibora se sale del borde o toca su cuerpo
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food: #que pasa si la cabeza de la vibora toca la comida
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake: #cuerpo de la vibora 
        square(body.x, body.y, 9, c1)

    square(food.x, food.y, 9, c2) #comida de la vibora
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()