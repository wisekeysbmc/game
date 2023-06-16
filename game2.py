import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Пример игры")
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.player = arcade.Sprite("D:\Code\CBeTbl\Igra\game2\Player.png")
        self.player.center_x = width // 9
        self.player.center_y = height // 9

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def update(self, delta_time):
        self.player.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED



    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
