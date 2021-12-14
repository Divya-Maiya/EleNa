import unittest

import networkx as nx
from mockito import when, unstub, verify

from src.backend.algorithm.astar import AStar
from src.backend.algorithm.dijkstra import Dijkstra
from src.backend.controller.controller import Controller
from src.backend.model.model import Model
from test.helper_utils import test_setup

graph = test_setup()


class TestController(unittest.TestCase):
    global graph

    def test_handle_request(self):
        when(Controller).get_route(...).thenReturn({'path': [], 'path_data': []})

        model = Model()
        model.set_limit(0.5)
        model.set_destination("1 Rolling Green Dr, Amherst, MA 01002")
        model.set_source("Brandywine Dr, Amherst, MA 01002")
        model.set_algorithm("Dijkstra")
        model.set_mode("max")

        controller = Controller()
        controller.set_model(model)

        controller.handle_request(graph)

        verify(Controller, times=1).get_route(...)

        unstub()

    def test_get_route_AStar(self):
        start_node = 66692331
        dest_node = 66737929

        when(AStar).astar(...).thenReturn(nx.shortest_path(graph, start_node, dest_node, weight='length'))

        model = Model()
        model.set_limit(0.5)
        model.set_destination("1 Rolling Green Dr, Amherst, MA 01002")
        model.set_source("Brandywine Dr, Amherst, MA 01002")
        model.set_algorithm("Dijkstra")
        model.set_mode("max")

        controller = Controller()
        controller.set_model(model)

        controller.get_route(graph, start_node, dest_node, 'AStar', 50, max)

        verify(AStar, times=1).astar(...)

        unstub()

    def test_get_route_AStar_exception(self):
        when(AStar).astar(...).thenReturn("")

        model = Model()
        model.set_limit(0.5)
        model.set_destination("1 Rolling Green Dr, Amherst, MA 01002")
        model.set_source("Brandywine Dr, Amherst, MA 01002")
        model.set_algorithm("Dijkstra")
        model.set_mode("max")

        controller = Controller()
        controller.set_model(model)

        with self.assertRaises(Exception) as context:
            controller.get_route(graph, 123, 456, 'AStar', 50, max)

        self.assertTrue('Unable to find a route' in str(context.exception))

        verify(AStar, times=1).astar(...)

        unstub()

    def test_get_route_Dijkstra(self):
        start_node = 66692331
        dest_node = 66737929

        when(Dijkstra).dijkstra(...).thenReturn(nx.shortest_path(graph, start_node, dest_node, weight='length'))

        model = Model()
        model.set_limit(0.5)
        model.set_destination("1 Rolling Green Dr, Amherst, MA 01002")
        model.set_source("Brandywine Dr, Amherst, MA 01002")
        model.set_algorithm("Dijkstra")
        model.set_mode("max")

        controller = Controller()
        controller.set_model(model)

        controller.get_route(graph, start_node, dest_node, 'Dijkstra', 50, max)

        verify(Dijkstra, times=1).dijkstra(...)

        unstub()

    def test_get_route_Dijkstra_exception(self):
        when(Dijkstra).dijkstra(...).thenReturn("")

        model = Model()
        model.set_limit(0.5)
        model.set_destination("1 Rolling Green Dr, Amherst, MA 01002")
        model.set_source("Brandywine Dr, Amherst, MA 01002")
        model.set_algorithm("Dijkstra")
        model.set_mode("max")

        controller = Controller()
        controller.set_model(model)

        with self.assertRaises(Exception) as context:
            controller.get_route(graph, 123, 456, 'Dijkstra', 50, max)

        self.assertTrue('Unable to find a route' in str(context.exception))

        verify(Dijkstra, times=1).dijkstra(...)

        unstub()


if __name__ == '__main__':
    unittest.main()
