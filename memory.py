"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

"""

from random import shuffle
from turtle import done, onscreenclick, tracer, hideturtle, addshape, bye
from turtle import write, color, goto, up, stamp, shape, clear, left, forward
from turtle import begin_fill, down, end_fill, setup, ontimer, update, title

from freegames import path

# Se declaran las variables
car = path('car.gif')
tiles = list(range(32)) * 2
tiles2 = [
    "*", "#", "x", "y", ":)", ":(", ":O", "D:", ":D", ";)", "B)", ":P",
    ":v", ">:v", "v:", "UwU", "xD", "7w7", "TuT", ":3", "$",
    "%", "¿?", "c:", ":c", ":'c", ":')", "^^", "^u^", "(o.o)", ".o.", ".-."
    ] * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0
cuentacuantos = 0


# Se dibuja la cuadricula en pantalla
def square(x, y):
    "Draw white square with black outline at (x, y)."
    # Levanta el turtle para dibujar la cuadricula en
    # En las coordenadas x y y
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


# Las coordenadas de x,y se asocian a un index de tiles
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


# Convierte el index de tiles a una coordenada x,y
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


# Detecta los clicks en la pantalla
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    # Aparece el numero de clicks dado en la consola
    global tap_count
    tap_count = tap_count + 1
    print("number of taps: ", tap_count)

    spot = index(x, y)  # direccion del tile
    mark = state['mark']  # estado del tile

    # Identifica si las imagenes corresponden para revelar el fondo
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        # Indica cuantos pares se han encontrado desplegado en consola
        global cuentaPares
        cuentaPares = cuentaPares + 1
        print("Pares encontrados: ", cuentaPares)
        if cuentaPares == 32:
            bye()
            print("YOU WIN, congratulations!!")


# Dibuja el fondo my permite que sean visibles las tiles
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

    # Se indica que va a aparecer en las tiles al momento de voltearlas
    if mark is not None and hide[mark]:

        x, y = xy(mark)
        up()

        color('black')
        goto(x + 13, y + 10)
        write(tiles2[tiles[mark]], font=('Arial', 15, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
title("MemoryGame")
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
