"""Paint, for drawing shapes.
Exercises
1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import up, goto, down, begin_fill, forward, left, setup, circle
from turtle import end_fill, onscreenclick, listen, onkey, undo, color, done, setposition
from freegames import vector


def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle_draw(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    circle(end.x - start.x)
    
    end_fill()
    

def rectangle(start, end):
    "Draw rectangle from start to end."
    pass  # TODO


def triangle(start, end):
    "Draw triangle from start to end."
    pass  # TODO


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
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle_draw), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
