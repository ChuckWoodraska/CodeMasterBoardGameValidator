import networkx
import matplotlib.pyplot as plt
from transitions import Machine

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

edges = graph.edges()
colors = [graph[u][v]['color'] for u,v in edges]
networkx.draw(graph, edge_color=colors, with_labels=True, font_weight='bold')
plt.show()


class Level:
    def __init__(self, level_num, map, scroll, start, end, crystals, trolls, flow_colors):
        self.level_num = level_num
        self.map = map
        self.scroll = scroll
        self.start = start
        self.end = end
        self.crystals = crystals
        self.trolls = trolls
        self.flow_colors = flow_colors
        self.solution = None


# FSM
class Scroll:
    def __init__(self, scroll_num, states, transitions):
        # Initialize the state machine
        self.machine = Machine(model=self, states=states, ordered_transitions=transitions, initial=states[0])




# Graph
class Map:
    def __init__(self, map_num, graph):
        self.map_num = map_num
        self.graph = graph


class Solution:
    def __init__(self, level, solution_flow):
        self.level = level
        self.solution_flow = solution_flow
        self.path = []

    def run(self):
        # check_valid_flow(len(self.level.scroll.states), len(self.solution_flow))
        self.path.append(self.level.start)
        self.step()
        # if self.check_valid_state():
        while self.level.scroll.next_state() and self.level.scroll.state != 'End':
            self.step()
        print(self.path)
        self.check_win()

    def check_win(self):
        if self.level.end == self.path[-1]:
            print('Winner!')
        else:
            print('Try Again.')

    def check_valid_state(self):
        # if self.level.scroll.state
        return True

    def step(self):
        node = self.level.map.graph[self.path[-1]]
        color = self.solution_flow[int(self.level.scroll.state)]
        self.find_neighbor_by_color(node, color)

    def find_neighbor_by_color(self, node, color):
        for key in node:
            if node[key].get('color') == color:
                self.path.append(key)
                return


map_1 = Map(1, graph)
scroll_1 = Scroll(1, ['0', '1', '2', '3', 'End'], ['0', '1', '2', '3', 'End'])
level_1 = Level(1, map_1, scroll_1, 5, 3, [], [], ['red', 'red', 'green', 'green'])
Solution(level_1, ['red', 'green', 'red', 'green']).run()



# print(find_neighbor_by_color(graph[5], 'red'))