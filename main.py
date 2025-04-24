from game_manger import Game_Manger


def main():
    game = Game_Manger()
    game.add_player('red', 0, 1)
    game.add_player('green', 3, 0)
    game.start_game()


if __name__ == '__main__':
    main()
