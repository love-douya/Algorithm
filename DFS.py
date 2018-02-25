graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print(dfs(graph, 'A'))# {'E', 'D', 'F', 'A', 'C', 'B'}

def dfs_recursion(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_recursion(graph, next, visited)
    return visited

print(dfs_recursion(graph, 'A'))# {'E', 'D', 'F', 'A', 'C', 'B'}

#use generator to return all possible paths between a start and goal vertex
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

print(list(dfs_paths(graph, 'A', 'F')))#[['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

def dfs_paths_yield_from(graph, start, goal, path = None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths_yield_from(graph, next, goal, path + [next])

print(list(dfs_paths_yield_from(graph, 'C', 'F')))# [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]