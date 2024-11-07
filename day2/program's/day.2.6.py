import math

PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_game_over(board):
    if check_win(board, PLAYER_X) or check_win(board, PLAYER_O):
        return True
    return all([cell != EMPTY for row in board for cell in row])

def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves

def alpha_beta(board, depth, alpha, beta, is_maximizing):
    if check_win(board, PLAYER_X):
        return 10 - depth
    if check_win(board, PLAYER_O):
        return depth - 10
    if is_game_over(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = PLAYER_X
            score = alpha_beta(board, depth + 1, alpha, beta, False)
            board[i][j] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = PLAYER_O
            score = alpha_beta(board, depth + 1, alpha, beta, True)
            board[i][j] = EMPTY
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        i, j = move
        board[i][j] = PLAYER_X
        score = alpha_beta(board, 0, -math.inf, math.inf, False)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def tic_tac_toe():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    current_player = PLAYER_X

    while True:
        print_board(board)
        if current_player == PLAYER_X:
            print("AI's (X) turn:")
            i, j = find_best_move(board)
        else:
            print("Player O's turn:")
            try:
                i, j = map(int, input("Enter row and column (0, 1, 2) separated by space: ").split())
            except ValueError:
                print("Invalid input. Please enter two numbers separated by space.")
                continue
            if board[i][j] != EMPTY:
                print("Invalid move. Try again.")
                continue

        board[i][j] = current_player

        if check_win(board, PLAYER_X):
            print_board(board)
            print("Player X wins!")
            break
        if check_win(board, PLAYER_O):
            print_board(board)
            print("Player O wins!")
            break
        if is_game_over(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

if __name__ == "__main__":
    tic_tac_toe()