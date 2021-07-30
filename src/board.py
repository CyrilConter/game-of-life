CELL_DEAD = False
CELL_ALIVE = True


class Cell:

    def __init__(self, state: int) -> None:
        self.__state = state

    def is_alive(self) -> bool:
        return self.__state != CELL_DEAD

    def get_state(self) -> int:
        return self.__state

    def set_state(self, state: int) -> None:
        self.__state = state

    def update_state(self, nb_alive_neighbor: int) -> None:
        if self.is_alive() and (
                nb_alive_neighbor == 2 or nb_alive_neighbor == 3):
            self.__state = CELL_ALIVE
        elif not self.is_alive() and nb_alive_neighbor == 3:
            self.__state = CELL_ALIVE
        else:
            self.__state = CELL_DEAD
