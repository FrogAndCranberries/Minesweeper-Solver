import numpy as np
from scipy.signal import convolve2d

class MinesweeperGame:
    def __init__(self, height, width, mine_count):
        assert(mine_count <= height * width)
        self.h = height
        self.w = width
        self.mine_count = mine_count
        
        self.mines = self._init_mines()
        self.field = self._init_field()
        self.uncovered = np.full((height, width), fill_value=False)

    def _init_mines(self):
        mines = np.zeros((self.h, self.w), dtype=np.int8)
        mine_indices = np.random.choice(self.h * self.w, replace=False, size=self.mine_count)
        mines[np.unravel_index(mine_indices, shape=self.mines.shape)] = 1
        return mines

    def _init_field(self):
        neighbor_kernel = np.ones((3,3), dtype=np.int8)
        neighbor_kernel[1,1] = 0
        print(self.mines.shape)
        field = convolve2d(self.mines, neighbor_kernel, mode="same")
        field[self.mines == 1] = -1
        return field


if __name__ == "__main__":
    game = MinesweeperGame(5, 10, 15)
    print(game.mines)
    print(game.field)
