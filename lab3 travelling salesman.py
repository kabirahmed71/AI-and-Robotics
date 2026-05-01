# Lab-3 : Travelling Salesman Problem (TSP)
# Nearest Neighbor Method

# Input Number of Nodes
n = int(input("Enter number of nodes: "))

print("Enter cost matrix:")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

visited = [False] * n
cost = 0


# Find Next Minimum Cost City
def find_next(city):
    global cost
    min_cost = float('inf')
    next_city = -1

    for i in range(n):
        if not visited[i] and graph[city][i] != 0:
            if graph[city][i] < min_cost:
                min_cost = graph[city][i]
                next_city = i

    if next_city != -1:
        cost += min_cost

    return next_city


# TSP Function
def tsp(city):
    visited[city] = True
    print(city + 1, end=" -> ")

    next_city = find_next(city)

    if next_city == -1:
        print(1)
        cost_final = cost + graph[city][0]
        print("\nMinimum cost:", cost_final)
        return

    tsp(next_city)


# Main Program
print("\nThe Path is:")
tsp(0)