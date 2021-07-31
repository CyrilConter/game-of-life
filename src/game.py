import pygame as pg
import sys
import time
from world import World

CELL_SIZE = 10
NB_COL = int(1920/CELL_SIZE)
NB_ROW = int(1040/CELL_SIZE)

BOARD_BACK_COLOR = 'black'
BOARD_LINE_COLOR = 'black'
ALIVE_CELL_COLOR = 'white'
FONT_COLOR = 'red'


class Game:
    FPS = 60

    def __init__(self) -> None:
        self.__paused = False
        self.__cycle = 0
        self.__world = World(NB_ROW, NB_COL)

        pg.init()
        # self.SCREEN_UPDATE = pg.USEREVENT
        # pg.time.set_timer(self.SCREEN_UPDATE, 1)
        self.__clock = pg.time.Clock()
        pg.display.set_caption("Game Of Life")
        pg.display.set_mode((1920, 1200))
        self.__screen = pg.display.set_mode((1920, 1200))

    def run(self) -> None:
        display_grid = True

        while True:
            self.__cycle += 1

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        exit()
                    elif event.key == pg.K_PAUSE:
                        self.pause_pressed()
                    elif event.key == pg.K_g:
                        display_grid = not display_grid
                    elif event.key == pg.K_r:
                        self.reset()

            if not self.__paused:
                start = time.perf_counter()
                self.__world.next_generation_apply()
                end = time.perf_counter()
                print(f'Time: {end - start: 0.4f} secs')

            self.__clock.tick(self.FPS)
            self.redraw()

    def reset(self) -> None:
        self.__cycle = 0
        self.__world.reset()

    def pause_pressed(self) -> None:
        self.__paused = not self.__paused
        pg.display.set_caption(
            "Game Of Life (PAUSED)"
            if self.__paused else "Game Of Life")

    def redraw(self) -> None:
        self.__screen.fill(pg.Color(BOARD_BACK_COLOR))
        self.draw_world()
        self.draw_information()
        pg.display.flip()

    def draw_world(self, y_padding: int = 0) -> None:
        world_surf = pg.Surface((
            self.__world.width * CELL_SIZE,
            self.__world.height * CELL_SIZE))

        for cell in self.__world.alive_cells:
            rect = pg.Rect(
                cell.x * CELL_SIZE,
                cell.y * CELL_SIZE,
                CELL_SIZE, CELL_SIZE)
            pg.draw.rect(world_surf, pg.Color(ALIVE_CELL_COLOR), rect)

        screen_rect = self.__screen.get_rect()
        world_rect = world_surf.get_rect(center=(screen_rect.center))
        self.__screen.blit(world_surf, world_rect)

    def draw_information(self):
        total = len(self.__world)
        alive = self.__world.alive_cells_count
        fps = int(self.__clock.get_fps())
        text_y = 5

        self.draw_text(f'Cells : {total}', (10, text_y))
        self.draw_text(f'| Alive: {alive}', (100, text_y))
        self.draw_text(f'| Dead : {total-alive}', (200, text_y))
        self.draw_text(f'| FPS : {fps}', (300, text_y))
        self.draw_text(f'| Cycle : {self.__cycle}', (600, text_y))

    def draw_text(self, msg: str, pos: tuple):
        font = pg.font.SysFont('comicsans', 20)
        text = font.render(msg, 1, FONT_COLOR)
        self.__screen.blit(text, (pos[0], pos[1]))

    def exit(self) -> None:
        pg.quit()
        sys.exit()


def main() -> None:
    game = Game()
    game.run()
    sys.exit()


if __name__ == "__main__":
    main()
