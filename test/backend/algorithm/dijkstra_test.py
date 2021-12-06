import os
import unittest
import networkx as nx

from src.backend.algorithm.dijkstra import Dijkstra
from src.backend.utils.map_utils import load_map


class MyTestCase(unittest.TestCase):
    graph = None
    limit = 5

    def test_get_shortest_path(self):
        print(os.getcwd())
        os.chdir("../..")
        graph = load_map("resources/graph_Amherst.pkl", changeDir=1)
        start_node = 66692331
        dest_node = 66737929
        received_shortest_path = Dijkstra().get_shortest_path(graph, start_node, dest_node)
        expected_shortest_path = nx.shortest_path(graph, start_node, dest_node, weight='length')
        self.assertEqual(received_shortest_path, expected_shortest_path)

    # def test_dijkstra(self):


if __name__ == '__main__':
    unittest.main()
