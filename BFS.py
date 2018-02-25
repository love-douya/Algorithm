# from pythonds.graphs import Graph, Vertex
# from pythonds.basic import Queue

# def bfs(g, start):
#     start.setDistance(0)
#     start.setPred(None)
#     vertQueue = Queue()
#     vertQueue.enqueue(start)
#     while (vertQueue.size() > 0):
#         currentVert = vertQueue.dequeue()
#         for nbr in currentVert.getConnections():
#             if (nbr.getColor() == 'white'):
#                 nbr.setColor('gray')
#                 nbr.setDistance(currentVert.getDistance() + 1)
#                 nbr.setPred(currentVert)
#                 vertQueue.enqueue(nbr)
#             currentVert.setColor('black')
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

print(bfs(graph, 'A'))# {'B', 'C', 'A', 'F', 'D', 'E'}

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)#here deque with leftpop() O(1) is better than queue pop(0) O(n)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

print(list(bfs_paths(graph, 'A', 'F')))# [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

#first result is the shortest path
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

print("Shortest path is: ", shortest_path(graph, 'A', 'F'))# ['A', 'C', 'F']
