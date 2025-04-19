from time import sleep

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

    def add_player(self, color, position):
        if position >= 0 and position < 4:
            self.player_list.append(Player(color, self.grid, *Game_Manger.player_respawn_positions[position]))

    def start_game(self):
        is_game_running = True
        while is_game_running:
            for player in self.player_list:
                if player.start_moving:
                    player.move()
            self.grid.screen.update()
            sleep(UPDATE_RATE)
