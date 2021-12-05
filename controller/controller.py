from algorithm.astar import astar
from algorithm.dijkstra import dijkstra
from algorithm.bfs import bfs
from utils.map_utils import convert_path, get_coordinates, get_node_from_address
import osmnx as ox

"""
Controller class
"""


class Controller(object):

    def _init_(self):
        self.model = None

    def set_model(self, model):
        self.model = model

    def get_route(self, graph, source_node, dest_node, algorithm='AStar', limit=0, mode='min'):
        path = ""
        if algorithm == 'AStar':
            path = astar(graph, source_node, dest_node, limit, mode)

        elif algorithm == 'Dijkstra':
            path = dijkstra(graph, source_node, dest_node, limit, mode)

        elif algorithm == 'BFS':
            path = bfs(graph, source_node, dest_node, limit, mode)

        final_path, path_data = convert_path(graph, path)

        # print(path)
        print(path_data)
        ox.plot_graph_route(graph, path)
        return {'path': final_path, 'path_data': path_data}

    def handle_request(self, graph):
        # #Load map
        # graph = load_map()
        #
        #Get lt and long of source and dest
        source_node = get_node_from_address(graph, self.model.get_source())
        dest_node = get_node_from_address(graph, self.model.get_destination())

        #Get route
        return self.get_route(graph, source_node, dest_node,
                              self.model.get_algorithm(),
                              self.model.get_limit(),
                              self.model.get_mode())
