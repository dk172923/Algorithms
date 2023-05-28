def is_safe(board, row, col, n):
    # Check if a queen can be placed at board[row][col]
  
    # Check the left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False
  
    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
  
    # Check the lower diagonal on the left side
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
  
    return True
  
  
def solve_n_queens_util(board, col, n, solutions):
    # Base case: If all queens are placed, add the solution to the list
    if col == n:
        solution = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(board[i][j])
            solution.append(row)
        solutions.append(solution)
        return True
  
    # Recursive case: Try placing the queen in each row of the current column
    for row in range(n):
        if is_safe(board, row, col, n):
            # Place the queen at board[row][col]
            board[row][col] = 1
  
            # Recur for the next column
            solve_n_queens_util(board, col + 1, n, solutions)
  
            # Backtrack: Remove the queen from board[row][col]
            board[row][col] = 0
  
    return False
  
  
def solve_n_queens(n):
    # Create an empty chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]
  
    solutions = []
  
    # Solve the N-Queens problem
    solve_n_queens_util(board, 0, n, solutions)
  
    return solutions


# Test the program
n = 4
solutions = solve_n_queens(n)
  
print(f"Number of solutions for {n}-Queens: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"\nSolution {i + 1}:")
    for row in solution:
        print(" ".join(map(str, row)))
