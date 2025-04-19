from time import sleep
from turtle import Turtle

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
        # Add score display turtle
        self.score_display = Turtle()
        self.score_display.hideturtle()
        self.score_display.penup()
        self.score_display.color('white')
        self.score_display.goto(0, SCREEN_HEIGHT/2 - 50)
        self.update_score_display()

    def update_score_display(self):
        self.score_display.clear()
        score_text = " | ".join(
            f"{player.player_color}: Kills {player.kills} Deaths {player.deaths}"
            for player in self.player_list
        )
        self.score_display.write(score_text, align="center", font=("Arial", 16, "normal"))

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

    def start_game(self):
        is_game_running = True
        while is_game_running:
            for player in list(self.player_list):
                if player.start_moving and player.can_move():
                    player.move()

                    cell = self.grid.grid[player.x_cell_poss][player.y_cell_poss]

                    # Check if player collides with another player's trail
                    if cell.cell_temp_owner is not None and cell.cell_temp_owner != player:
                        # Find the owner of the trail
                        trail_owner = cell.cell_temp_owner
                        self.kill_player(player)
                        trail_owner.kills += 1  # Increment kill counter
                        self.update_score_display()
                        continue

                    # Check if player collides with another player's territory
                    if cell.cell_full_owner is not None and cell.cell_full_owner != player:
                        territory_owner = cell.cell_full_owner
                        self.kill_player(player)
                        territory_owner.kills += 1  # Increment kill counter
                        self.update_score_display()
                        continue

                    if cell.cell_full_owner == player:
                        player.fill_cells()
                        self.graph_fill(player)

                    cell.set_temp_owner(player)

            self.grid.screen.update()
            sleep(UPDATE_RATE)

    def kill_player(self, player):
        print(f"{player.player_color} died!")
        player.reset_position()
        self.update_score_display()