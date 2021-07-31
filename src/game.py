import pygame as pg
import sys
import time
from world import World

CELL_SIZE = 10
NB_COL = int(1920/CELL_SIZE)
NB_ROW = int(1040/CELL_SIZE)

BOARD_BACK_COLOR = 'black'
BOARD_LINE_COLOR = '#121212'
ALIVE_CELL_COLOR = 'red'
FONT_COLOR = 'red'


class Game:
    FPS = 60

    def __init__(self) -> None:
        self.__paused = False
        self.__display_grid = True
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

        while True:

            for event in pg.event.get():
                self.process_events(event)

            if not self.__paused:
                self.__cycle += 1
                start = time.perf_counter()
                self.__world.next_generation_apply()
                end = time.perf_counter()
                print(f'Time: {end - start: 0.4f} secs')

            self.__clock.tick(self.FPS)
            self.redraw()

    def process_events(self, event) -> None:
        if event.type == pg.QUIT:
            self.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.exit()
            elif event.key == pg.K_PAUSE:
                self.pause_pressed()
            elif event.key == pg.K_g:
                self.__display_grid = not self.__display_grid
            elif event.key == pg.K_r:
                self.reset()

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

        if self.__display_grid:
            for x in range(self.__world.width+1):
                pg.draw.line(world_surf, BOARD_LINE_COLOR, (x * CELL_SIZE, 0), (x * CELL_SIZE, world_rect.height))
            for y in range(self.__world.height+1):
                pg.draw.line(world_surf, BOARD_LINE_COLOR, (0, y * CELL_SIZE), (world_rect.width, y * CELL_SIZE))

        self.__screen.blit(world_surf, world_rect)

    def draw_information(self):
        total = len(self.__world)
        alive = self.__world.alive_cells_count
        fps = int(self.__clock.get_fps())
        text_y = 5
        grid_state = 'ON' if self.__display_grid else 'OFF'
        self.draw_text(f'Cells: {total}', (10, text_y))
        self.draw_text(f'| Alive: {alive}', (100, text_y))
        self.draw_text(f'| Dead: {total-alive}', (200, text_y))
        self.draw_text(f'| FPS: {fps}', (300, text_y))
        self.draw_text(f'| Display Grid: {grid_state}', (450, text_y))
        self.draw_text(f'| Cycle: {self.__cycle}', (600, text_y))

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
