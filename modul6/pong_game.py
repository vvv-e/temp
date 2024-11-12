import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong game"


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.15)
        self.change_x = 3
        self.change_y = 3

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = - self.change_x
        if self.left <= 0:
            self.change_x = - self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = - self.change_y
        if self.bottom <= 0:
            self.change_y = - self.change_y


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.5)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0


class Game(arcade.Window):
    def __init__(self, width, hight, title):
        super().__init__(width, hight, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def update(self, delta_time: float):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = - self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_draw(self):
        self.clear((127, 255, 255))
        self.bar.draw()
        self.ball.draw()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2.
        self.bar.center_y = SCREEN_HEIGHT / 8.
        self.ball.center_x = SCREEN_WIDTH / 2.
        self.ball.center_y = SCREEN_HEIGHT / 2.


if __name__ == '__main__':
    windows = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
