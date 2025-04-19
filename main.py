from time import sleep
from turtle import Screen, Turtle
from cell import Cell
from grid import Grid
from CONSTANTS import *
from player import Player
from game_manger import Game_Manger
from threading import Thread


def main():
    game = Game_Manger()
    game.add_player('green', 0, 1)
    game.add_player('blue', 3, 0)
    game.start_game()


if __name__ == '__main__':
    main()