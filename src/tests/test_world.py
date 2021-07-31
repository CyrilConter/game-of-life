import pytest
from world import CELL_ALIVE, World, Cell


def test_size_properties():
    world = World(100, 50)
    assert world.height == 100, 'Height failed'
    assert world.width == 50, 'Width failed'
    assert len(world) == 5000, 'Size failed'


def test_str():
    grid = [[1, 1, 0], [1, 0, 1]]
    world = World.load_from_grid(grid)
    expected = '110\n101'
    assert str(world) == expected, 'Error converting World to string'


@pytest.mark.parametrize('grid', [
    [[0, 0, 0], [0, 1, 0], [0, 0, 0], [1, 1, 1]],
    [[0]]
])
def test_load_from_list(grid: list):
    world = World.load_from_grid(grid)

    # Checks size of generated world
    assert world.height == len(grid)
    assert world.width == len(grid[0])
    assert len(world) == len(grid) * len(grid[0])
    alive_cells_count = sum(row.count(CELL_ALIVE) for row in grid)
    assert alive_cells_count == world.alive_cells_count

    # Checks cells states according original grid
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            assert grid[y][x] == world.is_cell_alive(x, y), \
                    f'Bad loading on cell (x= {x}, y={y})'


def test_count_neighbours():
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    world = World.load_from_grid(grid)
    count = world.count_neighbors()
    assert count[Cell(1, 1)] == 0, 'Count neighbours KO'


@pytest.mark.parametrize('grid, expected', [
    ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], '000\n000\n000'),
    ([[1, 1, 1], [0, 0, 0], [0, 0, 0]], '010\n010\n000'),
    ([[0, 0, 0], [1, 1, 1], [0, 0, 0]], '010\n010\n010'),
    ([[1, 0, 0], [1, 1, 1], [1, 0, 0]], '100\n100\n100')
])
def test_next_generation(grid: list, expected: str):
    world = World.load_from_grid(grid)
    world.next_generation_apply()
    assert str(world) == expected, 'Error on updating world'
