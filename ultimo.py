#Alejandro Ruiz A01177251
#Luis García A01733800
#30 de octubre del 2020
#Este codigo cuando se corre, genera un juego de memorama. Nuestro objetivo es comprender el codigo a tal punto
#que podamos hacer cambios a nuestro gusto. En este caso, decidimos cambiar la sombología de las cartas de números
#a letras, el tamaño de estas y que estén más centradas en las casillas, que nos avise cuando terminemos y que nos regrese el número de taps que realizamos.

from random import *
from turtle import *
from freegames import path

#Valor inicial de Taps
Taps = {'Taps': 0}
car = path('car.gif')
#G representa el simbolo que representa las casillas, deben ser 32 si se quiere un tablero 8x8
G = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '%', '&', '+', '$', '?']
#Tiles es la lista G * 2 debido a que son 64 casillas y en G solos hay 32
#Esto también hará duplicas para que coincidan las cartas al momento de voltearlas
tiles = list(G) * 2
state = {'mark': None}
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    #Aqui podemos obtener tamaño de las casillas justo para nuestro juego, para que quepan las casillas y cubran la imagen
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    #Donde se pique en el tablero, se ajusta para que seleccione la casilla correspondiente
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    #Cada vez que haya un tap, se sumará a 'Taps' y al terminar el juego, se imprime
    Taps['Taps'] += 1
    
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #Coordenedas donde aparecera el número, el origen es la esquina inferior izquierda
        goto(x+10,y+2)
        #Color de letra
        color('black')
        #Tipografía y tamaño
        write(tiles[mark], font=('Arial', 20, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
print(Taps)