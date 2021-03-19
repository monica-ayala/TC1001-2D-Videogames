"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

from random import randrange
from turtle import done, onscreenclick, tracer, up, hideturtle, setup
from turtle import ontimer, update, dot, goto, clear
from freegames import vector

# Se declaran las variables
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


# Se detecta los clicks que se hagan en la pantalla
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        # Define el area de la pantalla donde la pelota
        # puede existir
        ball.x = -199
        ball.y = -199
        speed.x = (x + 400) / 25
        speed.y = (y + 400) / 25


# Revisa que la pelota esta en la pantalla
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200


# Dibuja la pelota y los targets
def draw():
    "Draw ball and targets."
    clear()

    # Se señala la coordenada en la cual se dibujan los targets
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    # Se señala la coordernada en la cual se dibuja la pelota
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


# Revisa como funciona el movimiento de la pelota y los targets
def move():
    "Move ball and targets."
    # Se genera la coordenada del target de manera aleatoria
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Indica la velocidad del target de derecha a izquierda
    for target in targets:
        # Velocidad es aleatoria para los targets
        target.x -= randrange(1, 4)

    # Indica la velocidad de la pelota de izquierda a derecha
    if inside(ball):
        speed.y -= 0.2
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    # Copia los targets que no se usaron
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
