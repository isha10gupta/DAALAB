#DFS- first the source node visited then next node then its next node and so on...
#TC- O(V^2) for adjancy matrix
# Take the number of vertices as input
n = int(input("Enter number of vertices: "))
# Take the number of edges as input
e = int(input("Enter number of edges: "))
# Initialize the adjacency matrix for the graph
G = [[0 for i in range(n)] for j in range(n)]
# Take the edges as input and update the adjacency matrix
for i in range(e):
    print("Enter vertices (u, v):")
    a = int(input())  # First vertex of the edge (start taking input of vertices from zero)
    b = int(input())  # Second vertex of the edge
    G[a][b] = 1  # Mark the edge from a to b
    G[b][a] = 1  # Mark the edge from b to a (since the graph is undirected)
# Take the starting vertex for DFS as input
s = int(input("Enter root: "))
# Initialize the visited list to keep track of visited vertices
visited = [0 for i in range(n)]

# Define the DFS function
def DFS(G, visited, s, n):
    visited[s] = 1  # Mark the current vertex as visited
    print(s)  # Print the current vertex
    for j in range(n):  # Iterate over all vertices
        if G[s][j] and visited[j] == 0:  # If there is an edge and the vertex is not visited
            DFS(G, visited, j, n)  # Recur for the connected vertex

# Print the adjacency matrix
print("Adjacency Matrix:")
for row in G:
    print(row)

# Perform DFS starting from the root vertex
print("DFS Traversal:")
DFS(G, visited, s, n)
