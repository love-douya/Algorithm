from collections import defaultdict

class Graph:
    def ___init___(self, vertices):
        self.V = vertices 
        #dictionary containing adjacency lsit
        self.graph = defaultdict(list)

    #function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    #A recursive function used by shortestPath
    def topologicalSortUtil(self, v, visited, stack):
        #Mark the current node as visited.list
        visited[v] = True
        
        if v in self.graph.keys():
            for node, weight in self.graph[v]:
                if visited[node] == False:
                    self.topologicalSortUtil(node, visited, stack)
        
        #Push current vertex to stack which stores topological
        stack.append(v)

    def shortestPath(self, s):
        #Mark all the vertices as not visited 
        visited = [False] * self.V
        stack = []

        #Call the recursion helper function to store Topological
        #Sort starting from source vertice
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(s, visited, stack)

        #Initialize distances to all vertices as infinite
        #distance to source as 0
        dist = [float("Inf")] * (self.V)
        dist[s] = 0

        #Process vertices in topological order
        while stack:
            #Get the next vertex from topological order
            i = stack.pop()

            #Update distances of all adjacent vertices
            for node, weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight

        #Print the calculated shortest distance
        for i in range(self.V):
            print("%d" %dist[i]) 

g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)

# source = 1
s = 1

print("Following are shortest distances from source %d" %s)
g.shortestPath(s)




                
        