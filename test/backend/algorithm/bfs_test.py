import unittest
import networkx as nx
from src.backend.algorithm.bfs import BFS
import os

from src.backend.utils.map_utils import load_map


def test_setup():
    os.chdir("../..")
    return load_map("resources/graph_Amherst.pkl", changeDir=1)


graph = test_setup()


class TestBfs(unittest.TestCase):
    global graph

    def test_shortest_path(self):
        start_node = 66692331
        dest_node = 66737929
        bfs = BFS()

        received_shortest_path = bfs.get_shortest_path(graph, start_node, dest_node)
        expected_shortest_path = nx.shortest_path(graph, start_node, dest_node, weight='length')

        self.assertEqual(received_shortest_path[0], expected_shortest_path[0])

    def test_shortest_path_invalid(self):
        start_node = 0
        dest_node = 1
        bfs = BFS()

        with self.assertRaises(Exception) as context:
            bfs.get_shortest_path(graph, start_node, dest_node)

        self.assertTrue(
            'Start node is not in the map. Please restart with the correct start node' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
