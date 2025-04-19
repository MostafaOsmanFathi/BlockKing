from time import sleep

import grid
from grid import Grid
from player import Player
from CONSTANTS import *


class Game_Manger:
    player_respawn_positions = [(1, 1), (1, M_CELLS - 2), (N_CELLS - 2, 1), (N_CELLS - 2, M_CELLS - 2)]

    def __init__(self):
        self.grid = Grid()
        self.grid.draw_grid(N_CELLS, M_CELLS)
        self.grid.screen.listen()
        self.player_list = []

    def add_player(self, color, position, keyboard_set=0):
        if position >= 0 and position < 4:
            self.player_list.append(
                Player(color, self.grid, *Game_Manger.player_respawn_positions[position], keyboard_set))
            x, y = Game_Manger.player_respawn_positions[position]
            self.grid.grid[x][y].set_owner(self.player_list[-1])
            self.grid.grid[x][y].set_owner(self.player_list[-1])

    def dfs(self, grid, player, x, y):
        if x >= N_CELLS or x < 0 or y >= M_CELLS or y < 0:
            return False
        res = False
        if grid[x][y].cell_full_owner == player:
            res = True

        res |= self.dfs(grid, player, x + 1, y)
        if res:
            grid[x][y].set_full_owner(player)
        return res

    def graph_fill(self, player: Player):
        for i in range(M_CELLS):
            self.dfs(self.grid.grid, player, 0, i)

    def start_game(self):
        is_game_running = True
        while is_game_running:
            for player in self.player_list:
                if player.start_moving and player.can_move():
                    player.move()
                    if self.grid.grid[player.x_cell_poss][player.y_cell_poss].cell_full_owner == player:
                        player.fill_cells()
                        self.graph_fill(player)
                    self.grid.grid[player.x_cell_poss][player.y_cell_poss].set_owner(player)

            self.grid.screen.update()
            sleep(UPDATE_RATE)
