from ConnectFourBoard import ConnectFourBoard
class Node:
    def __init__(self, player1: int, player2: int, col: int, game_state: ConnectFourBoard, children: ['Node']):
        """
        A node for the MiniMax tree.
        :param player1:     Player 1's score
        :param player2:     Player 2's score
        :param col:         The column of the last move
        :param game_state:  The game board state
        :param children:    The children of this game state.
        """
        self.player1 = player1
        self.player2 = player2
        self.col = col
        self.game_state = game_state
        self.children = children

    def add(self, node: 'Node'):
        self.children.append(node)

    def get_score(self, player: int) -> int:
        if player == 1:
            return self.player1
        elif player == 2:
            return self.player2
        else:
            return None

    def __str__(self):
        return str(self.player1) + " " + str(self.player2) + " " + str(self.col)