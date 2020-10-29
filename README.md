# Tiro Parabólico
En este proyecto modificaremos un código de un juego que consiste en lanzar una pelota para destruir los objetivos 
obedeciendo las leyes del tiro parabólico
## Primer paso
Necesitamos obtener el código base del juego para poder modificarlo, este se obtiene en la página de FreePythonGames 
y lo primero que dicta es que se importan algunas funciones para correr el juego.
```
from random import randrange
from turtle import *
from freegames import vector
```
Sin estas lineas de codigo, el juego no podrá correrse porque no tendrán las funciones básicas necesarias.
## Segundo paso
Una vez ya tenido el codigo, se identificarán las áreas a modificar. En nuestro caso, se quiere modificar la velocidad 
de la pelota, de los objetivos y que el juego sea infinito

En esta siguiente parte se ve el código que dicta la velocidad de la pelota:
```
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
```

La siguiente linea de código dicta la velocidad de los objetivos:
```
    for target in targets: #Velocidad de los targets
        target.x -=  2
```

Por último, para que el juego sea infinito.
```
    for target in dupe: #como eliminar objetivos
        #Esto se saca restando el tamaño de la bola al tamaño del target para que cada vez 
        #que esta distancia sean menor a esto, se desaparezca el target
        if abs(target - ball) > 14:
            targets.append(target)

```

## Ultima parte
Una vez tenida bien definidas las partes del código a modificar para los fines deseados, ya podremos controlar 
ciertos aspectos del juego para facilitarlo o dificultarlo.
