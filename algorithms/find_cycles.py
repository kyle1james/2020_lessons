g = {1: (2,), 2: (3,), 3: (1,)} # -> True

graph = {
    0: [1, 2, 3],
    1: [0, 5],
    2: [0, 3],
    3: [0, 2, 4],
    4: [3],
    5: [1]
}

"""
2 --- 0 --- 1 --- 5
  \   |
   \  |
      3 --- 4
"""

def find_cycle(graph):
    discover = {v:False for v in graph}
    found = [False]

    for vertex in graph:
        if found[0]:
            break
        if not discover[vertex]:
            visit(graph, vertex, vertex, discover, found)
    return found[0]


def visit(graph, node, prev_node, discover, found):
    if found[0]:
        return

    discover[node] = True
    for edge in graph[node]:
        if discover[edge] and edge != prev_node:
            found[0] = True
            return
        if discover[edge] == False:
            visit(graph, edge, node, discover, found)


def bfs_cycle(graph):
    visited = {v:False for v in graph}
    start = list(graph.keys())[-1]
    queue = [start]
    parent = start

    while queue:
        node = queue.pop(0)

        for edge in graph[node]:
            if parent != edge:
                if visited[edge]:
                    print(edge)
                    #return True
                if not visited[edge]:
                    queue.append(edge)
        visited[node] = True
        parent = node
    return False


print(find_cycle(graph))
print(bfs_cycle(graph))
