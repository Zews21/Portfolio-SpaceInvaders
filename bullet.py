import turtle

# Default bullet speeds
PLAYER_BULLET_SPEED = 15
ENEMY_BULLET_SPEED = 5


class Bullet:
    def __init__(self, owner):
        self.shape = turtle.Turtle()
        self.shape.color("yellow" if owner == "player" else "orange")
        self.shape.shape("square")
        self.shape.shapesize(0.5, 0.5)
        self.shape.penup()
        self.shape.hideturtle()
        self.owner = owner
        self.is_active = False
        # Set bullet speed based on owner type
        self.speed = PLAYER_BULLET_SPEED if owner == "player" else ENEMY_BULLET_SPEED

    def fire(self, x, y):
        if not self.is_active:
            self.shape.goto(x, y)
            self.shape.showturtle()
            self.is_active = True

    def move(self):
        if self.is_active:
            y = self.shape.ycor() + (self.speed if self.owner == "player" else -self.speed)
            self.shape.sety(y)
            if y > 280 or y < -280:
                self.reset()

    def reset(self):
        self.shape.hideturtle()
        self.is_active = False
