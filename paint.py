from turtle import  *
from freegames import vector

def line(start, end): #esta función nos ayuda a trazar una linea recta utilizando coordenadas en en el eje "x" y eje "y"
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end): #esta función dibuja un cuadrado basandose en las coordenadas en el eje x
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4): #En este for, se toma la distancia entre las x y dibuja un cuadrado con 4 lados de longitud x2-x1
        forward(end.x - start.x)
        left(90)

    end_fill() #Aqui llena los espacios encerrados

def circle(start, end): #esta función es parecida a al del cuadrado, traza varios cuadrados rotados en difetentes angulos en la misma posición de X y Y considerando el primer punto de origen y el segundo como el lago que tambien es el equivalente al diametro del circulo
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    speed(100)

    for count in range(40):
        forward(end.x - start.x)
        left(91)
        for count in range(1):
            forward(end.x - start.x)
            left(80)
            speed(100)
        
    end_fill()


def rectangle(start, end): #Aqui se dibuja y colorea un rectangulo con 2 lados iguales y 2 diferentes
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2): #Este for hace que el rectangulo tenga un lado de x2-x1 y otro lado de y2-y1. Solo se colocan dos puntos en el plano y listo
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
        
    end_fill()

def triangle(start, end): #Esta función dibuja un triangulo equilatero solamente con dos puntos
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3): #Este for toma la distancia en x de los 2 puntos y con esa distancia forma un triangulo equilatero
        forward(end.x - start.x)
        left(120)

    end_fill() 

def tap(x, y): #Esta función es la encargada de registrar las coordenadas que hemos seleccionado en el mapa cartesiano que se genera
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()