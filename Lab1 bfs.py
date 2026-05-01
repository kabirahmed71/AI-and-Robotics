# Lab-1 : Breadth First Search (BFS)

# BFS Function
def bfs(start, visited, G, n):
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        i = queue.popleft()
        print(i, end=" ")

        for j in range(n):
            if not visited[j] and G[i][j] == 1:
                visited[j] = True
                queue.append(j)


# Main Program
n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
G = []

for i in range(n):
    row = list(map(int, input().split()))
    G.append(row)

visited = [False] * n

start = int(input("Enter starting vertex (0 to n-1): "))

print("BFS Traversal:")
bfs(start, visited, G, n)