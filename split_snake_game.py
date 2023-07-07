import turtle
import random
import time

screen = turtle.Screen()
screen.title('DATAFLAIR-SNAKE GAME')
screen.setup(width=700, height=700)
screen.tracer(0)
turtle.bgcolor('black')

turtle.speed(0)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color('cyan')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

score = 0
delay = 0.1

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("lime")  # Change snake 1 head color to lime
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30, 30)

snake_parts_1 = []
snake_parts_2 = []

scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("pink")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score :", align="center", font=("Courier", 24, "bold"))


def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

while True:
    screen.update()

    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))

        new_part_1 = turtle.Turtle()
        new_part_1.speed(0)
        new_part_1.shape('square')
        new_part_1.color('green')  # Change snake 1 body color to green
        new_part_1.penup()
        snake_parts_1.append(new_part_1)

        new_part_2 = turtle.Turtle()
        new_part_2.speed(0)
        new_part_2.shape('square')
        new_part_2.color('purple')  # Change snake 2 body color to purple
        new_part_2.penup()
        snake_parts_2.append(new_part_2)

    for index in range(len(snake_parts_1) - 1, 0, -1):
        x = snake_parts_1[index - 1].xcor()
        y = snake_parts_1[index - 1].ycor()
        snake_parts_1[index].goto(x, y)

    if len(snake_parts_1) > 0:
        x = snake.xcor()
        y = snake.ycor()
        snake_parts_1[0].goto(x, y)

    for index in range(len(snake_parts_2) - 1, 0, -1):
        x = snake_parts_2[index - 1].xcor()
        y = snake_parts_2[index - 1].ycor()
        snake_parts_2[index].goto(x, y)

    if len(snake_parts_2) > 0:
        x = -snake.xcor()
        y = -snake.ycor()
        snake_parts_2[0].goto(x, y)
        snake_parts_2[0].setheading(snake.heading())

    snake_move()

    if (
        snake.xcor() > 280
        or snake.xcor() < -300
        or snake.ycor() > 240
        or snake.ycor() < -240
    ):
        time.sleep(1)
        screen.clear()
        screen.bgcolor('turquoise')
        scoring.goto(0, 0)
        scoring.write(
            "   GAME OVER \n Your Score is {}".format(score),
            align="center",
            font=("Courier", 30, "bold"),
        )
        break

    for part in snake_parts_1:
        if part.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0, 0)
            scoring.write(
                "    GAME OVER \n Your Score is {}".format(score),
                align="center",
                font=("Courier", 30, "bold"),
            )
            break

    for part in snake_parts_2:
        if part.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0, 0)
            scoring.write(
                "    GAME OVER \n Your Score is {}".format(score),
                align="center",
                font=("Courier", 30, "bold"),
            )
            break

    for part in snake_parts_1:
        if part.distance(snake_parts_2[0]) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0, 0)
            scoring.write(
                "    GAME OVER \n Your Score is {}".format(score),
                align="center",
                font=("Courier", 30, "bold"),
            )
            break

    time.sleep(delay)
