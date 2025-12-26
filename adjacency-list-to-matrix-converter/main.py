# Build an Adjacency List to Matrix Converter

adj_list = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}

def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for node, adj_nodes in adj_list.items():
        for adj_node in adj_nodes:
            adj_matrix[node][adj_node] = 1

    for row in adj_matrix:
        print(row)

    return adj_matrix

adjacency_list_to_matrix(adj_list)
