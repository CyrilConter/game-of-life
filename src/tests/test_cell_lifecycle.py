import pytest
from board import CELL_ALIVE, CELL_DEAD, Cell


@pytest.mark.parametrize('dest_desc, initial_value, expected_state', [
    ('Cell alive', CELL_ALIVE, True),
    ('Dead cell', CELL_DEAD, False)
])
def test_cell_state(dest_desc: str, initial_value: int, expected_state: bool):
    cell = Cell(initial_value)
    assert cell.is_alive() == expected_state, f'{dest_desc} failed'


@pytest.mark.parametrize(
    'dest_desc, initial_state, neighbor_count, expected_state',
    [
        ('Alive - 0 neighbor', CELL_ALIVE, 0, CELL_DEAD),
        ('Alive - 1 neighbor', CELL_ALIVE, 1, CELL_DEAD),
        ('Alive - 2 neighbors', CELL_ALIVE, 2, CELL_ALIVE),
        ('Alive - 3 neighbors', CELL_ALIVE, 3, CELL_ALIVE),
        ('Alive - 4 neighbors', CELL_ALIVE, 4, CELL_DEAD),
        ('Alive - 5 neighbors', CELL_ALIVE, 5, CELL_DEAD),
        ('Alive - 6 neighbors', CELL_ALIVE, 6, CELL_DEAD),
        ('Alive - 7 neighbors', CELL_ALIVE, 7, CELL_DEAD),
        ('Alive - 8 neighbors', CELL_ALIVE, 8, CELL_DEAD),
        ('Dead - 0 neighbor', CELL_DEAD, 0, CELL_DEAD),
        ('Dead - 1 neighbor', CELL_DEAD, 1, CELL_DEAD),
        ('Dead - 2 neighbors', CELL_DEAD, 2, CELL_DEAD),
        ('Dead - 3 neighbors', CELL_DEAD, 3, CELL_ALIVE),
        ('Dead - 4 neighbors', CELL_DEAD, 4, CELL_DEAD),
        ('Dead - 5 neighbors', CELL_DEAD, 5, CELL_DEAD),
        ('Dead - 6 neighbors', CELL_DEAD, 6, CELL_DEAD),
        ('Dead - 7 neighbors', CELL_DEAD, 7, CELL_DEAD),
        ('Dead - 8 neighbors', CELL_DEAD, 8, CELL_DEAD)]
)
def test_cell_updatestate(dest_desc: str, initial_state: int,
                          neighbor_count: int, expected_state: bool):
    cell = Cell(initial_state)
    cell.update_state(neighbor_count)
    assert cell.is_alive() == expected_state, f'{dest_desc} failed'
