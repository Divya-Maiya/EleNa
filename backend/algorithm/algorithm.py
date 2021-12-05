import abc

"""
Template method for all algorithms to implement
"""


class Algorithm(abc.ABC):
    @abc.abstractmethod
    def get_shortest_path(self, graph, start_node, dest_node, edge_weight):
        pass
