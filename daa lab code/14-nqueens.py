#TC-O(N!) (number of recursive calls made)
#backtracking approach

# Initialize the problem size (n x n board)
n = int(input("enter n*n chess board value of n:"))
# Sets to track columns and diagonals under attack
col = set()
negDiag = set()  # Tracks (r - c) for negative diagonals
posDiag = set()  # Tracks (r + c) for positive diagonals
# List to store all valid board configurations
res = []
# Initialize the board with '_' indicating empty spaces
board = [['_'] * n for i in range(n)]

#backtracking func
def backtrack(r, n):
    # If we've placed queens in all rows
    if r == n:
        # Append the current board configuration to the results
        res.append([" ".join(row) for row in board])
        return
    
    # Try placing a queen in each column of the current row
    for c in range(n):
        # Check if the column, positive diagonal, or negative diagonal is under attack
        if c in col or (r + c) in posDiag or (r - c) in negDiag:
            continue
        
        # Place the queen and mark the column and diagonals as under attack
        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)
        board[r][c] = 'Q'

        # Move to the next row and continue the search
        backtrack(r + 1, n)

        # Remove the queen and unmark the column and diagonals (backtrack)
        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)
        board[r][c] = '_'

# Start the backtracking process from the first row
backtrack(0, n)

# Print the number of solutions found
print("Number of ways:", len(res))

# Print all possible board configurations
print("\nPossible arrangements:")
for r in res:
    print(r)
