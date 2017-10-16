import networkx
import matplotlib.pyplot as plt

graph = networkx.Graph()
graph.add_nodes_from([0, 1, 2, 3, 4, 5])
graph.add_edge(0, 1, color='red')
graph.add_edge(0, 2, color='green')
graph.add_edge(0, 4, color='blue')
graph.add_edge(1, 2, color='blue')
graph.add_edge(1, 3, color='green')
graph.add_edge(2, 5, color='red')
graph.add_edge(3, 4, color='red')
graph.add_edge(3, 5, color='blue')
graph.add_edge(4, 5, color='green')
networkx.draw(graph, with_labels=True, font_weight='bold')
plt.show()

class Level():
    def __init__(self, level_num, map_num, scroll_num, start, end, crystals, flow_colors):
        self.level_num = level_num
        self.map_num = map_num
        self.scroll_num = scroll_num
        self.start = start
        self.end = end
        self.crystals = crystals
        self.flow_colors = flow_colors
        self.solution = None

class Scroll():
    def __init__(self, scroll_num, flow):
        pass

class Map():
    def __init__(self, map_num, graph):
        pass

level_1 = Level(1, 5, 3, [], ['red', 'red', 'green', 'green'])

