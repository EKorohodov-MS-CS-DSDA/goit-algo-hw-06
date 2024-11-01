from HW6_Task1 import draw_graph, get_graph
import networkx as nx


def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        cur_node = min(unvisited, key=lambda node: distances[node])

        if distances[cur_node] == float('infinity'):
            break

        for adj_node, weight in graph[cur_node].items():
            distance = distances[cur_node] + weight.get('weight', 1)

            if distance < distances[adj_node]:
                distances[adj_node] = distance

        unvisited.remove(cur_node)

    return distances


def main():
    print(dijkstra(get_graph(), 'Kyiv'))

if __name__ == '__main__':
    main()