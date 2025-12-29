# Implement the N-Queens Problem

def is_valid(board, row, col):
    for r, c in enumerate(board):
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True

def dfs_n_queens(n):
    if n < 1:
        return []

    result = []
    stack = [[]]

    while stack:
        board = stack.pop()
        row = len(board)

        if row == n:
            result.append(board)
            continue
        
        for col in range(n - 1, -1, -1):
            if is_valid(board, row, col):
                stack.append(board + [col])

    return result
    
print(dfs_n_queens(4))
