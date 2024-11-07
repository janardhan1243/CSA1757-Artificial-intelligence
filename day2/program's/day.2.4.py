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

def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])

def valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn:")
        
        try:
            row, col = map(int, input("Enter row and column (0, 1, 2) separated by space: ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue

        if valid_move(board, row, col):
            board[row][col] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
