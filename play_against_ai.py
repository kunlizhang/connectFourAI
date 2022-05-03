from ConnectFourBoard import ConnectFourBoard
import helperFunctions as fn
from Node import Node
from MiniMax import MiniMax

if __name__ == '__main__':
    gb = ConnectFourBoard()
    mm = MiniMax(gb)
    print(gb)
    while gb.check_for_winner() == 0:
        while True:
            player_move = input("Your move? Between 0-6: ")
            if gb.make_move(int(player_move)):
                break
        print(gb)
        gb.make_move(mm.get_move(gb))
        print(gb)