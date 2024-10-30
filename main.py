from game import Game
import turtle
import time

# Set up the screen
window = turtle.Screen()
window.title("Space Invaders")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# Initialize the game
game = Game(window)

# Main game loop
while True:
    game.update()
    if game.is_game_over:
        game.end_game()
        break
    time.sleep(0.02)
