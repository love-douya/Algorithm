import pylint, sys, os

def init_single_source(s):
    for i in range(v):
        dist[i] = None
        pred[i] = -1
    dist[s] = 0

def relax(u, v, w):
    if dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        pred[v] = u

def bellman(s):
    init_single_source(s)
    for k in range(v - 1):
        for i in range(v):
            for j in range(v):
                if g[i][j] != 0:
                    relax(i, j, g[i][j])

def path_trace(d, s):
    if d == s:
        print (str(s + 1))
    else:
        path_trace(s, pred[d])
        print (str(d + 1))

v = int(input("Enter Number of vertices:"))
e = int(input("Enter Number of edges:"))
g = []
pred = []
dist = []

for i in range(v):
    ta = []
    pred.append(0)
    dist.append(0)
    for j in range (v):
        ta.append(0)
    g.append(ta)

for i in range(e - 1):
    print ("Edge " + str(i + 1))
    start = int(input("Start Vertex: "))
    end = int(input("End Vertex: "))
    weight = int(input("Weight: "))
    g[start - 1][end - 1] = weight

s = int(input("Source Vertex: ")) - 1
d = int(input("Destination Vertex: ")) - 1

bellman(s)
print("Shortest path from source " + str(s) + "is .. ")
path_trace(s, d)
print("Weight: " + str(dist[d]))