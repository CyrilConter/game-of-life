import pygame as pg
import sys
# from world import World


class Game:

    def __init__(self) -> None:
        self.__running = False
        pg.init()
        pg.display.set_caption("Game Of Life")
        pg.display.set_mode((400, 400))

    def run(self) -> None:

        timer = pg.time.Clock()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.exit()

            pg.display.update()
            timer.tick(60)

    def exit(self) -> None:
        pg.quit()
        sys.exit()


def main() -> None:
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
