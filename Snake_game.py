# Snake game

import turtle
import random
import time


# creating screeen
screen = turtle.Screen()
screen.title("Screen Game")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# creating border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-250, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(500)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# Score
score = 0
delay = 0.1

# Snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.penup()
food.goto(30, 30)

old_food = []

# Scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: ", align="center", font=("Courier", 24, "bold"))

# define how to move


def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"


def move():
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


# Keyboard binding
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# Main loop
while True:
    try:
        screen.update()

        # snake & food colition
        if snake.distance(food) < 20:
            while True:
                x = random.randint(-240, 240)
                y = random.randint(-240, 240)
                food.goto(x, y)
                if len(old_food) == 0:
                    break
                else:
                    xxx = 0
                    for number1 in range(len(old_food)):
                        if old_food[number1].distance(food) < 20:
                            xxx += 1
                    if xxx == 0:
                        break

            scoring.clear()
            score += 1
            scoring.write(f"Score: {score}", align="center",
                          font=("Courier", 24, "bold"))
            # creating new foods
            new_food1 = turtle.Turtle()
            new_food1.speed(0)
            new_food1.shape("square")
            new_food1.color("red")
            new_food1.penup()
            old_food.append(new_food1)

        # Adding ball to the snake
        for index in range(len(old_food)-1, 0, -1):
            a = old_food[index-1].xcor()
            b = old_food[index-1].ycor()

            old_food[index].goto(a, b)
        if len(old_food) > 0:
            a = snake.xcor()
            b = snake.ycor()
            old_food[0].goto(a, b)
        move()

        # snake & border colition
        if snake.xcor() > 240 or snake.xcor() < -240 or snake.ycor() > 240 or snake.ycor() < -240:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write(f"     Game Over \n Your score is : {
                score}", align="center", font=("Courier", 30, "bold"))
        for segmant in old_food:
            if segmant.distance(snake) < 20:
                time.sleep(1)
                screen.clear()
                screen.bgcolor("turquoise")
                scoring.goto(0, 0)
                scoring.write(f"     Game Over \n Your score is : {
                    score}", align="center", font=("Courier", 30, "bold"))
        time.sleep(delay)  # Pause to control the speed of the game
    except:
        break
