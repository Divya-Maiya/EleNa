import unittest

import networkx as nx

from src.backend.algorithm.astar import AStar
from src.backend.utils import graph_utils
from test.helper_utils import test_setup

graph = test_setup()


class TestAstar(unittest.TestCase):
    global graph

    def test_shortest_path(self):
        start_node = 66692331
        dest_node = 66737929
        astar = AStar()

        received_shortest_path = astar.get_shortest_path(graph, start_node, dest_node)
        expected_shortest_path = nx.shortest_path(graph, start_node, dest_node, weight='length')

        self.assertEqual(received_shortest_path, expected_shortest_path)

    def test_shortest_path_invalid(self):
        start_node = 0
        dest_node = 1
        astar = AStar()

        with self.assertRaises(Exception) as context:
            astar.get_shortest_path(graph, start_node, dest_node)

        self.assertTrue(
            'Start node is not in the map. Please restart with the correct start node' in str(context.exception))

    def test_min_elevation(self):
        start_node = 66692331
        dest_node = 66737929
        limit = 5

        astar = AStar()
        received_min_elevation_path = astar.astar(graph, start_node, dest_node, limit=limit, mode='min')
        min_elevation = graph_utils.get_path_elevation(graph, received_min_elevation_path)
        max_path_length = graph_utils.get_path_length(graph, received_min_elevation_path)

        received_shortest_path = astar.astar(graph, start_node, dest_node, limit=limit, mode='length')
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

        astar = AStar()
        received_min_elevation_path = astar.astar(graph, start_node, dest_node, limit=limit, mode='max')
        max_elevation = graph_utils.get_path_elevation(graph, received_min_elevation_path)
        max_path_length = graph_utils.get_path_length(graph, received_min_elevation_path)

        received_shortest_path = astar.astar(graph, start_node, dest_node, limit=limit, mode='length')
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
