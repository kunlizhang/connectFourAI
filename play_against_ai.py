from ConnectFourBoard import ConnectFourBoard
import helper_functions as fn
from Node import Node
from MiniMax import MiniMax

if __name__ == '__main__':
    gb = ConnectFourBoard()
    mm = MiniMax(gb)
    position = input("Would you like play first (1) or second (2)? ")
    print(gb)
    if position == "2":
        gb.make_move(mm.get_move())
        print(gb)
    while gb.check_for_winner() == 0:
        while True:
            player_move = input("Your move? ")
            if gb.make_move(int(player_move)):
                break
        print(gb)
        gb.make_move(mm.get_move())
        print(gb)