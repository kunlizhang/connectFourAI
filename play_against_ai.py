from ConnectFourBoard import ConnectFourBoard
import helperFunctions as fn
from Node import Node
from MiniMax import MiniMax

if __name__ == '__main__':
    print("hi")
    gb = ConnectFourBoard()
    mm = MiniMax(gb)
    while gb.check_for_winner() == 0:
        print(gb)
        player_move = input("Your move? Between 0-6")
        gb.make_move(int(player_move))
        print(gb)
        gb.make_move(mm.get_move(gb))