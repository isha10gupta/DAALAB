#TC- O(N!⋅N)
#BACKTRACKING APPRIACH

# Taking input from the user
n = int(input("Enter the number of vertices: "))
graph = []
# Input adjacency matrix
print("Enter the adjacency matrix row by row:")
for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    graph.append(row)
# Boolean array to check if a node has been visited or not
v = [False for i in range(n)]
# Mark the 0th node as visited (starting point)
v[0] = True
# List to store the minimum weight Hamiltonian Cycle
answer = []

# Function to find the minimum weight Hamiltonian Cycle
def tsp(graph, v, currPos, n, count, cost):
    # If last node is reached and it has a link to the starting node
    # i.e., the source, then add the total cost of traversal to the answer list
    if count == n and graph[currPos][0]:
        answer.append(cost + graph[currPos][0])
        return
    # BACKTRACKING STEP
    # Loop to traverse the adjacency list of currPos node
    # and increase the count by 1 and cost by graph[currPos][i] value
    for i in range(n):
        if not v[i] and graph[currPos][i]:
            # Mark as visited
            v[i] = True
            tsp(graph, v, i, n, count + 1, cost + graph[currPos][i])
            # Mark ith node as unvisited
            v[i] = False

# Find the minimum weight Hamiltonian Cycle
tsp(graph, v, 0, n, 1, 0)

# ans is the minimum weight Hamiltonian Cycle
print("The minimum cost of the Hamiltonian Cycle is:", min(answer))
