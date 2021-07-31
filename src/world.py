import random
from collections import namedtuple, Counter
import time
import copy

CELL_DEAD = 0
CELL_ALIVE = 1


Cell = namedtuple("Cell", "x y")


class World:
    """Represent world of cells
    """

    def __init__(self, height: int, width: int) -> None:
        self.__height = height
        self.__width = width
        self.reset()

    @property
    def height(self) -> int: return self.__height

    @property
    def width(self) -> int: return self.__width

    @property
    def alive_cells_count(self) -> int: return len(self.__cells_alive)

    @property
    def alive_cells(self) -> int: return self.__cells_alive

    @classmethod
    def load_from_grid(cls, grid: list):
        """Generate a World instance from a 2-D grid

        Args:
            grid (list): non empty 2-D grid with {0,1} values

        Returns:
            [type]: World instance
        """
        rows, cols = len(grid), len(grid[0])
        instance = cls(rows, cols)
        instance.__cells_alive = [
            Cell(x, y) for x in range(cols)
            for y in range(rows)
            if grid[y][x] == CELL_ALIVE
        ]
        return instance

    def reset(self):
        """Generates a new world with random alive cells
        """
        self.__cells_alive = [
            Cell(x, y) for x in range(self.__width)
            for y in range(self.__height)
            if random.randint(0, 1) == CELL_ALIVE
        ]

    def get_neighbors(self, cell: Cell) -> list:
        res = (
            Cell(cell.x + x, cell.y + y) for x in range(-1, 2)
            for y in range(-1, 2))
        res = [cell for cell in res
               if cell.x < self.__width and cell.y < self.__height]
        res.remove(cell)
        return res

    def count_neighbors(self) -> Counter:
        return Counter(
            nb for cell in self.__cells_alive
            for nb in self.get_neighbors(cell))

    def is_cell_alive(self, x: int, y: int) -> bool:
        return (x, y) in self.__cells_alive

    def next_generation_apply(self):
        start = time.perf_counter()
        tmp = rest = self.count_neighbors()
        end = time.perf_counter()
        print(f'Get - 2: {end - start: 0.4f} secs')
        alive = copy.deepcopy(self.__cells_alive)
        self.__cells_alive = [
            cell for cell in tmp
            if (rest[cell] == 3) or (rest[cell] == 2 and cell in alive)]

    def __len__(self) -> int:
        return self.__height * self.__width

    def __str__(self) -> str:
        def row(y): return ''.join(
            str(CELL_ALIVE) if (x, y) in self.__cells_alive
            else str(CELL_DEAD) for x in range(self.__width))
        return '\n'.join(row(y) for y in range(self.__height))
