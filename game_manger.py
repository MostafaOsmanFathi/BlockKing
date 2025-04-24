from time import sleep

import turtle_camera
from CONSTANTS import *
from camera import Camera
from grid import Grid
from player import Player


class Game_Manger:
    player_respawn_positions = [(1, 1), (1, M_CELLS - 2), (N_CELLS - 2, 1), (N_CELLS - 2, M_CELLS - 2)]

    def __init__(self, camera_idx=0):
        self.grid = Grid()
        self.grid.draw_grid(N_CELLS, M_CELLS)
        self.grid.screen.listen()
        self.player_list = []
        self.camera_on_player_idx = camera_idx
        self.camera_obj = None

    def add_player(self, color, position, keyboard_set=0):
        if position >= 0 and position < 4:
            self.player_list.append(
                Player(color, self.grid, *Game_Manger.player_respawn_positions[position], keyboard_set))
            x, y = Game_Manger.player_respawn_positions[position]
            self.grid.grid[x][y].set_full_owner(self.player_list[-1])

            self.grid.grid[x - 1][y - 1].set_full_owner(self.player_list[-1])
            self.grid.grid[x - 1][y].set_full_owner(self.player_list[-1])
            self.grid.grid[x][y - 1].set_full_owner(self.player_list[-1])
            self.grid.grid[x + 1][y].set_full_owner(self.player_list[-1])
            self.grid.grid[x + 1][y - 1].set_full_owner(self.player_list[-1])
            self.grid.grid[x + 1][y + 1].set_full_owner(self.player_list[-1])
            self.grid.grid[x][y + 1].set_full_owner(self.player_list[-1])
            self.grid.grid[x - 1][y + 1].set_full_owner(self.player_list[-1])

    def dfs(self, grid, player, x, y, start=False):
        if x >= N_CELLS or x < 0 or y >= M_CELLS or y < 0:
            return False
        res = False
        if grid[x][y].cell_full_owner == player:
            res = True

        res |= self.dfs(grid, player, x + 1, y, res | start)
        if res and start:
            grid[x][y].set_full_owner(player)
        return res

    def graph_fill(self, player: Player):
        for i in range(M_CELLS):
            self.dfs(self.grid.grid, player, 0, i)

    def change_camera_idx(self, idx):
        self.camera_on_player_idx = idx % len(self.player_list)
        self.camera_obj = Camera(self.player_list[self.camera_on_player_idx])

    def start_game(self):
        is_game_running = True
        self.change_camera_idx(self.camera_on_player_idx)
        self.grid.screen.onkey(lambda: self.change_camera_idx(self.camera_on_player_idx + 1), 'v')
        turtle_camera.TurtleCamera.change_camera(*self.camera_obj.get_neg_cors())
        while is_game_running:
            for player in self.player_list:
                if player.start_moving and player.can_move():
                    # turtle_camera.TurtleCamera.reset()
                    # turtle_camera.TurtleCamera.change_camera(*self.camera_obj.get_neg_cors())
                    player.move()
                    if self.grid.grid[player.x_cell_poss][player.y_cell_poss].cell_full_owner == player:
                        player.fill_cells()
                        self.graph_fill(player)
                    self.grid.grid[player.x_cell_poss][player.y_cell_poss].set_temp_owner(player)

            turtle_camera.TurtleCamera.reset()
            turtle_camera.TurtleCamera.change_camera(*self.camera_obj.get_neg_cors())
            self.grid.screen.update()
            sleep(UPDATE_RATE)
