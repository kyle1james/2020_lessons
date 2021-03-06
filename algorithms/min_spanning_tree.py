
'''
Prim’s Algorithm Psuedocode
1 Maintain priority queue Q on V \ S, where v.key = min{w(u, v) | u ∈ S}
2 Q = V

3 Choose arbitrary start vertex s ∈ V , s.key = ∅

4 for v in V \ {s}
5 v.key = ∞

6 while Q is not empty

7 u = Extract-Min(Q), add u to S

8 for v ∈ Adj[u]

9 if v ∈ Q and v /∈ S and w(u, v) < v.key:

10 v.key = w(u, v) (via a Decrease-Key operation)

11 v.parent = u

12 return {{v, v.parent} | v ∈ V \ {s}}
 

'''
import random, heapq


def prims_v(adj_list, start):
    queue = [start]
    s = []
    heapq.heapify(queue)

    for vertex in adj_list:
        while queue:
            _ ,node = heapq.heappop(queue)
            s.append(node)
            best_edge_weight = float('inf')
            best_edge = None
            for edge in adj_list[node]:
                if edge[0] not in s and edge[1] < best_edge_weight:
                    best_edge_weight = edge[1]
                    best_edge = edge[0]
            if best_edge != None:
                heapq.heappush(queue, (best_edge_weight, best_edge))
        if vertex not in s:
            queue.append((0,vertex))
    return s 



#def find_min(adj_list, tree):
    best = float('inf')
    current = None
    
    for vertex in tree:
        for edge in adj_list[vertex]:
            if edge[0] not in tree and edge[1] < best:
                best = edge[1]
                current = edge[0]
                parent = vertex
    return current, parent, best

def prims(adj_list, start):
    tree = [start]
    connections = []
    total = 0
    while len(tree) < len(adj_list):
        next_vertex, parent, best = find_min(adj_list, tree)
        tree.append(next_vertex)
        total += best
        connections.append((parent, next_vertex))
    return connections, tree, total



adj_list = {
'a':[('b', 8), ('c', 6), ('d', 5)],
'b':[('a', 8), ('d', 4)],
'c':[('a',6), ('d', 3)],
'd':[('a',5), ('b',4), ('c',3)]
}

adj_list2 = {
'a':[('b',8), ('f',1), ('h', 6), ('e',5)],
'b':[('a',8), ('c',4), ('f',2)],
'c':[('b',4), ('f',2), ('g',7)],
'g':[('c',7), ('f',9)],
'f':[('g',9), ('c',2), ('b', 6), ('a',1), ('h',5), ('e',1)],
'h':[('f',5), ('a',6), ('e',3)],
'e':[('a',5), ('h',3), ('f',1)]
}


#print(prims(adj_list2, 'a'))
print(prims_v(adj_list2, (0,'a')))
