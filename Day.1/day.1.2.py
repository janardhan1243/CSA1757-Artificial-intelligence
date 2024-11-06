def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i] == j:
            return False

    return True

def solve_n_queens(board, row):
    n = len(board)
    if row == n:
        return [board[:]]
    solutions = []
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solutions += solve_n_queens(board, row + 1)
            board[row] = -1
    return solutions
def print_solution(board):
    n = len(board)
    for row in board:
        print(" ".join("Q" if col == row else "." for col in range(n)))
    print("\n")
n = 8
board = [-1] * n  
solutions = solve_n_queens(board, 0)
print(f"Total solutions: {len(solutions)}\n")
for solution in solutions:
    print_solution(solution)
