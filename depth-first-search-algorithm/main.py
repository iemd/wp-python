# Implement the Depth First Search Algorithm

adj_matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]
def dfs(matrix, start_node):
    n = len(matrix)
    visited = [False] * n

    stack = [start_node]
    result = []

    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            result.append(u)
        
        for v in range(n):
            if matrix[u][v] == 1 and not visited[v]:
                stack.append(v)

    return result

print(dfs(adj_matrix, 1))
