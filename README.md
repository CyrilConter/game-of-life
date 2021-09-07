# Conway's Game of Life
Implementation of [Conway's Game of Life](http://en.wikipedia.org/wiki/Conway's_Game_of_Life) in Python using [PyGame](https://www.pygame.org/) library for visual rendering.

The Game of Life is a zero-player game. It is defined by an universe: a 2-D grid of cells, where each cell is in one of 2 possible states : living or dead.
According an initial configuration (seed) of the universe, the game will make evolve the universe by applying the following rules :
1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The Wikipedia page [Conway's Game of Life](http://en.wikipedia.org/wiki/Conway's_Game_of_Life) give more information, and examples of patterns related to this topic.
<br /><br />

![Github workflow](https://github.com/CyrilConter/game-of-life/actions/workflows/python_app.yml/badge.svg)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=CyrilConter_game-of-life&metric=ncloc)](https://sonarcloud.io/dashboard?id=CyrilConter_game-of-life)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=CyrilConter_game-of-life&metric=coverage)](https://sonarcloud.io/dashboard?id=CyrilConter_game-of-life)
## Getting started
### Requirements
* Python: v3.9 [Download](https://www.python.org/downloads/)
* Dependency: [PyGame](https://www.pygame.org/)
```bash
pip install pygame
```
### Clone code
```bash
git clone https://github.com/CyrilConter/game-of-life.git
cd game-of-life/src
```
### Launch tests
```bash
pytest --no-header -v
```
Output
```bash
================================================= test session starts =================================================
collected 9 items

tests/test_world.py::test_size_properties PASSED                                                                 [ 11%]
tests/test_world.py::test_str PASSED                                                                             [ 22%]
tests/test_world.py::test_load_from_list[grid0] PASSED                                                           [ 33%]
tests/test_world.py::test_load_from_list[grid1] PASSED                                                           [ 44%]
tests/test_world.py::test_count_neighbours PASSED                                                                [ 55%]
tests/test_world.py::test_next_generation[grid0-000\n000\n000] PASSED                                            [ 66%]
tests/test_world.py::test_next_generation[grid1-010\n010\n000] PASSED                                            [ 77%]
tests/test_world.py::test_next_generation[grid2-010\n010\n010] PASSED                                            [ 88%]
tests/test_world.py::test_next_generation[grid3-100\n100\n100] PASSED                                            [100%]

================================================== 9 passed in 0.05s ==================================================
```
### Launch application
```bash
python game.py
```
This will launch the application with default configuration.
## Controls
The following keybinds are avaialble:
* `r` - Randomize the grid
* `g` - Display/Hide grid lines
* `p` - Pause/Resume game
* `q` - Quit
## What I've learned ?
* Practice Python and first unit testint using [pytest](https://docs.pytest.org/)
* Use GitHub: source control, actions...
* Test basic integration of [Sonarcloud](https://sonarcloud.io/) with GitHub
## Possible improvements
* Performance improvement: with large grid (> 10,000 cells) the game is slow (< 15 FPS).\
Probably some code needs to be improved to get better performances.
* Allow user to load predefined configurations of universe (seeds)
* Display cells with different colors according life state: 
    * born
    * alive and will stay alive at next cycle
    * alive but will die at next cycle