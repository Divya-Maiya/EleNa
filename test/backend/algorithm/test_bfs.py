import unittest
import networkx as nx
from src.backend.algorithm.bfs import BFS
from test.helper_utils import test_setup

graph = test_setup()


class TestBfs(unittest.TestCase):
    global graph

    def test_shortest_path(self):
        start_node = 66692331
        dest_node = 66737929
        bfs = BFS()

        received_shortest_path = bfs.bfs(graph, start_node, dest_node, limit=5, mode='length')
        expected_shortest_path = nx.shortest_path(graph, start_node, dest_node, weight='length')

        self.assertEqual(received_shortest_path[0], expected_shortest_path[0])

    def test_shortest_path_invalid(self):
        start_node = 0
        dest_node = 1
        bfs = BFS()

        with self.assertRaises(Exception) as context:
            bfs.bfs(graph, start_node, dest_node, limit=5, mode='length')

        self.assertTrue('Start node not in graph' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
