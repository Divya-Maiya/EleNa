import unittest
from mockito import *
import osmnx

from src.backend.utils.map_utils import *
from src.backend.algorithm.astar import *
from test.helper_utils import test_setup

graph = test_setup()


class TestGraphUtils(unittest.TestCase):
    global graph

    def test_shortest_path_optimizer(self):
        source_node = 66692331
        successor_graph = graph._succ if graph.is_directed() else graph._adj
        expected_coords = -72.532612, 42.406836
        when(osmnx).nearest_nodes(...).thenReturn((source_node, 0))
        when(osmnx).geocode(...).thenReturn(expected_coords)

        source_node = get_node_from_address(graph, "Random String")
        neighbor = 66644252
        w = successor_graph[source_node][66644252]

        def weight_(source, dest, edge_data):
            return min(attr.get('length', 1) for attr in edge_data.values())

        expected_function = weight_
        obtained_function = shortest_path_optimizer(graph, 'length')
        self.assertEqual(obtained_function(source_node, neighbor, w), expected_function(source_node, neighbor, w))

        verify(osmnx, times=1).nearest_nodes(...)
        verify(osmnx, times=1).geocode(...)
        unstub()

        # clean up

    def test_get_path_length(self):
        a = AStar()

        source_node = 66692331
        neighbor = 66644252
        expected_coords = -72.532612, 42.406836
        when(osmnx).nearest_nodes(...).thenReturn((source_node, 0))
        when(osmnx).geocode(...).thenReturn(expected_coords)

        source_node = get_node_from_address(graph, "Random String")

        shortest_path = [source_node, neighbor]
        expected_length = graph[source_node][neighbor][0]['length']
        obtained_path = get_path_length(graph, shortest_path)
        self.assertEqual(obtained_path, expected_length)

        verify(osmnx, times=1).nearest_nodes(...)
        verify(osmnx, times=1).geocode(...)

        unstub()

    def test_get_path_elevation(self):
        a = AStar()

        source_node = 66692331
        neighbor = 66644252
        expected_coords = -72.532612, 42.406836
        when(osmnx).nearest_nodes(...).thenReturn((source_node, 0))
        when(osmnx).geocode(...).thenReturn(expected_coords)

        source_node = get_node_from_address(graph, "Random String")

        shortest_path = [source_node, neighbor]
        expected_elevation = max(0, graph.nodes[neighbor]['elevation'] - graph.nodes[source_node]['elevation'])
        obtained_elevation = get_path_elevation(graph, shortest_path)
        self.assertEqual(obtained_elevation, expected_elevation)

        verify(osmnx, times=1).nearest_nodes(...)
        verify(osmnx, times=1).geocode(...)

        unstub()

    def test_get_l1_distance(self):
        a = AStar()

        source_node = 66692331
        neighbor = 66644252

        shortest_path = [source_node, neighbor]
        expected_elevation = max(0, graph.nodes[neighbor]['elevation'] - graph.nodes[source_node]['elevation'])
        obtained_elevation = get_path_elevation(graph, shortest_path)
        self.assertEqual(obtained_elevation, expected_elevation)


if __name__ == '__main__':
    unittest.main()
