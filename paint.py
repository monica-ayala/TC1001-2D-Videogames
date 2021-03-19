"""Paint, for drawing shapes.
Exercises
1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import up, goto, down, begin_fill, forward, left, setup, circle
from turtle import end_fill, onscreenclick, listen, onkey, undo, color, done
from turtle import setposition, right
from freegames import vector


def line(start, end):
    "Draw line from start to end."
    # Levanta el turtle del lienzo (no pinta)
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    # Levanta el turtle del lienzo (no pinta)
    up()
    # Mueve el turtle hacia la posición que clicquea el usuario
    goto(start.x, start.y)
    # Pone el turtle sobre el lienzo (puede pintar)  
    down()

    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()
    up()


def circle_draw(start, end):
    "Draw square from start to end."
    # Levanta el turtle del lienzo (no pinta)
    up()
    # Mueve el turtle hacia la posición que clicquea el usuario
    goto(start.x, start.y)
    # Pone el turtle sobre el lienzo (puede pintar)
    down()
    begin_fill()

    circle(end.x - start.x)

    end_fill()
    up()


def rectangle(start, end):
    "Draw rectangle from start to end."
    # Levanta el turtle del lienzo (no pinta)
    up()
    # Mueve el turtle hacia la posición que clicquea el usuario
    goto(start.x, start.y)
    # Pone el turtle sobre el lienzo (puede pintar)
    down()

    # Se indica el color de relleno de la figura
    # al igual que el inicio y final de la acción
    begin_fill()

    # Se realiza dos trazos principales del rectangulo: base y lateral.
    # Guarda una relacion 1:2
    for i in range(2):
        forward(end.x-start.x)
        right(90)
        forward((end.x-start.x)*2)
        right(90)
    up()
    # Termina de rellenar
    end_fill()


def triangle(start, end):
    "Draw triangle from start to end."
    # Levanta el turtle del lienzo (no pinta)
    up()
    # Mueve el turtle hacia la posición que clicquea el usuario
    goto(start.x, start.y)
    # Pone el turtle sobre el lienzo (puede pintar)
    down()

    begin_fill()

    # Se realiza el trazo principal del triangulo. Lados iguales.
    for i in range(3):
        forward(end.x - start.x)
        left(120)
    end_fill()


def tap(x, y):
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
onkey(lambda: color('black'), 'k')
onkey(lambda: color('white'), 'w')
onkey(lambda: color('green'), 'g')
onkey(lambda: color('blue'), 'b')
onkey(lambda: color('red'), 'r')
onkey(lambda: color('yellow'), 'y')
onkey(lambda: store('shape', line), 'L')
onkey(lambda: store('shape', square), 'S')
onkey(lambda: store('shape', circle_draw), 'C')
onkey(lambda: store('shape', rectangle), 'R')
onkey(lambda: store('shape', triangle), 'T')
done()
