import flask as Flask
from algorithm.astar import astar
from algorithm.dijkstra import dijkstra
from algorithm.bfs import bfs

from utils.map_utils import convert_path, get_coordinates

"""
Controller class
"""


class Controller(object):

    def _init_(self):
        self.model = None

    def set_model(self, model):
        self.model = model
        self.app = Flask(__name__)
        graphs = {}

    def get_route(self, graph, source_node, dest_node, algorithm='AStar', limit=0, mode='min'):
        if algorithm == 'AStar':
            path = astar(graph, source_node, dest_node, limit, mode)

        elif algorithm == 'Dijkstra':
            path = dijkstra(graph, source_node, dest_node, limit, mode)

        elif algorithm == 'BFS':
            path = bfs(graph, source_node, dest_node, limit, mode)

        print(path)

        path, path_data = convert_path(graph, path)

        print(path)
        print(path_data)
        return {'path': path, 'path_data': path_data}

    def handle_request(self, graph):
        # #Load map
        # graph = load_map()
        #
        #Get lt and long of source and dest
        source_node = get_coordinates(self.model.get_source())
        dest_node = get_coordinates(self.model.get_destination())

        #Get route
        return self.get_route(graph, source_node, dest_node,
                              self.model.get_algorithm(),
                              self.model.get_limit(),
                              self.model.get_mode())
