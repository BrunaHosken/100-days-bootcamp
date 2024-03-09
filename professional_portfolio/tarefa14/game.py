# game.py

import turtle
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Space Invaders")
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

        self.player = Player()
        self.enemies = []
        self.bullets = []
        self.score = 0

        self.game_over_display = turtle.Turtle()
        self.score_display = turtle.Turtle()

        self.screen.listen()
        self.screen.onkey(self.player.move_left, "Left")
        self.screen.onkey(self.player.move_right, "Right")
        self.screen.onkey(self.player.move_up, "Up")
        self.screen.onkey(self.shoot_bullet, "space")

        self.spawn_wave()

    def shoot_bullet(self):
        bullet = self.player.shoot()
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()

            for enemy in self.enemies:
                if bullet.is_collision(enemy.enemy):
                    enemy.enemy.hideturtle()
                    self.enemies.remove(enemy)
                    bullet.bullet.hideturtle()
                    self.bullets.remove(bullet)
                    self.score += 1
                    self.update_score_display()

            if bullet.bullet.ycor() > 300:
                bullet.bullet.hideturtle()
                self.bullets.remove(bullet)

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update()
            if self.is_collision(enemy.enemy, self.player.player):
                self.game_over()
                return

        if not self.enemies:
            self.spawn_wave()

        if any(enemy.enemy.ycor() < -250 for enemy in self.enemies):
            self.spawn_new_wave()

    def spawn_wave(self):
        num_enemies = 3 + len(self.enemies)  # Increase the number of enemies for each new wave
        self.enemies = [Enemy(x, 250) for x in range(-200, (num_enemies - 1) * 100, 100)]

    def spawn_new_wave(self):
        for enemy in self.enemies:
            enemy.enemy.goto(enemy.enemy.xcor(), 250)

    def is_collision(self, obj1, obj2):
        distance = obj1.distance(obj2)
        return distance < 20  # Adjust the collision threshold as needed

    def game_over(self):
        self.game_over_display.hideturtle()
        self.game_over_display.color("red")
        self.game_over_display.penup()
        self.game_over_display.goto(0, 0)
        self.game_over_display.write("Game Over", align="center", font=("Arial", 24, "normal"))

        self.score_display.hideturtle()
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.goto(0, -30)
        self.score_display.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))

        self.screen.update()
        turtle.mainloop()  # Keep the window open after game over

    def update_score_display(self):
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))

    def run(self):
        while True:
            self.screen.update()

            self.player.update()
            self.update_bullets()
            self.update_enemies()

if __name__ == "__main__":
    game = Game()

    game.run()
