import copy


class ConnectFourBoard:
    """
    This class handles the game being played
    """
    def __init__(self):
        self.HEIGHT = 6
        self.WIDTH = 7
        self.board = [[0] * self.WIDTH for _ in range(self.HEIGHT) ]
        self.currPlayer = 1

    def make_move(self, col: int) -> bool:
        """
        Makes a move on the board.
        :param col:     The column of the move
        :return:        True if a valid move was made
        """
        for i in range(self.HEIGHT):
            if self.board[i][col] == 0:
                if self.currPlayer == 1:
                    self.board[i][col] = 1
                else:
                    self.board[i][col] = 2
                self.toggle_curr_player()
                return True
        return False

    def revert_move(self, col: int):
        """
        Removes the most recent move on the board and toggles
        the player again
        :param col:     The column of the revert
        :return:        Void
        """
        for i in reversed(range(self.HEIGHT)):
            if self.board[i][col] != 0:
                self.board[i][col] = 0
                self.toggle_curr_player()
                return

    def toggle_curr_player(self):
        """Toggles the current player of the game."""
        if self.currPlayer == 1:
            self.currPlayer = 2
        else:
            self.currPlayer = 1

    def check_for_winner(self) -> int:
        """
        Checks if there is a winner in the current board
        :return: 0 if there is no winner, 1 for player 1 and 2 for player 2.
        """
        # Horizontal check
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH-3):
                if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] != 0:
                    return self.board[i][j]

        # Vertical check
        for i in range(self.WIDTH):
            for j in range(self.HEIGHT-3):
                if self.board[j][i] == self.board[j+1][i] == self.board[j+2][i] == self.board[j+3][i] != 0:
                    return self.board[j][i]

        # Ascending Diagonal check
        for i in range(self.HEIGHT-3):
            for j in range(self.WIDTH-3):
                if self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3] != 0:
                    return self.board[i][j]

        # Descending Diagonal check
        for i in range(3, self.HEIGHT):
            for j in range(self.WIDTH - 3):
                if self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] == self.board[i-3][j+3] != 0:
                    return self.board[i][j]

        return 0

    def __str__(self):
        res = ""
        for i in reversed(range(self.HEIGHT)):
            res += "| "
            for j in range(self.WIDTH):
                if self.board[i][j] == 0:
                    res += " "
                elif self.board[i][j] == 1:
                    res += "X"
                else:
                    res += "O"
                res += " | "
            res += "\n"
        res += "  0   1   2   3   4   5   6  "
        return res

    def get_state(self):
        """
        Gets a copy of the current game state
        :return: A copy of this object.
        """
        return copy.deepcopy(self)
