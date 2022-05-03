from ConnectFourBoard import ConnectFourBoard
import helperFunctions as fn
from Node import Node
import math

class MiniMax:
    def __init__(self, gb: ConnectFourBoard):
        """
        Initialises the MiniMax algorithm
        :param gb: The gameboard (must be an empty gameboard)
        """
        self.root = Node(0, 0, None, gb, [])
        self.gb = gb
        self.DEPTH = 3

    def construct_game_tree(self, curr: Node, depth: int):
        """
        Constructs a game tree of boards
        :param curr:    The current node to construct the game tree
        :param depth:   The current depth of the tree
        :return:        Void
        """
        for i in range(self.root.game_state.WIDTH):
            if not self.gb.make_move(i):
                continue
            p1_score = fn.get_score(1, self.gb)
            p2_score = fn.get_score(2, self.gb)
            node = Node(p1_score, p2_score, i, self.gb.get_state(), [])
            curr.add(node)
            if depth < self.DEPTH and self.gb.check_for_winner() == 0:
                self.construct_game_tree(node, depth + 1)
            self.gb.revert_move(i)

    def get_move(self, gb: ConnectFourBoard) -> int:
        """
        Gets the best move for the current player.
        :param gb:  The current game board.
        :return:    The int of the best column for the move.
        """
        player = gb.currPlayer
        self.root = Node(fn.get_score(1, gb), fn.get_score(2, gb), None, gb, [])
        self.construct_game_tree(self.root, 0)
        best_col, score = self.get_move_recursive_helper(self.root, False, player)
        print("Chosen score: " + str(score))
        # print("Chosen col: " + str(best_col))
        return best_col

    def get_move_recursive_helper(self, curr: Node, minimising: bool, player: int) -> [int, int]:
        """
        Recursive helper function for minimax algorithm.
        :param player:      The player that originally called to get move
        :param curr:        The current node
        :param minimising:  True if we are minimising, false if maximising
        :return:            The column chosen and its score for the player
        """
        if len(curr.children) == 0: # The current move is at the end of the tree
            return curr.col, curr.get_score(player)
        elif minimising:
            lowest_child_score = math.inf
            lowest_child_col = None
            # Gets the minimum maximum child of the current node
            for child in curr.children:
                child_col, child_score = self.get_move_recursive_helper(child, False, player)
                if child_score < lowest_child_score:
                    lowest_child_score = child_score
                    lowest_child_col = child.col
            # print("Lowest:" + str(lowest_child_score))
            return lowest_child_col, lowest_child_score
        else:
            highest_child_score = -math.inf
            highest_child_col = None
            # Gets the maximum minimum child of the current node
            for child in curr.children:
                child_col, child_score = self.get_move_recursive_helper(child, True, player)
                if child_score > highest_child_score:
                    highest_child_score = child_score
                    highest_child_col = child.col
            # print("Highest:" + str(highest_child_score))
            return highest_child_col, highest_child_score


