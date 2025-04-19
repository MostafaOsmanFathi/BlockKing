from time import sleep
from turtle import Screen, Turtle
from cell import Cell
from grid import Grid
from CONSTANTS import *
from player import Player
from game_manger import Game_Manger

def main():
    game = Game_Manger()
    game.add_player('green',0)
    game.start_game()


if __name__ == '__main__':
    main()
