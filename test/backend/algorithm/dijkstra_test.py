import os
import unittest
import networkx as nx

from src.backend.algorithm.dijkstra import Dijkstra
from src.backend.utils import graph_utils
from src.backend.utils.map_utils import load_map


def test_setup():
    os.chdir("../..")
    return load_map("resources/graph_Amherst.pkl", changeDir=1)


graph = test_setup()


class MyTestCase(unittest.TestCase):
    global graph

    def test_get_shortest_path(self):
        start_node = 66692331
        dest_node = 66737929
        received_shortest_path = Dijkstra().get_shortest_path(graph, start_node, dest_node)
        expected_shortest_path = nx.shortest_path(graph, start_node, dest_node, weight='length')
        self.assertEqual(received_shortest_path, expected_shortest_path)

    def test_get_shortest_path_invalid(self):
        start_node = 0
        dest_node = 1
        received_shortest_path = Dijkstra().get_shortest_path(graph, start_node, dest_node)
        expected_shortest_path = []
        self.assertEqual(received_shortest_path, expected_shortest_path)

    def test_min_elevation(self):
        start_node = 66692331
        dest_node = 66737929
        limit = 5

        dijkstra = Dijkstra()
        received_min_elevation_path = dijkstra.get_shortest_path(graph, start_node, dest_node, edge_weight='min')
        min_elevation = graph_utils.get_path_elevation(graph, received_min_elevation_path)
        max_path_length = graph_utils.get_path_length(graph, received_min_elevation_path)

        received_shortest_path = dijkstra.get_shortest_path(graph, start_node, dest_node, edge_weight='length')
        regular_elevation = graph_utils.get_path_elevation(graph, received_shortest_path)
        regular_path_length = graph_utils.get_path_length(graph, received_shortest_path)
        max_length = regular_path_length * (1 + limit)

        # For debugging
        if max_path_length <= max_length and min_elevation <= regular_elevation:
            print("Test Passed")
        else:
            print("Test Failed")

        self.assertLessEqual(max_path_length, max_length)
        self.assertLessEqual(min_elevation, regular_elevation)

    def test_max_elevation(self):
        start_node = 66692331
        dest_node = 66737929
        limit = 5

        dijkstra = Dijkstra()
        received_min_elevation_path = dijkstra.get_shortest_path(graph, start_node, dest_node, edge_weight='max')
        max_elevation = graph_utils.get_path_elevation(graph, received_min_elevation_path)
        max_path_length = graph_utils.get_path_length(graph, received_min_elevation_path)

        received_shortest_path = dijkstra.get_shortest_path(graph, start_node, dest_node, edge_weight='length')
        regular_elevation = graph_utils.get_path_elevation(graph, received_shortest_path)
        regular_path_length = graph_utils.get_path_length(graph, received_shortest_path)
        max_length = regular_path_length * (1 + limit)

        # For debugging
        if max_path_length <= max_length and max_elevation >= regular_elevation:
            print("Test Passed")
        else:
            print("Test Failed")
        print("\n")

        self.assertLessEqual(max_path_length, max_length)
        self.assertGreaterEqual(max_elevation, regular_elevation)


if __name__ == '__main__':
    unittest.main()
