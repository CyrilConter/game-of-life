import pytest
from world import World, Cell


def test_size_properties():
    world = World(100, 50)
    assert world.height == 100, 'Height failed'
    assert world.width == 50, 'Width failed'
    assert len(world) == 5000, 'Size failed'


def test_str():
    grid = [[1, 1, 0], [1, 0, 1]]
    world = World.load_from(grid)
    expected = '110\n101'
    assert str(world) == expected, 'Error converting World to string'


@pytest.mark.parametrize('grid', [
    [[0, 0, 0], [0, 1, 0], [0, 0, 0], [1, 1, 1]],
    [[0]]
])
def test_load_from_list(grid: list):
    world = World.load_from(grid)

    # Checks size of generated world
    assert world.height == len(grid)
    assert world.width == len(grid[0])
    assert len(world) == len(grid) * len(grid[0])

    # Checks cells states according original grid
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            assert grid[y][x] == world.is_cell_alive(x, y), \
                    f'Bad loading on cell (x= {x}, y={y})'


def test_count_neighbours():
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    world = World.load_from(grid)
    assert world.count_neighbors(Cell(0, 1)) == 1, 'Count neighbours KO'


def test_next_generation():
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    world = World.load_from(grid)
    world.next_generation_apply()
    expected = '000\n000\n000'
    assert str(world) == expected, 'Error on updating world'
