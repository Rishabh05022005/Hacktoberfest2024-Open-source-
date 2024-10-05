# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

# Function to check if it's safe to place a number in a specific cell
def is_safe(grid, row, col, num):
    # Check if the number is already in the row
    if num in grid[row]:
        return False
    
    # Check if the number is already in the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check if the number is in the 3x3 subgrid
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

# Backtracking function to solve the Sudoku
def solve_sudoku(grid):
    empty_spot = False
    row = col = 0

    # Find an empty cell in the grid (denoted by 0)
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                row, col = i, j
                empty_spot = True
                break
        if empty_spot:
            break

    # If no empty spot is found, the Sudoku is solved
    if not empty_spot:
        return True

    # Try placing digits from 1 to 9 in the empty spot
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            # Recursively try to solve the rest of the grid
            if solve_sudoku(grid):
                return True

            # If placing num didn't lead to a solution, backtrack
            grid[row][col] = 0

    return False

# Example Sudoku grid (0 represents empty cells)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku and print the result
if solve_sudoku(grid):
    print("Solved Sudoku:")
    print_grid(grid)
else:
    print("No solution exists")
