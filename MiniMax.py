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
        :param root:    The current node to construct the game tree
        :param depth:   The current depth of the tree
        :return:        Void
        """
        for i in range(self.root.game_state.WIDTH):
            if not self.gb.make_move(i):
                continue
            winner = self.gb.check_for_winner()
            if winner == 1:
                p1_score = 100000000
                p2_score = -100000000
            elif winner == 2:
                p2_score = 100000000
                p1_score = -100000000
            else:
                p1_score = fn.countPossibleFours(1, self.gb)
                p2_score = fn.countPossibleFours(2, self.gb)
            node = Node(p1_score, p2_score, i, self.gb.get_state(), [])
            self.root.add(node)
            if depth < self.DEPTH:
                self.construct_game_tree(node, depth + 1)
            self.gb.revert_move(i)

    def get_move(self, gb: ConnectFourBoard) -> int:
        """
        Gets the best move for the current player.
        :param gb:  The current game board.
        :return:    The int of the best column for the move.
        """
        player = gb.currPlayer
        self.root = Node(fn.countPossibleFours(1, gb), fn.countPossibleFours(2, gb), None, gb, [])
        self.construct_game_tree(self.root, 0)
        best_node = self.get_move_recursive_helper(self.root, True, player)
        return best_node.col

    def get_move_recursive_helper(self, curr: Node, min: bool, player: int) -> Node:
        """
        Recursive helper function for minimax algorithm.
        :param player:  The player that originally called to get move
        :param curr:    The current node
        :param min:     True if we are minimising, false if maximising
        :return:        The minimum/maximum node
        """
        if len(curr.children) == 0:
            return curr
        elif min:
            lowest_score_node = None
            # Gets the minimum maximum child of the current node
            for node in curr.children:
                curr_max_child = self.get_move_recursive_helper(node, False, player)
                if lowest_score_node is None or curr_max_child.get_score(player) < lowest_score_node.get_score(player):
                    lowest_score_node = curr_max_child
            return lowest_score_node
        else:
            highest_score_node = None
            # Gets the maximum child of the current node
            for node in curr.children:
                curr_min_child = self.get_move_recursive_helper(node, True, player)
                if highest_score_node is None or curr_min_child.get_score(player) > highest_score_node.get_score(player):
                    highest_score_node = curr_min_child
            return highest_score_node


    def get_max(self, nodes: [Node], player: int) -> Node:
        res = nodes[0]
        for child in nodes:
            if child.get_score(player) >= res:
                res = child
        return res

    def get_min(self, nodes: [Node], player: int) -> Node:
        res = nodes[0]
        for child in nodes:
            if child.get_score(player) <= res:
                res = child
        return res


