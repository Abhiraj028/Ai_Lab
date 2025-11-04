def is_safe(board, row, col, n):
    # Check if there is any queen in the same row
    for i in range(col):  # Iterate through all columns to the left of current position
        if board[row][i] == 1:  # If a queen (1) is found in the same row
            return False  # Position is not safe, return False
    
    # Check upper diagonal (from current position going up-left)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):  # Simultaneously decrement row and column indices
        if board[i][j] == 1:  # If a queen is found on the upper diagonal
            return False  # Position is not safe, return False
    
    # Check lower diagonal (from current position going down-left)
    for i, j in zip(range(row, n), range(col, -1, -1)):  # Increment row index while decrementing column index
        if board[i][j] == 1:  # If a queen is found on the lower diagonal
            return False  # Position is not safe, return False
    
    # If there is no queen in the same row or in the diagonals, then it is safe to place a queen
    return True  # Position is safe, return True


def solve_n_queens(board, col, n):
    # Base case: If all queens are placed successfully
    if col == n:  # If we've successfully placed queens in all n columns
        print_board(board)  # Print the solution board
        return True  # Indicate successful placement of all queens
    
    for i in range(n):  # Try placing a queen in each row of the current column
        if is_safe(board, i, col, n):  # Check if placing a queen at (i, col) is safe
            board[i][col] = 1  # Place the queen at position (i, col)
            
            # Recursively call solve_n_queens function for the next column
            if solve_n_queens(board, col + 1, n):  # Try to place queens in remaining columns
                return True  # If successful, propagate True up the recursion stack
            
            # If solve_n_queens function does not return True, remove the queen from the current cell
            board[i][col] = 0  # Backtrack: remove the queen (set position back to 0)
    
    # If a queen cannot be placed in any row in the current column, return False
    return False  # No valid placement found in this branch, trigger backtracking


def print_board(board):
    for row in board:  # Iterate through each row in the board
        print(row)  # Print the entire row as a list


# Testing the program for different board sizes
n = 4  # Set board size to 4x4
board = [[0 for _ in range(n)] for _ in range(n)]  # Create a 4x4 board initialized with zeros
solve_n_queens(board, 0, n)  # Start solving from column 0

n = 8  # Set board size to 8x8
board = [[0 for _ in range(n)] for _ in range(n)]  # Create an 8x8 board initialized with zeros
solve_n_queens(board, 0, n)  # Start solving from column 0