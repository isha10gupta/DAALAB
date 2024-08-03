#BFS- Breadth first search (first the soruce node visited then the neighboring node visited)

# Take the number of vertices as input
n = int(input("Enter number of vertices: "))
# Take the number of edges as input
e = int(input("Enter number of edges: "))
# Initialize the adjacency matrix for the graph
G = [[0 for i in range(n)] for j in range(n)]
# Take the edges as input and update the adjacency matrix
for i in range(e):
    print("Enter vertices (u, v):")
    a = int(input())  # First vertex of the edge(start naming from 0)
    b = int(input())  # Second vertex of the edge
    G[a][b] = 1  # Mark the edge from a to b
    G[b][a] = 1  # Mark the edge from b to a (since the graph is undirected)
# Take the starting vertex for BFS as input
s = int(input("Enter root: "))
# Initialize the visited list to keep track of visited vertices
visited = [0 for i in range(n)]

# Define the BFS function
def BFS(G, visited, s, n):
    queue = []  # Initialize the queue for BFS
    visited[s] = 1  # Mark the starting vertex as visited
    print(s)  # Print the starting vertex
    queue.append(s)  # Enqueue the starting vertex

    while len(queue) != 0:  # Continue until the queue is empty
        v = queue.pop(0)  # Dequeue a vertex from the queue

        for j in range(n):  # Iterate over all vertices
            if G[v][j] and visited[j] == 0:  # If there is an edge and the vertex is not visited
                visited[j] = 1  # Mark the vertex as visited
                print(j)  # Print the vertex
                queue.append(j)  # Enqueue the vertex

# Print the adjacency matrix
print("Adjacency Matrix:")
for row in G:
    print(row)

# Perform BFS starting from the root vertex
print("BFS Traversal:")
BFS(G, visited, s, n)
