def is_safe(board, row, col, n):
    # Check if there is any queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # If there is no queen in the same row or in the diagonals, then it is safe to place a queen
    return True


def solve_n_queens(board, col, n):
    # Base case: If all queens are placed successfully
    if col == n:
        print_board(board)
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            # Recursively call solve_n_queens function for the next column
            if solve_n_queens(board, col + 1, n):
                return True
            # If solve_n_queens function does not return True, remove the queen from the current cell
            board[i][col] = 0
    # If a queen cannot be placed in any row in the current column, return False
    return False


def print_board(board):
    for row in board:
        print(row)


# Testing the program for different board sizes
n = 4
board = [[0 for _ in range(n)] for _ in range(n)]
solve_n_queens(board, 0, n)

n = 8
board = [[0 for _ in range(n)] for _ in range(n)]
solve_n_queens(board, 0, n)