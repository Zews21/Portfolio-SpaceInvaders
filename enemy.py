import turtle
import random
from bullet import Bullet

ENEMY_SPEED = 2


class Enemy:
    def __init__(self, x, y):
        self.shape = turtle.Turtle()
        self.shape.color("red")
        self.shape.shape("circle")
        self.shape.penup()
        self.shape.speed(0)
        self.shape.goto(x, y)
        self.direction = 1  # 1 means moving right, -1 means moving left
        self.bullet = Bullet(owner="enemy")

    def move(self):
        x = self.shape.xcor() + (ENEMY_SPEED * self.direction)
        if x > 280 or x < -280:
            self.direction *= -1
            x = self.shape.xcor() + (ENEMY_SPEED * self.direction)
        self.shape.setx(x)

    def try_shoot(self):
        if not self.bullet.is_active and random.randint(0, 100) < 2:
            self.bullet.fire(self.shape.xcor(), self.shape.ycor() - 10)
