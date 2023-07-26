from turtle import Screen
from paddle import Paddle
from ball import  Ball
import time
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.tracer(0)
first_paddle = Paddle((350, 0))
second_paddle = Paddle((-350, 0))
the_ball = Ball()
is_working = True


while is_working:
    time.sleep(0.1)
    my_screen.update()
    the_ball.move()



    if the_ball.ycor() > 280 or the_ball.ycor() < -280:
        the_ball.bounce()

    if the_ball.distance(first_paddle) < 25 and the_ball.xcor() > 320 \
            or the_ball.distance(second_paddle) < 25 and the_ball.xcor() < -320:
        the_ball.penetrate()
    elif the_ball.xcor() > 380 or the_ball.xcor() < - 380:
    #    is_working = False
        the_ball.reset()
        first_paddle.reset()
        second_paddle.reset()


    my_screen.listen()
    my_screen.onkey(first_paddle.up,"Up")
    my_screen.onkey(first_paddle.down,"Down")
    my_screen.onkey(second_paddle.up,"")
    my_screen.onkey(second_paddle.down,"s")




my_screen.exitonclick()