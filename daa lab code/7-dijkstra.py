#DIJKSTRA ALGO -taking out minimum distance from each vertex with a given source
#TC- O((V+E)logV)
V = int(input("Enter the number of vertices: ")) #input for number of vertices
edges = int(input("Enter the number of edges: ")) #input for number of edges
graph = [[] for _ in range(V)]
#input for edges
for _ in range(edges):
    u, v, wt = map(int, input("Enter edge (u, v, wt): ").split())
    graph[u - 1].append((v - 1, wt))  
#input for source
source = int(input("Enter the source vertex: ")) - 1 

#function for taking out minimum distance from each vertex with a given source
def dijkstra(V, graph, S):
    dist = [float('inf')] * V #declaring all the vertex distance as infinite
    dist[S] = 0 #self loop from source to source as zero
    visited = [False] * V #declare all the vertex as not visited
    for _ in range(V):
        min_dist = float('inf')
        u = -1
        for i in range(V):
            if not visited[i] and dist[i] < min_dist: #compare the distance
                min_dist = dist[i] #change the min dist with the current distance
                u = i #change the value of u
        if u == -1: 
            break
        visited[u] = True #delare the current vertex as visited       
        for v, wt in graph[u]:
            if not visited[v] and dist[u] + wt < dist[v]: #compare the weight of the soruce edge till the another vertex and replace it with minimum distance
                dist[v] = dist[u] + wt #add in the total distance
    return dist #display the distance array containing minimum distance from source vertex

dist = dijkstra(V, graph, source) #gives distances
print("Shortest distances from source vertex:", dist) #print 