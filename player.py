import turtle
from bullet import Bullet

PLAYER_SPEED = 15


class Player:
    def __init__(self):
        self.shape = turtle.Turtle()
        self.shape.color("blue")
        self.shape.shape("triangle")
        self.shape.penup()
        self.shape.setheading(90)
        self.shape.goto(0, -250)
        self.bullet = Bullet(owner="player")

    def move_left(self):
        x = self.shape.xcor() - PLAYER_SPEED
        if x < -280:
            x = -280
        self.shape.setx(x)

    def move_right(self):
        x = self.shape.xcor() + PLAYER_SPEED
        if x > 280:
            x = 280
        self.shape.setx(x)

    def shoot(self):
        if not self.bullet.is_active:
            self.bullet.fire(self.shape.xcor(), self.shape.ycor() + 10)
