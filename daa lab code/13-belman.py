# Bellman-Ford algorithm to detect negative weight cycles and find shortest paths
# A large number representing infinity
inf = 999999
# Taking input from the user
# Number of edges in the graph
edges = int(input("Enter the number of edges: "))
G = []
# Input for each edge
for i in range(edges):
    # Source vertex of the edge
    u = int(input(f"Enter the source vertex of edge {i+1}: "))
    # Destination vertex of the edge
    v = int(input(f"Enter the destination vertex of edge {i+1}: "))
    # Weight of the edge
    weight = int(input(f"Enter the weight of edge {i+1}: "))
    # Append the edge (u, v, weight) to the graph
    G.append((u, v, weight))
# Number of vertices in the graph
vertices = int(input("Enter the number of vertices: "))
# Source vertex from which to calculate shortest paths
root = int(input("Enter the source vertex: "))
# Initialize distances from the source vertex to all other vertices as infinity
dist = [inf] * vertices
# Distance to the source vertex itself is 0
dist[root] = 0

#function
def bellman(G, dist, n):
    # Relax all edges n-1 times
    for _ in range(n - 1):
        for u, v, weight in G:
            # If the distance to the destination can be shortened by taking the edge u->v
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Check for negative weight cycles
    for u, v, weight in G:
        # If we can still relax an edge, then there is a negative weight cycle
        if dist[u] + weight < dist[v]:
            print("-ve cycle detected!!")
            return

    # Print the shortest distances from the source vertex
    print("Shortest distances from source:", dist)

# Run Bellman-Ford algorithm
bellman(G, dist, vertices)
