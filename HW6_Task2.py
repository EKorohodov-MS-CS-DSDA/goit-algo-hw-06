from collections import deque
from HW6_Task1 import get_graph

def DFS(graph, start):
    visited = {}
    stack = [start]

    while stack:
        adj_node = stack.pop()
        if adj_node not in visited:
            visited[adj_node] = True
            stack.extend(graph[adj_node])

    return list(visited.keys())

def BFS(graph,start):
    visited = {}
    queue = deque([start])

    visited[start] = True
    while queue:
        node = queue.popleft()
        for adj_node in graph[node]:
            if adj_node not in visited:
                visited[adj_node] = True
                queue.append(adj_node)
    return list(visited.keys())

def main():
    G = get_graph()
    print(f"BFS: {BFS(G, 'Kyiv')}")
    print(f"DFS: {DFS(G, 'Kyiv')}")

if __name__ == '__main__':
    main()