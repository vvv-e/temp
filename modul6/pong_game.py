import arcade

class Game(arcade.Window):
    def on_draw(self):
        self.clear((127,255,127))

if __name__ == '__main__':
    windows = Game()
    arcade.run()
