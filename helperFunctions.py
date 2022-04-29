import ConnectFourBoard

def countPossibleFours(player: int, game: ConnectFourBoard) -> int:
    """
    Counts the number of possible connect 4 positions.
    This acts as the main heuristic for the game.
    :param player:  The player who we are counting for
    :param game:    The game board
    :return:        The number of possible connect 4s
    """
    if player == 1:
        otherPlayer = 2
    else:
        otherPlayer = 1

    res = 0
    for i in range(game.HEIGHT):
        for j in range(game.WIDTH - 3):
            if otherPlayer not in [
                game.board[i][j], game.board[i][j + 1], game.board[i][j + 2], game.board[i][j + 3]
            ]:
                res += 1

    # Vertical check
    for i in range(game.WIDTH):
        for j in range(game.HEIGHT - 3):
            if otherPlayer not in [
                game.board[j][i], game.board[j + 1][i], game.board[j + 2][i], game.board[j + 3][i]
            ]:
                res += 1

    # Ascending Diagonal check
    for i in range(game.HEIGHT - 3):
        for j in range(game.WIDTH - 3):
            if otherPlayer not in [
                game.board[i][j], game.board[i + 1][j + 1], game.board[i + 2][j + 2], game.board[i + 3][j + 3]
            ]:
                res += 1

    # Descending Diagonal check
    for i in range(3, game.HEIGHT):
        for j in range(game.WIDTH - 3):
            if otherPlayer not in [
                    game.board[i][j], game.board[i - 1][j + 1], game.board[i - 2][j + 2], game.board[i - 3][j + 3]
            ]:
                res += 1

    return res
