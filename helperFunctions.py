import ConnectFourBoard


def get_score(player: int, game: ConnectFourBoard) -> int:
    """
    This acts as the main heuristic for the game.
    :param player:  The player who we are counting for
    :param game:    The game board
    :return:        The score we use for the AI
    """
    res = 0
    for i in range(game.HEIGHT):
        for j in range(game.WIDTH - 3):
            res += get_weighting([
                game.board[i][j], game.board[i][j + 1], game.board[i][j + 2], game.board[i][j + 3]
            ], player)

    # Vertical check
    for i in range(game.WIDTH):
        for j in range(game.HEIGHT - 3):
            res += get_weighting([
                game.board[j][i], game.board[j + 1][i], game.board[j + 2][i], game.board[j + 3][i]
            ], player)

    # Ascending Diagonal check
    for i in range(game.HEIGHT - 3):
        for j in range(game.WIDTH - 3):
            res += get_weighting([
                game.board[i][j], game.board[i + 1][j + 1], game.board[i + 2][j + 2], game.board[i + 3][j + 3]
            ], player)

    # Descending Diagonal check
    for i in range(3, game.HEIGHT):
        for j in range(game.WIDTH - 3):
            res += get_weighting([
                game.board[i][j], game.board[i - 1][j + 1], game.board[i - 2][j + 2], game.board[i - 3][j + 3]
            ], player)

    return res


def get_weighting(frame: [int], player: int) -> int:
    """
    Gets the weight for a given frame to be added to the score
    :param frame:   A list of 4 ints
    :param player:  The player we are counting for
    :return:        The weighting for that given combination
    """
    if player == 1:
        other_player = 2
    else:
        other_player = 1
    score = 0
    if frame.count(player) == 4:
        score += 100
    elif frame.count(player) == 3 and frame.count(0) == 1:
        score += 15
    elif frame.count(player) == 2 and frame.count(0) == 2:
        score += 5

    if frame.count(other_player) == 4:
        score -= 100
    elif frame.count(other_player) == 3 and frame.count(0) == 1:
        score -= 10
    elif frame.count(other_player) == 2 and frame.count(0) == 2:
        score -= 4
    return score
