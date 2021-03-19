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


# Funcion que dibuja una linea recta
def line(start, end):
    "Draw line from start to end."
    # Levanta el turtle del lienzo (no pinta)
    up()

    # Mueve el turtle hacia la posición que clicquea el usuario
    goto(start.x, start.y)

    # Pone el turtle sobre el lienzo (puede pintar)
    down()

    # Mueve el turtle hacia la posición que clicquea el usuario
    goto(end.x, end.y)


# Funcion que dibuja un cuadrado
def square(start, end):
    "Draw square from start to end."
    # Levanta el turtle del lienzo (no pinta)
    up()

    # Mueve el turtle hacia la posición que clicquea el usuario
    goto(start.x, start.y)

    # Pone el turtle sobre el lienzo (puede pintar)
    down()

    # Se indica el rellenado de la figura
    begin_fill()

    # Se realiza un trazo que se repite 4 veces
    # para formar el cuadrado
    for count in range(4):
        # Accion del trazado
        forward(end.x - start.x)
        # El turtle gira 90 grados a la izquierda
        left(90)

    # Termina el relleno de la figura
    end_fill()

    # Levanta el turtle del lienzo (no pinta)
    up()


# Funcion que dibuja un circulo
def circle_draw(start, end):
    "Draw square from start to end."
    # Levanta el turtle del lienzo (no pinta)
    up()

    # Mueve el turtle hacia la posición que clicquea el usuario
    goto(start.x, start.y)

    # Pone el turtle sobre el lienzo (puede pintar)
    down()

    # Se inicia el relleno de la figura
    begin_fill()

    # Funcion circle de turtle, dibuja un circulo con radio Delta x
    circle(end.x - start.x)

    # Se termina el relleno de la figura
    end_fill()

    # Levanta el turtle del lienzo(no pinta)
    up()


# Funcion que dibuja un rectangulo
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

    # Se realiza dos trazos principales del rectangulo: base y lateral
    # Guarda una relacion 1:2
    for i in range(2):
        # Se hace el trazado con el cambio en x
        forward(end.x-start.x)

        # El turtle gira 90 grados a la derecha
        right(90)

        forward((end.x-start.x)*2)
        right(90)
    # Levanta el turtle del lienzo (no pinta)
    up()

    # Termina de rellenar
    end_fill()


# Funcion que dibuja un triangulo
def triangle(start, end):
    "Draw triangle from start to end."
    # Levanta el turtle del lienzo (no pinta)
    up()

    # Mueve el turtle hacia la posición que clicquea el usuario
    goto(start.x, start.y)

    # Pone el turtle sobre el lienzo (puede pintar)
    down()

    # Se inica el rellenado de la figura
    begin_fill()

    # Se realiza el trazo principal del triangulo. Lados iguales.
    for i in range(3):
        # hace el trazado con el cambio en x
        forward(end.x - start.x)

        # Gira el turtle 120 grados a la izquierda
        left(120)
    # Termina de rellenar la figura
    end_fill()

    # Levanta el turtle del lienzo (no pinta)
    up()


# Guarda el punto donde se quiere dibujar
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
