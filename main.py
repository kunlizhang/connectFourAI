from ConnectFourBoard import ConnectFourBoard
import helperFunctions as fn
from Node import Node
from MiniMax import MiniMax

if __name__ == '__main__':
    gb = ConnectFourBoard()
    mm = MiniMax(gb)
    gb.make_move(3)
    gb.make_move(2)
    print(gb)
    print(mm.get_move(gb))
