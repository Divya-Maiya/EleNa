from algorithm.astar import astar
from algorithm.dijkstra import dijkstra
from algorithm.bfs import bfs
from utils.map_utils import convert_path

"""
Controller class
"""


class Controller(object):

    def _init_(self):
        self.model = None

    def set_model(self, model):
        self.model = model

    def get_route(self, graph, start_node, dest_node, algorithm='AStar', limit=0, mode='min'):
        if algorithm == 'AStar':
            path = astar(graph, start_node, dest_node, limit, mode)

        elif algorithm == 'Dijkstra':
            path = dijkstra(graph, start_node, dest_node, limit, mode)

        elif algorithm == 'BFS':
            path = bfs(graph, start_node, dest_node, limit, mode)

        print(path)

        path, path_data = convert_path(graph, path)
        return {'path': path, 'path_data': path_data}
