
# Floyd-Warshall Algorithm

INF = float('inf')

# Graph represented as an adjacency matrix
graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

n = len(graph)

# Floyd-Warshall Algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(
                graph[i][j],
                graph[i][k] + graph[k][j]
            )

# Display shortest distance matrix
print("Shortest Distance Matrix:")

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print("INF", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
