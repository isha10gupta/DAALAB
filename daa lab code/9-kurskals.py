#E(log(V))
# Main function to take user input and execute the algorithm
V = int(input("Enter the number of vertices: "))  # Number of vertices
E = int(input("Enter the number of edges: "))  # Number of edges
edges = []
# Take edge input from the user
print("Enter each edge in the format: u v weight")
for _ in range(E):
    u, v, wt = map(int, input().split())
    edges.append([u, v, wt])

# Function to find the root of the set in which element i belongs
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# Function to perform union of two sets of x and y based on rank
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of high rank tree
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        # If ranks are same, make one as root and increment its rank by one
        parent[yroot] = xroot
        rank[xroot] += 1

# Function to implement Kruskal's algorithm
def kruskal(V, edges):
    # Initialize parent and rank arrays
    parent = []
    rank = []

    # Sort all the edges in non-decreasing order of their weight
    edges.sort(key=lambda x: x[2])

    # Create V subsets with single elements
    for node in range(V):
        parent.append(node)
        rank.append(0)

    mst_cost = 0  # Initialize result for minimum spanning tree cost
    mst_edges = []  # To store the edges in the minimum spanning tree

    # Iterate through all sorted edges
    for u, v, wt in edges:
        x = find(parent, u)
        y = find(parent, v)

        # If including this edge does not cause a cycle
        if x != y:
            mst_cost += wt  # Add weight of the edge to the result
            mst_edges.append([u, v, wt])  # Include this edge in the result
            union(parent, rank, x, y)  # Union of two sets

    return mst_cost, mst_edges

    # Call Kruskal's algorithm and get the result
mst_cost, mst_edges = kruskal(V, edges)
    
    # Print the minimum cost of the spanning tree
print("Minimum Cost of Spanning Tree:", mst_cost)
    
    # Print the edges in the minimum spanning tree
print("Edges in Minimum Spanning Tree:")
for edge in mst_edges:
    print(edge)


