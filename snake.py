"""Snake, classic arcade game.
Exercises
1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.
"""

from turtle import update, clear, ontimer, setup
from turtle import hideturtle, tracer, listen, onkey, done
from random import randrange
from freegames import square, vector

# Se declaran las variables
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
color_body = ""
color_food = ""


# Se indentifica la dirección a la que apunta el snake
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


# Se cerciorar que la cabeza esté dentro de la pantalla
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


# Movimientos de la serpiente y comida
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    # Se crea una nueva coordenada donde la comida
    # corre +-1 en todas direcciones mientras la cabeza
    # no toque la coordernada de la comida
    k = int(food.x/10)
    c = int(food.y/10)
    food.x = randrange(-1+k, 2+k) * 10
    food.y = randrange(-1+c, 2+c) * 10

    clear()

    for body in snake:
        square(body.x, body.y, 9, color[0])

    square(food.x, food.y, 9, color[1])
    update()
    ontimer(move, 250)


# Se indican los colores con los que aparece la serpiente y la comida
def color():
    color_list1 = ['blue', 'green', 'brown', 'yellow', 'purple']
    color_list2 = ['black', 'cyan', 'orange', 'pink', 'violet']

    # El color es random cada vez que inicias el juego
    color_body = color_list1[randrange(0, 4)]
    color_food = color_list2[randrange(0, 4)]
    return color_body, color_food


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
color()
color = color()
move()
done()
