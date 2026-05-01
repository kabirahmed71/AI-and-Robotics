# Lab-2 : Depth First Search (DFS)

# DFS Function
def dfs(i, visited, G, n):
    print(i, end=" ")
    visited[i] = True

    for j in range(n):
        if not visited[j] and G[i][j] == 1:
            dfs(j, visited, G, n)


# Main Program
n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
G = []

for i in range(n):
    row = list(map(int, input().split()))
    G.append(row)

visited = [False] * n

start = int(input("Enter starting vertex: "))

print("DFS Traversal:")
dfs(start, visited, G, n)