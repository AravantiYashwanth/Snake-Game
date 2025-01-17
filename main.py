from turtle import Turtle ,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
ALIGN = "center"
FONT = ('courier', 20, 'normal')

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


screen.textinput("Welcome to Snake Game", "Press OK to play and then press 'space' to start the game")


def run():
    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")


    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detect collision with food
        if snake.head.distance(food) < 15 :
            food.refresh()
            snake.extend()
            score.increase_score()

        #detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
            game_is_on = False
            score.game_over()
        
        #detect collision with tail
        for segment in snake.segments[1:]:

            if snake.head.distance(segment) < 10 :  
                game_is_on = False
                score.game_over()               
                

# Bind the space key to start the game
screen.listen()
screen.onkey(run, "space")

# Main loop
screen.mainloop()