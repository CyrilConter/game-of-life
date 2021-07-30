import random
from collections import namedtuple

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

    @classmethod
    def load_from(cls, grid: list):
        rows, cols = len(grid), len(grid[0])
        o = cls(rows, cols)
        o.__cells_alive = [
            Cell(x, y) for x in range(cols)
            for y in range(rows)
            if grid[y][x] == CELL_ALIVE
        ]
        return o

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

    def count_neighbors(self, cell: Cell) -> int:
        neighbors = self.get_neighbors(cell)
        return sum(1 for x in neighbors if x in self.__cells_alive)

    def is_cell_alive(self, x: int, y: int) -> bool:
        return (x, y) in self.__cells_alive

    def next_generation_apply(self):
        rest = {cell: self.count_neighbors(cell)
                for cell in self.__cells_alive}
        self.__cells_alive = [
            k for k, v in rest.items()
            if (v == 3) or (v == 2 and k in self.__cells_alive)]

    def __len__(self) -> int:
        return self.__height * self.__width

    def __str__(self) -> str:
        def row(y): return ''.join(
            str(CELL_ALIVE) if (x, y) in self.__cells_alive
            else str(CELL_DEAD) for x in range(self.__width))
        return '\n'.join(row(y) for y in range(self.__height))
