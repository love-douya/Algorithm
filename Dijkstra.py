'''
Dijkstra algorithm
graphdict  = {"A":[("B", 6),("C", 3)], "B":[("C", 2),("D", 5)], "C":[("B", 2),("D", 3),("E", 4)],
"D":[("B", 5),("C", 3),("E", 2),("F", 3)], "E":[("C", 4),("D", 2),("F", 5)], "F":[("D", 3),("E", 5)]}
'''

def Dijkstra(startnode, endnode, graphdict = None):
    s = [startnode]
    v = []
    for node in graphdict.keys():
        if node != startnode:
            v.append(node)
        #distance dict from startnode
        dist = {}
    for node in v:
        dist[node] = float('Inf')

    while len(v) > 0:
        center = s[-1]#get the final node as the new center node
        minval = ("None", float("Inf"))
        for node, d in graphdict[center]:
            if node not in v:
                continue
            if len(s) == 1:
                dist[node] = d
            else:
                start2centerdist = dist[center]
                if start2centerdist + d < dist[node]:
                    dist[node] = start2centerdist + d            
            if d < minval[1]:
                minval = (node, d)

        v.remove(minval[0])
        s.append(minval[0])

    return dist

shortest_road = Dijkstra("A", "F", graphdict  = {"A":[("B", 6),("C", 3)], "B":[("C", 2),("D", 5)], "C":[("B", 2),("D", 3),("E", 4)],
"D":[("B", 5),("C", 3),("E", 2),("F", 3)], "E":[("C", 4),("D", 2),("F", 5)], "F":[("D", 3),("E", 5)]})

Guide = "Shortest distance from A to "

for key, shortest in shortest_road.items():
    print(Guide + str(key) + " is: " + str(shortest))

