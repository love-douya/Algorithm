#Strongly connected componets using tarjan
from collections import defaultdict

#using adjancency list representation
class Graph:
    def __init__(self, vertices):
        #No.of vertices
        self.V = vertices
        #default dictionary to store graph
        self.graph = defaultdict(list)

    #function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursion function that find finds and prints strongly connected
    components using DFS traversal
    u --> The vertex to be visited next
    disc[] --> Stores discovery times of visited vertices
    low[] -->> earliest visited vertex (the vertex with minimum discovery time)
                that can be reached from subtree rooted with current vertex
    '''
    def DFSUtil(self, v, visited):
        #Mark the current node as visited and print it
        visited[v] = True
        print(v)
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        #Mark the current node as Visited
        visited[v] = True
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    #Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)

        #Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            g = Graph(self.V)

            #Recuir for all the vertices adjacent to this vertex
            for i in self.graph:
                for j in self.graph[i]:
                    g.addEdge(j, i)
            return g

    #The main function that finds and prints all strongly
    #connected components
    def printSCCs(self):
        stack = []
        #Mark all the vertices as not visited (For first DFS)
        visited = [False] * (self.V)
        #Fill vertices in stack according to their finishing
        #times
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

        #Create a reversed graph
        gr = self.getTranspose()

        #Mark all the vertices as not visited (For second DFS)
        visited = [False] * (self.V)

        #Now process all vertices in order defined by stack
        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited)
                print(" ")

#Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

print("Following are strongly connected components " + "in given graph")
g.printSCCs()

