import turtle
from player import Player
from enemy import Enemy


class Game:
    def __init__(self, window):
        self.window = window
        self.player = Player()
        self.enemies = [Enemy(x, 200) for x in range(-200, 201, 100)]
        self.is_game_over = False
        self.is_won = False

        # Keyboard bindings
        self.window.listen()
        self.window.onkeypress(self.player.move_left, "Left")
        self.window.onkeypress(self.player.move_right, "Right")
        self.window.onkeypress(self.player.shoot, "space")

    def check_collisions(self):
        # Check player bullet collisions with enemies
        for enemy in self.enemies[:]:  # Copy of the list to avoid modification during iteration
            if self.player.bullet.is_active and self.player.bullet.shape.distance(enemy.shape) < 15:
                self.player.bullet.reset()
                enemy.shape.hideturtle()

                # Reset the enemy's bullet if it's still active
                if enemy.bullet.is_active:
                    enemy.bullet.reset()

                self.enemies.remove(enemy)

        # Check if player won by eliminating all enemies
        if not self.enemies:
            self.is_won = True
            self.is_game_over = True

        # Check enemy bullet collisions with the player
        for enemy in self.enemies:
            if enemy.bullet.is_active and enemy.bullet.shape.distance(self.player.shape) < 15:
                self.is_game_over = True
                break

    def update(self):
        if not self.is_game_over:
            # Move enemies and allow them to shoot
            for enemy in self.enemies:
                enemy.move()
                enemy.try_shoot()

            # Move player bullet
            self.player.bullet.move()

            # Move enemy bullets
            for enemy in self.enemies:
                enemy.bullet.move()

            # Check for collisions
            self.check_collisions()

            # Update screen
            self.window.update()
        else:
            self.end_game()

    def end_game(self):
        message = turtle.Turtle()
        message.color("white")
        message.penup()
        message.hideturtle()
        if self.is_won:
            message.write("You Won!", align="center", font=("Arial", 24, "normal"))
        else:
            message.write("Game Over", align="center", font=("Arial", 24, "normal"))
        turtle.done()
