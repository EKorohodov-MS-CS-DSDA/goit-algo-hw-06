import networkx as nx
import matplotlib.pyplot as plt


graph = {
    "Kyiv": {"Makariv": 50, "Borodyanka": 45, "Fastiv": 60},
    "Makariv": {"Kyiv": 50, "Radomyshl": 40, "Borodyanka": 20, "Kocheriv": 35},
    "Borodyanka": {"Kyiv": 45, "Makariv": 20},
    "Fastiv": {"Kyiv": 60, "Brusyliv": 35},
    "Brusyliv": {"Fastiv": 35, "Popil'nya": 35, "Kocheriv": 15},
    "Popil'nya": {"Brusyliv": 35, "Zhytomyr": 60},
    "Kocheriv": {"Brusyliv": 15, "Radomyshl": 15, "Makariv": 35, "Korostyshiv": 20},

    "Radomyshl": {"Kocheriv": 15, "Makariv": 40, "Cherniakhiv": 40},
    "Cherniakhiv": {"Radomyshl": 40, "Zhytomyr": 20},
    "Korostyshiv": {"Kocheriv": 20, "Zhytomyr": 25},
    "Zhytomyr": {"Cherniakhiv": 20, "Korostyshiv": 25, "Popil'nya": 65}

}

gr = {
    from_: {
        to_: {'weight': w}
        for to_, w in to_nodes.items()
    }
    for from_, to_nodes in graph.items()
}


def draw_graph(graph):

    pos ={
        "Kyiv": (10, 0),
        "Borodyanka": (7, 0.3),
        "Makariv": (6, 0.05),
        "Kocheriv": (4, -0.05),
        "Korostyshiv": (2, 0.05),
        "Fastiv": (7, -0.4),
        "Brusyliv": (5, -0.2),
        "Popil'nya": (3, -0.5),
        "Cherniakhiv": (0.1, 0.2),
        "Radomyshl": (3.8, 0.2),
        "Zhytomyr": (0, 0)
    }
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

def get_graph():
    return nx.from_dict_of_dicts(gr, create_using=nx.Graph)

def main():
    draw_graph(get_graph())

if __name__ == '__main__':
    main()